import aioredis

from app.settings import REDIS_KEY_EXPIRE_SECONDS, REDIS_URL


class RedisMachine:
    async def __aenter__(self):
        self.redis = await aioredis.create_redis(REDIS_URL)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.redis.close()
        await self.redis.wait_closed()

    async def get(self, key):
        return await self.redis.get(key)

    async def set(self, key, value, expire=REDIS_KEY_EXPIRE_SECONDS):
        return await self.redis.set(key, value, expire=expire)
