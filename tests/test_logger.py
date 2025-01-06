"""Tests for the logger utility."""
import logging
from pathlib import Path
import pytest  # pylint: disable=unused-import
from src.utils.logger import setup_logger


def test_logger_basic_setup():
    """Test basic logger setup without file handler."""
    logger = setup_logger("test_logger")
    assert logger.name == "test_logger"
    assert logger.level == logging.INFO
    assert len(logger.handlers) == 1
    assert isinstance(logger.handlers[0], logging.StreamHandler)


def test_logger_with_file(tmp_path):
    """Test logger setup with file handler."""
    log_file = tmp_path / "test.log"
    logger = setup_logger("test_logger", log_file=Path(log_file))
    assert len(logger.handlers) == 2
    assert isinstance(logger.handlers[1], logging.FileHandler)

    # Test logging to file
    test_message = "Test log message"
    logger.info(test_message)

    # Verify message was written to file
    with open(log_file, encoding="utf-8") as f:
        log_content = f.read()
        assert test_message in log_content


def test_logger_different_levels():
    """Test logger with different log levels."""
    logger = setup_logger("test_logger", level=logging.DEBUG)
    assert logger.level == logging.DEBUG
