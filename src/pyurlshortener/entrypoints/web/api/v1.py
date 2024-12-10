from sanic import Blueprint
from sanic.response import json

from pyurlshortener.service.counter import ThreadUnsafeCounter
from pyurlshortener.service.url import shortened

bp = Blueprint("URLShortener", version=1, url_prefix="/api")


@bp.route("/url", methods=["POST"])
async def get_url(request, counter: ThreadUnsafeCounter):
    original_url = request.json.get("original_url")
    created_by = request.json.get("created_by")
    shortened_ = shortened(original_url, created_by, counter)
    return json({"short_url": f"{shortened_.short_url}"})
