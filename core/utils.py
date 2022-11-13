
import jwt
from .config import settings

class AuthJWT:
    @staticmethod
    def generate(national_code):
        encoded_jwt = jwt.encode(
            {"data": national_code},
            settings.JWT_SECRET_KEY,
            algorithm="HS256"
        )
        return encoded_jwt

    @staticmethod
    def decode(token):
        result = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=["HS256"])
        if result is not None:
            return result["data"]

        return None
