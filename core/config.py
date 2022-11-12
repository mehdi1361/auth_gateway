import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import (AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn,
                      validator)


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SERVER_NAME: str = None
    SERVER_HOST: AnyHttpUrl = None
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    CUSTOMER_SERVICE_GRPC_SERVER_URL: str = "127.0.0.1"
    CUSTOMER_SERVICE_GRPC_SERVER_PORT: str = "9000"
    CUSTOMER_SERVICE_MAX_RECIEVE_SIZE: str = "20971520"
    CUSTOMER_SERVICE_MAX_SEND_SIZE: str = "20971520"


    PROJECT_NAME: str = "auth_gateway"
    SENTRY_DSN: Optional[HttpUrl] = None


    class Config:
        case_sensitive = True

settings = Settings()