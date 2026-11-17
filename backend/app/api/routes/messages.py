from fastapi import APIRouter, Depends, HTTPException, status, WebSocket, WebSocketDisconnect
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from app.api.deps import get_db, get_current_user
from app.models.user import User
from app.models.message import Conversation, Message, ConversationType
from app.schemas.message import (
    ConversationCreate,
    ConversationResponse,
    MessageCreate,
    MessageResponse,
    WebSocketMessage
)
from app.websocket.manager import ConnectionManager
from typing import List

router = APIRouter(prefix="/messages", tags=["messages"])
manager = ConnectionManager()


@router.get("/conversations", response_model=list[ConversationResponse])
async def get_conversations(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Get all conversations for the current user.
    """
    conversations_query = select(Conversation).where(
        current_user.id == Conversation.participant_ids.any()
    ).order_by(Conversation.created_at.desc())

    result = await db.execute(conversations_query)
    conversations = result.scalars().all()

    return [
        ConversationResponse(
            id=str(conv.id),
            type=conv.type,
            participant_ids=conv.participant_ids,
            created_at=conv.created_at
        )
        for conv in conversations
    ]


@router.post("/conversations", response_model=ConversationResponse, status_code=status.HTTP_201_CREATED)
async def create_conversation(
    conversation_data: ConversationCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Start a new conversation.
    """
    # Ensure current user is in participants
    if current_user.id not in conversation_data.participant_ids:
        conversation_data.participant_ids.append(current_user.id)

    # Ensure exactly 2 participants
    if len(conversation_data.participant_ids) != 2:
        raise HTTPException(
            status_code=400,
            detail="Conversation must have exactly 2 participants"
        )

    # Check if conversation already exists between these users
    existing_query = select(Conversation).where(
        Conversation.participant_ids.contains(conversation_data.participant_ids)
    )
    existing_result = await db.execute(existing_query)
    existing = existing_result.scalar_one_or_none()

    if existing:
        # Set participants in manager for existing conversation
        manager.set_conversation_participants(
            str(existing.id),
            set(existing.participant_ids)
        )
        return ConversationResponse(
            id=str(existing.id),
            type=existing.type,
            participant_ids=existing.participant_ids,
            created_at=existing.created_at
        )

    # Create new conversation
    conversation = Conversation(
        type=conversation_data.type,
        participant_ids=conversation_data.participant_ids
    )

    db.add(conversation)
    await db.commit()
    await db.refresh(conversation)

    # Set participants in manager for new conversation
    manager.set_conversation_participants(
        str(conversation.id),
        set(conversation.participant_ids)
    )

    return ConversationResponse(
        id=str(conversation.id),
        type=conversation.type,
        participant_ids=conversation.participant_ids,
        created_at=conversation.created_at
    )


@router.get("/conversations/{conversation_id}/messages", response_model=list[MessageResponse])
async def get_conversation_messages(
    conversation_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Get message history for a conversation.
    """
    # Verify user is a participant in the conversation
    conversation_query = select(Conversation).where(
        Conversation.id == conversation_id
    )
    conversation_result = await db.execute(conversation_query)
    conversation = conversation_result.scalar_one_or_none()

    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")

    if current_user.id not in conversation.participant_ids:
        raise HTTPException(
            status_code=403,
            detail="You are not a participant in this conversation"
        )

    # Get messages
    messages_query = select(Message).where(
        Message.conversation_id == conversation_id
    ).order_by(Message.created_at.asc())

    result = await db.execute(messages_query)
    messages = result.scalars().all()

    return [
        MessageResponse(
            id=str(msg.id),
            conversation_id=msg.conversation_id,
            sender_id=msg.sender_id,
            content=msg.content,
            read_at=msg.read_at,
            created_at=msg.created_at
        )
        for msg in messages
    ]


@router.patch("/conversations/{conversation_id}/read")
async def mark_conversation_read(
    conversation_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Mark all messages in a conversation as read for the current user.
    """
    # Verify user is a participant
    conversation_query = select(Conversation).where(
        Conversation.id == conversation_id
    )
    conversation_result = await db.execute(conversation_query)
    conversation = conversation_result.scalar_one_or_none()

    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")

    if current_user.id not in conversation.participant_ids:
        raise HTTPException(
            status_code=403,
            detail="You are not a participant in this conversation"
        )

    # Mark all unread messages from other participants as read
    messages_query = select(Message).where(
        and_(
            Message.conversation_id == conversation_id,
            Message.sender_id != current_user.id,
            Message.read_at.is_(None)
        )
    )

    result = await db.execute(messages_query)
    messages = result.scalars().all()

    from datetime import datetime
    for message in messages:
        message.read_at = datetime.utcnow()

    await db.commit()

    return {"status": "success", "messages_marked_read": len(messages)}


@router.websocket("/ws/chat")
async def websocket_chat(websocket: WebSocket, token: str):
    """
    WebSocket endpoint for real-time messaging.
    """
    # Verify token (simplified - in production use proper JWT validation)
    try:
        # For now, accept any token - implement proper validation
        await websocket.accept()
        user_id = token  # In production, decode JWT to get user_id
        
        await manager.connect(user_id, websocket)
        
        try:
            while True:
                data = await websocket.receive_json()
                ws_message = WebSocketMessage(**data)
                
                if ws_message.type == "message":
                    # Save message to database
                    # This would require a database session - simplified for now
                    # In production, inject db session dependency
                    await manager.broadcast_to_conversation(
                        ws_message.conversation_id,
                        data,
                        exclude_user_id=user_id
                    )
                    
        except WebSocketDisconnect:
            manager.disconnect(user_id)
            
    except Exception as e:
        await websocket.close(code=1008)
