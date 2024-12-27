from datetime import datetime, timedelta
from xml.dom import ValidationErr

import pytest
from pydantic import ValidationError

from pyurlshortener.domain.models import Url, url_factory


def test_url_creation():
    short_url = "http://short.url/abc123"
    original_url = "http://original.url/longurl"
    created_by = "user123"

    # Create a Url instance
    url = Url(short_url=short_url, original_url=original_url, created_by=created_by)

    # Assertions
    assert str(url.short_url) == short_url
    assert str(url.original_url) == original_url
    assert url.created_by == created_by


def test_url_factory():
    short_url = "http://short.url/xyz789"
    original_url = "http://original.url/somelongurl"
    created_by = "user456"

    # Use the factory to create a Url instance
    url = url_factory(short_url, original_url, created_by)
    # Assertions
    assert str(url.short_url) == short_url
    assert str(url.original_url) == original_url
    assert url.created_by == created_by


def test_url_factory_with_wrong_type():
    short_url = "google.com"
    original_url = "http://original.url/somelongurl"
    created_by = "user456"

    # Use the factory to create a Url instance
    with pytest.raises(ValidationError):
        url_factory(short_url, original_url, created_by)
