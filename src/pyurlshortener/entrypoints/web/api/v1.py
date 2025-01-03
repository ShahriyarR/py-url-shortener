from sanic import Blueprint, redirect
from sanic.log import logger
from sanic.response import json

from pyurlshortener.service.cache import RedisCache
from pyurlshortener.service.url import shortened

bp = Blueprint("URLShortener", version=1, url_prefix="/api")


@bp.route("/url", methods=["POST"])
async def get_original_url(request, cache: RedisCache):
    original_url = request.json.get("original_url")
    created_by = request.json.get("created_by")
    shortened_, shortened_id = shortened(original_url, created_by, cache)
    cache.set(shortened_id, original_url)
    logger.info(f"Original url cached: {original_url}")
    return json({"short_url": f"{shortened_.short_url}"})


@bp.route("/url/<shortened_id>", methods=["GET"])
async def get_shortened_url(request, shortened_id, cache: RedisCache):
    original_url = cache.get(shortened_id)
    logger.info(f"Original url cache hit: {original_url}")
    return redirect(to=str(original_url), status=302)
