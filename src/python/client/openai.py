from openai import AsyncOpenAI

from client.base import BaseClient
from client.storage import Storage
from infra.config.app import OpenAIConfig


class OpenAIClient(BaseClient):
    def __init__(self, config: OpenAIConfig, storage: Storage):
        super().__init__(config, storage)
        self.model = config.model
        self.client = AsyncOpenAI(
            api_key=config.api_key,
            base_url=config.base_url,
            timeout=config.timeout,
            max_retries=config.max_retries,
        )

    async def get(self, context: str) -> str:
        response = await self.client.responses.create(
            model=self.model,
            input=context,
        )
        return response.output_text
