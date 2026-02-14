from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic_settings import BaseSettings

class GeminiConfig(BaseSettings):
    GOOGLE_API_KEY: str = ""
    
    class Config:
        env_file = ".env"
        extra = "ignore"

config = GeminiConfig()

class GeminiService:
    def __init__(self):
        if not config.GOOGLE_API_KEY:
            raise ValueError("GOOGLE_API_KEY is required for Gemini Service")
            
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=config.GOOGLE_API_KEY,
            temperature=0.3
        )

    async def invoke(self, prompt: str) -> str:
        """Invoke Gemini LLM and return response text"""
        response = await self.llm.ainvoke(prompt)
        return response.content
