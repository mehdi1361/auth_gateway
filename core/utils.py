import jwt
from .config import settings
from random import randint

class AuthJWT:
    @staticmethod
    def generate(national_code):
        encoded_jwt = jwt.encode(
            {"data": national_code},
            f"{settings.JWT_SECRET_KEY}{randint(11111, 99999)}",
            algorithm="HS256"
        )
        return encoded_jwt

    @staticmethod
    def decode(token):
        result = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=["HS256"])
        if result is not None:
            return result["data"]

        return None
