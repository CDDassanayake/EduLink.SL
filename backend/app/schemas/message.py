from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import datetime
from app.models.message import ConversationType


class ConversationCreate(BaseModel):
    participant_ids: List[str]
    type: ConversationType


class ConversationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    type: ConversationType
    participant_ids: List[str]
    created_at: datetime


class MessageCreate(BaseModel):
    conversation_id: str
    content: str


class MessageResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    conversation_id: str
    sender_id: str
    content: str
    read_at: Optional[datetime] = None
    created_at: datetime


class WebSocketMessage(BaseModel):
    type: str
    conversation_id: Optional[str] = None
    content: Optional[str] = None
