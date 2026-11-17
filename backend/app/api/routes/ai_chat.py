from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_db, get_current_user
from app.models.user import User
from app.services.ai_service import AIService
from pydantic import BaseModel
from typing import List, Dict

router = APIRouter(prefix="/ai", tags=["ai"])


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


class HistoryResponse(BaseModel):
    history: List[Dict]


@router.post("/chat", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Send a message to the AI career guide and get a response.
    Only students can use this feature.
    """
    if current_user.role != "STUDENT":
        raise HTTPException(
            status_code=403,
            detail="Only students can use the AI career guide"
        )

    ai_service = AIService(db)
    response = await ai_service.get_ai_response(
        user_id=str(current_user.id),
        message=request.message
    )

    return ChatResponse(response=response)


@router.get("/chat/history", response_model=HistoryResponse)
async def get_chat_history(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Get the conversation history for the current user.
    Only students can use this feature.
    """
    if current_user.role != "STUDENT":
        raise HTTPException(
            status_code=403,
            detail="Only students can use the AI career guide"
        )

    ai_service = AIService(db)
    history = await ai_service.get_conversation_history(str(current_user.id))

    return HistoryResponse(history=history)


@router.delete("/chat/history")
async def clear_chat_history(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Clear the conversation history for the current user.
    Only students can use this feature.
    """
    if current_user.role != "STUDENT":
        raise HTTPException(
            status_code=403,
            detail="Only students can use the AI career guide"
        )

    ai_service = AIService(db)
    await ai_service.clear_conversation_history(str(current_user.id))

    return {"status": "success", "message": "Conversation history cleared"}
