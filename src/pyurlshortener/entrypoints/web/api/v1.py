from pydantic import HttpUrl
from sanic import Blueprint, redirect
from sanic.response import json

from pyurlshortener.service.url import shortened

bp = Blueprint("URLShortener", version=1, url_prefix="/api")


@bp.route("/url", methods=["POST"])
async def get_original_url(request):
    original_url = request.json.get("original_url")
    created_by = request.json.get("created_by")
    shortened_, shortened_id = shortened(original_url, created_by, request.app.ctx.counter)
    request.app.ctx.shared_data[f"{shortened_id}"] = HttpUrl(original_url)
    return json({"short_url": f"{shortened_.short_url}"})


@bp.route("/url/<shortened_id>", methods=["GET"])
async def get_shortened_url(request, shortened_id):
    original_url = request.app.ctx.shared_data[f"{shortened_id}"]
    return redirect(to=str(original_url), status=302)
