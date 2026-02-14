from pydantic_settings import BaseSettings
from typing import Literal, Optional
from integrations.local_llm import LocalLLMService
from integrations.gemini_service import GeminiService

class LLMConfig(BaseSettings):
    LLM_PROVIDER: Literal["local", "gemini", "mock"] = "local"
    
    class Config:
        env_file = ".env"
        extra = "ignore"

config = LLMConfig()

class UnifiedLLM:
    _instance = None

    def __init__(self):
        self.provider = config.LLM_PROVIDER
        self.service = self._create_service()

    def _create_service(self):
        print(f"Initializing LLM Provider: {self.provider.upper()}")
        
        if self.provider == "gemini":
            try:
                return GeminiService()
            except Exception as e:
                import traceback
                print(f"Failed to init Gemini: {e}")
                traceback.print_exc()
                print("Falling back to Mock.")
                return MockService()
                
        elif self.provider == "local":
            # LocalLLMService handles its own mock fallback internally
            return LocalLLMService()
            
        elif self.provider == "mock":
            return MockService()
            
        return MockService()

    async def invoke(self, prompt: str) -> str:
        return await self.service.invoke(prompt)

class MockService:
    async def invoke(self, prompt: str) -> str:
        print(f"[MOCK LLM]: {prompt[:50]}...")
        if "Analyze this email" in prompt:
            return '{"is_valid": true, "confidence": 0.9, "reason": "Mock valid inquiry"}'
        elif "Extract structured client information" in prompt:
            return '{"client_name": "Mock User", "company": "Mock Corp", "project_type": "Web App", "requirements": ["Mock Req"], "timeline": "2 weeks", "budget": "$5000"}'
        elif "Create project breakdown" in prompt:
            return '{"phases": [{"name": "Phase 1", "tasks": ["Task A"], "duration": "1 week"}], "total_hours": 20, "complexity": "simple"}'
        elif "Write professional proposal" in prompt:
            return "Dear User,\n\nWe would love to build your app using Mock AI.\n\nBest,\nOttoMail"
        return "Mock response"
