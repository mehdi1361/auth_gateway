import redis
from core.config import settings

class RedisClient:
    @staticmethod
    def set_token(token, national_code):
        r = redis.Redis(
            host=settings.REDIS_SERVER_URL,
            port=settings.REDIS_SERVER_PORT,
        )
        r.set(token, national_code)
        r.expire(token, 60*20)
        return True

    @staticmethod
    def get_token(token):
        r = redis.Redis(
            host=settings.REDIS_SERVER_URL,
            port=settings.REDIS_SERVER_PORT,
        )
        return r.get(token)

    @staticmethod
    def check_token(national_code):
        r = redis.Redis(
            host=settings.REDIS_SERVER_URL,
            port=settings.REDIS_SERVER_PORT,
        )

        for key in r.scan_iter():
            if r.get(key) == RedisClient.get_token(key):
                return True, key

        else:
            return False, None

    @staticmethod
    def delete_token_with_national_code(national_code):
        r = redis.Redis(
            host=settings.REDIS_SERVER_URL,
            port=settings.REDIS_SERVER_PORT,
        )

        for key in r.scan_iter():
            if r.get(key) == RedisClient.get_token(key):
                r.delete(key)
