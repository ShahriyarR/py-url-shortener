from pydantic import HttpUrl

from pyurlshortener.service.url import shortened


def test_shortened(global_counter):
    original_url = "https://google.com"
    created_by = "Shako"
    data, shortened_id = shortened(original_url, created_by, global_counter)
    assert data.original_url == HttpUrl(original_url)
    assert data.created_by == created_by
    assert data.short_url == HttpUrl("https://short.url/g9")
