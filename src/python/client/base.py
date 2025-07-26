import asyncio
from abc import ABC, abstractmethod

from client.storage import Storage
from infra.config.app import Config


class BaseClient(ABC):
    def __init__(self, config: Config, storage: Storage):
        self.config = config
        self.storage = storage

    @abstractmethod
    async def get(self, context: str) -> str:
        """
        Abstract method to get a response from the API.
        :param context: The input text and chat context for the API.
        :return: Response text from the API.
        """
        pass

    async def run(self):
        print("Write your question to start the conversation. Type 'exit' to quit.")
        while True:
            user_input = input("> ")

            if not user_input.strip():
                continue

            if user_input.lower() == "exit":
                break
            self.storage.add({"role": "user", "content": user_input})
            spinner_task = asyncio.create_task(self._spinner())
            try:
                response = await self.get(str(self.storage.get_history()))
            finally:
                spinner_task.cancel()
                try:
                    await spinner_task
                except asyncio.CancelledError:
                    pass
            self.storage.add({"role": "assistant", "content": response})
            print(f"AI: {response}")

    @staticmethod
    async def _spinner():
        while True:
            print("..", end="\r", flush=True)
            await asyncio.sleep(0.5)
