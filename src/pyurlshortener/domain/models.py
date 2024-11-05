from dataclasses import dataclass
from datetime import datetime


@dataclass
class Url:
    short_url: str
    original_url: str
    creation_date: datetime
    expiration_date: datetime
    created_by: str


def url_factory(
    short_url: str, original_url: str, creation_date: datetime, expiration_date: datetime, created_by: str
) -> Url:
    return Url(short_url, original_url, creation_date, expiration_date, created_by)
