from typing import Dict, Set
from fastapi import WebSocket
import json


class ConnectionManager:
    """
    WebSocket connection manager for real-time messaging.
    Manages active connections and broadcasts messages to conversation participants.
    """

    def __init__(self):
        # Active connections: user_id -> set of WebSocket connections
        self.active_connections: Dict[str, Set[WebSocket]] = {}
        # Conversation participants: conversation_id -> list of user_ids
        self.conversation_participants: Dict[str, Set[str]] = {}

    async def connect(self, user_id: str, websocket: WebSocket):
        """Connect a WebSocket for a user"""
        if user_id not in self.active_connections:
            self.active_connections[user_id] = set()
        self.active_connections[user_id].add(websocket)

    def disconnect(self, user_id: str, websocket: WebSocket):
        """Disconnect a WebSocket for a user"""
        if user_id in self.active_connections:
            self.active_connections[user_id].discard(websocket)
            if not self.active_connections[user_id]:
                del self.active_connections[user_id]

    async def send_personal_message(self, message: dict, user_id: str):
        """Send a message to all connections for a specific user"""
        if user_id in self.active_connections:
            for connection in self.active_connections[user_id]:
                await connection.send_json(message)

    def set_conversation_participants(self, conversation_id: str, participant_ids: Set[str]):
        """Store participants for a conversation"""
        self.conversation_participants[conversation_id] = participant_ids

    async def broadcast_to_conversation(
        self,
        conversation_id: str,
        message: dict,
        exclude_user_id: str = None
    ):
        """
        Broadcast a message to all participants in a conversation.
        """
        if conversation_id not in self.conversation_participants:
            return

        participants = self.conversation_participants[conversation_id]
        
        for user_id in participants:
            if exclude_user_id and user_id == exclude_user_id:
                continue
            await self.send_personal_message(message, user_id)


manager = ConnectionManager()
