from pydantic import HttpUrl

from pyurlshortener.domain.models import Url, url_factory
from pyurlshortener.service.counter import ThreadUnsafeCounter
from pyurlshortener.service.encoder import encode


def shortened(original_url: str, created_by: str, counter: ThreadUnsafeCounter) -> tuple[Url, str]:
    counter.increment()
    val = counter.value()
    encoded = encode(val)
    encoded_url = f"https://short.url/{encoded}"
    return (
        url_factory(short_url=HttpUrl(encoded_url), original_url=HttpUrl(original_url), created_by=created_by),
        encoded,
    )
