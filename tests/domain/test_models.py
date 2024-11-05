from datetime import datetime, timedelta

from pyurlshortener.domain.models import Url, url_factory


def test_url_creation():
    short_url = "http://short.url/abc123"
    original_url = "http://original.url/longurl"
    creation_date = datetime.now()
    expiration_date = creation_date + timedelta(days=30)
    created_by = "user123"

    # Create a Url instance
    url = Url(short_url, original_url, creation_date, expiration_date, created_by)

    # Assertions
    assert url.short_url == short_url
    assert url.original_url == original_url
    assert url.creation_date == creation_date
    assert url.expiration_date == expiration_date
    assert url.created_by == created_by


def test_url_factory():
    short_url = "http://short.url/xyz789"
    original_url = "http://original.url/somelongurl"
    creation_date = datetime.now()
    expiration_date = creation_date + timedelta(days=60)
    created_by = "user456"

    # Use the factory to create a Url instance
    url = url_factory(short_url, original_url, creation_date, expiration_date, created_by)

    # Assertions
    assert url.short_url == short_url
    assert url.original_url == original_url
    assert url.creation_date == creation_date
    assert url.expiration_date == expiration_date
    assert url.created_by == created_by
