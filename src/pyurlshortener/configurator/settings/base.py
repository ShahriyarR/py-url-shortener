"""Add the base settings"""

import os

import sentry_sdk

import pyurlshortener

REDIS_CACHE_DB = os.environ.get("REDIS_CACHE_DB", 0)
REDIS_COUNTER_DB = os.environ.get("REDIS_COUNTER_DB", 1)
REDIS_PORT = os.environ.get("REDIS_PORT", 6379)
REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", "")

SENTRY_DSN = os.environ.get("SENTRY_DSN", "")


def init_sentry():
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        send_default_pii=True,
        max_request_body_size="always",
        release=pyurlshortener.__version__,
        traces_sample_rate=0,
    )
