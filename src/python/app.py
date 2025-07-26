import asyncio
import logging
import argparse
from dotenv import load_dotenv

from client.openai import OpenAIClient
from client.storage import InMemoryStorage
from infra.config.app import AppConfig
from infra.config.logger import setup_logger

logger = logging.getLogger(__name__)


async def app_run(env_file: str = None, level: str = "INFO"):
    setup_logger(level)
    if env_file:
        logger.info(f"Loading environment from {env_file}")
        load_dotenv(env_file)

    logger.info("Start app...")
    config = AppConfig()
    storage = InMemoryStorage()
    client = OpenAIClient(config.provider_config, storage)
    try:
        await client.run()
    except KeyboardInterrupt:
        return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the app with optional .env file")
    parser.add_argument("--env-file", type=str, help="Path to .env file")
    parser.add_argument(
        "--log-level",
        type=str,
        help="Level of logging",
    )

    args = parser.parse_args()
    try:
        asyncio.run(app_run(args.env_file, args.log_level))
    except KeyboardInterrupt:
        pass
