import json
from typing import Any, Optional

import redis

from pyurlshortener.configurator.settings.base import REDIS_DB, REDIS_HOST, REDIS_PORT
from src.pyurlshortener.configurator.settings.base import REDIS_PASSWORD


class RedisCache:
    def __init__(
        self,
        host: str = REDIS_HOST,
        port: int = REDIS_PORT,
        db: int = REDIS_DB,
        password: Optional[str] = REDIS_PASSWORD,
    ):
        self.client = redis.StrictRedis(host=host, port=port, db=db, password=password, decode_responses=True)

    @classmethod
    def create(cls):
        return cls(REDIS_HOST, REDIS_PORT, REDIS_DB, REDIS_PASSWORD)

    def set(self, key: str, value: Any, expire: Optional[int] = None) -> bool:
        """
        Set a value in the cache with an optional expiration time.

        :param key: The key under which the value will be stored.
        :param value: The value to store in the cache. It must be JSON serializable.
        :param expire: Expiration time in seconds, if any.
        :return: True if the operation was successful, False otherwise.
        """
        try:
            json_value = json.dumps(value)
            self.client.set(key, json_value, ex=expire)
            return True
        except Exception as e:
            print(f"Error setting value in Redis: {e}")
            return False

    def get(self, key: str) -> Optional[Any]:
        """
        Retrieve a value from the cache.

        :param key: The key of the value to retrieve.
        :return: The value if found, None otherwise.
        """
        try:
            json_value = self.client.get(key)
            if json_value is not None:
                return json.loads(json_value)
            return None
        except Exception as e:
            print(f"Error getting value from Redis: {e}")
            return None

    def delete(self, key: str) -> bool:
        """
        Delete a value from the cache.

        :param key: The key of the value to delete.
        :return: True if the operation was successful, False otherwise.
        """
        try:
            self.client.delete(key)
            return True
        except Exception as e:
            print(f"Error deleting value from Redis: {e}")
            return False

    def clear(self) -> bool:
        """
        Clear all values from the cache.

        :return: True if the operation was successful, False otherwise.
        """
        try:
            self.client.flushdb()
            return True
        except Exception as e:
            print(f"Error clearing Redis cache: {e}")
            return False


# Example usage:
# cache = RedisCache()
# cache.set('key', {'example': 'value'}, expire=60)
# value = cache.get('key')
# cache.delete('key')
# cache.clear()
