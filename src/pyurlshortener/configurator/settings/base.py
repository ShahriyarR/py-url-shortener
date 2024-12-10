"""Add the base settings"""

import os

REDIS_CACHE_DB = os.environ.get("REDIS_CACHE_DB", 0)
REDIS_COUNTER_DB = os.environ.get("REDIS_COUNTER_DB", 1)
REDIS_PORT = os.environ.get("REDIS_PORT", 6379)
REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", "")
