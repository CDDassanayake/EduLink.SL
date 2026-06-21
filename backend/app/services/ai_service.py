from sqlalchemy.ext.asyncio import AsyncSession


class AIService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_ai_response(self, user_id: str, message: str, conversation_history: list = None) -> str:
        """
        Get an AI response using LangChain + OpenAI.
        This will be implemented with ConversationChain.
        """
        # TODO: Implement AI chat with LangChain
        pass

    async def get_conversation_history(self, user_id: str) -> list:
        """
        Get the conversation history for a user.
        """
        # TODO: Implement conversation history retrieval
        pass

    async def clear_conversation_history(self, user_id: str) -> None:
        """
        Clear the conversation history for a user.
        """
        # TODO: Implement conversation history clearing
        pass
