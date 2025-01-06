import pytest

# Set default event loop policy
pytest_plugins = ["pytest_asyncio"]


@pytest.fixture(scope="function")
def event_loop():
    """Create an instance of the default event loop for each test function."""
    import asyncio

    loop = asyncio.new_event_loop()
    yield loop
    loop.close()
