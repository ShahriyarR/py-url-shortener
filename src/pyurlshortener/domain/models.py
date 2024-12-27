from pydantic import BaseModel, HttpUrl


class Url(BaseModel):
    short_url: HttpUrl
    original_url: HttpUrl
    created_by: str


def url_factory(short_url: HttpUrl, original_url: HttpUrl, created_by: str) -> Url:
    return Url(short_url=short_url, original_url=original_url, created_by=created_by)
