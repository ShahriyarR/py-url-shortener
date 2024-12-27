import pytest

from pyurlshortener.service.counter import ThreadUnsafeCounter


@pytest.fixture(scope="session")
def global_counter():
    return ThreadUnsafeCounter()
