from sqlalchemy.ext.asyncio import AsyncSession
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from typing import List, Dict
import os


class AIService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.conversations: Dict[str, ConversationChain] = {}
        self._initialize_llm()

    def _initialize_llm(self):
        """Initialize the OpenAI LLM with LangChain"""
        self.llm = ChatOpenAI(
            model="gpt-4",
            temperature=0.7,
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )

    def _get_conversation_chain(self, user_id: str) -> ConversationChain:
        """Get or create a conversation chain for a user"""
        if user_id not in self.conversations:
            system_prompt = SystemMessagePromptTemplate.from_template(
                "You are an AI Career Guide for EduLink SL, a tutor booking marketplace for Sri Lankan students. "
                "You are trained on the Sri Lankan curriculum (O/L, A/L) and university entrance requirements. "
                "You can help students choose A/L subjects, understand university pathways, find the right tutors, "
                "or plan their study schedule. Be helpful, encouraging, and specific to the Sri Lankan context. "
                "When suggesting tutors, mention that they can find verified tutors on EduLink SL."
            )
            
            human_prompt = HumanMessagePromptTemplate.from_template("{input}")
            
            prompt = ChatPromptTemplate.from_messages([
                system_prompt,
                MessagesPlaceholder(variable_name="history"),
                human_prompt
            ])
            
            memory = ConversationBufferMemory(
                memory_key="history",
                return_messages=True
            )
            
            self.conversations[user_id] = ConversationChain(
                llm=self.llm,
                prompt=prompt,
                memory=memory,
                verbose=False
            )
        
        return self.conversations[user_id]

    async def get_ai_response(self, user_id: str, message: str, conversation_history: List[Dict] = None) -> str:
        """
        Get an AI response using LangChain + OpenAI.
        """
        try:
            chain = self._get_conversation_chain(user_id)
            response = await chain.apredict(input=message)
            return response
        except Exception as e:
            # Fallback response if AI fails
            return f"I apologize, but I'm having trouble connecting right now. Please try again later. Error: {str(e)}"

    async def get_conversation_history(self, user_id: str) -> List[Dict]:
        """
        Get the conversation history for a user.
        """
        if user_id in self.conversations:
            memory = self.conversations[user_id].memory
            history = memory.chat_memory.messages
            return [
                {
                    "role": "user" if msg.type == "human" else "ai",
                    "content": msg.content
                }
                for msg in history
            ]
        return []

    async def clear_conversation_history(self, user_id: str) -> None:
        """
        Clear the conversation history for a user.
        """
        if user_id in self.conversations:
            self.conversations[user_id].memory.clear()
            del self.conversations[user_id]
