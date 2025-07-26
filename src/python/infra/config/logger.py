import logging
import sys


def setup_logger(level: str):
    level = logging.getLevelName(level.upper())

    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(levelname)s - %(message)s",
        stream=sys.stdout,
    )
