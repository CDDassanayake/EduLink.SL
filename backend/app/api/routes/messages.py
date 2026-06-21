from fastapi import APIRouter

router = APIRouter(prefix="/messages", tags=["messages"])

# TODO: Implement message routes
# GET /conversations
# POST /conversations
# GET /conversations/{id}/messages
# PATCH /conversations/{id}/read
# WS /ws/chat
