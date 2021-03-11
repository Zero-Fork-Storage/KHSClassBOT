import aiocache
from aiocache.backends.redis import RedisCache
from aiocache.factory import CacheHandler


class REDIS_CLIENT:
    def __init__(self, host: str, port: int):
        """REDIS Client Core

        :param host: REDIS Server host
        :param port: REDIS Server port
        """
        self.host = host
        self.port = port
        self._caches: CacheHandler = aiocache.caches
        self._caches.set_config(
            {
                "default": {
                    "cache": "aiocache.RedisCache",
                    "endpoint": self.host,
                    "port": self.port,
                    "timeout": 1,
                    "serializer": {"class": "aiocache.serializers.PickleSerializer"},
                    "plugins": [
                        {"class": "aiocache.plugins.HitMissRatioPlugin"},
                        {"class": "aiocache.plugins.TimingPlugin"},
                    ],
                }
            }
        )
        self.cache: RedisCache = self._caches.create(
            **self._caches.get_alias_config("default")
        )
