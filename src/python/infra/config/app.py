import os
from enum import StrEnum


class APIProvider(StrEnum):
    OPENAI = "openai"


class Config:
    pass


class OpenAIConfig(Config):
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY", "")
        self.base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
        self.model = os.getenv("OPENAI_MODEL", "gpt-4.1")
        self.timeout = int(os.getenv("OPENAI_TIMEOUT", "30"))
        self.max_retries = int(os.getenv("OPENAI_MAX_RETRIES", "3"))


class AppConfig:
    def __init__(self):
        self.provider = APIProvider(os.getenv("API_PROVIDER", APIProvider.OPENAI.value))
        self.provider_config = self.get_provider_settings(self.provider)

    @staticmethod
    def get_provider_settings(provider: APIProvider):
        if provider == APIProvider.OPENAI:
            return OpenAIConfig()
        raise ValueError(f"Unsupported API provider: {provider}")
