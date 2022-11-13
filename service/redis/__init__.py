import redis
from core.config import settings

class RedisClient:
    @staticmethod
    def set_token(token, national_code):
        r = redis.Redis(
            host=settings.REDIS_SERVER_URL,
            port=settings.REDIS_SERVER_PORT,
            db=settings.REDIS_SERVER_DATABASE
        )
        r.set(token, national_code)
        r.expire(token, 60*20)
        return True

    @staticmethod
    def get_token(token):
        pass

    @staticmethod
    def check_token(national_code):
        pass
