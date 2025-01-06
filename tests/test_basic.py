"""Basic tests for the logger utility."""
import pytest  # pylint: disable=unused-import
from src.utils.logger import setup_logger


def test_logger_setup():
    """Test basic logger setup functionality."""
    logger = setup_logger("test")
    assert logger.name == "test"
    assert logger.level == 20  # INFO level
