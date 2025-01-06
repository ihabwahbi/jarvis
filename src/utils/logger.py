import logging
import sys
from pathlib import Path
from typing import Optional


def setup_logger(
    name: str = "jarvis", level: int = logging.INFO, log_file: Optional[Path] = None
) -> logging.Logger:
    """Setup and return a logger instance."""
    logger = logging.getLogger(name)

    # Clear any existing handlers
    if logger.hasHandlers():
        logger.handlers.clear()

    logger.setLevel(level)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler if log_file is specified
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
