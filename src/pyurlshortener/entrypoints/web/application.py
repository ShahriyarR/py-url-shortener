from sanic import Sanic

from pyurlshortener.entrypoints.web.api.v1 import bp as api_v1_bp
from pyurlshortener.service.counter import ThreadUnsafeCounter


def create_app() -> Sanic:
    app = Sanic("URL-Shortener")
    app.blueprint(api_v1_bp)
    counter = ThreadUnsafeCounter()
    app.ctx.shared_data = {}
    app.ctx.counter = counter
    return app
