import secrets
import os
from typing import Any, Dict, List, Optional, Union
from pydantic import (AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn,
                      validator)
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
env_file = os.environ.get('auth_gateway_env')

if env_file is not None:
    dotenv_path = Path(os.path.join(BASE_DIR, env_file))
else:
    dotenv_path = Path(os.path.join(BASE_DIR, '.server.env'))

load_dotenv(dotenv_path=dotenv_path)

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
    CUSTOMER_SERVICE_GRPC_SERVER_URL: str = os.getenv("CUSTOMER_SERVICE_URL")
    CUSTOMER_SERVICE_GRPC_SERVER_PORT: str = os.getenv("CUSTOMER_SERVICE_PORT")
    CUSTOMER_SERVICE_MAX_RECIEVE_SIZE: str = os.getenv("CUSTOMER_SERVICE_MAX_RECIEVE_SIZE")
    CUSTOMER_SERVICE_MAX_SEND_SIZE: str = os.getenv("CUSTOMER_SERVICE_MAX_SEND_SIZE")

    REDIS_SERVER_URL: str = os.getenv("REDIS_SERVER_URL")
    REDIS_SERVER_PORT: str = os.getenv("REDIS_SERVER_PORT")
    REDIS_SERVER_DATABASE: str = os.getenv("REDIS_SERVER_DATABASE")

    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY")
    SERVER: str = os.getenv("SERVER")
    PORT: int = os.getenv("PORT")
    GRPC_PORT: int = os.getenv("GRPC_PORT")

    PROJECT_NAME: str = "auth_gateway"
    SENTRY_DSN: Optional[HttpUrl] = None


    class Config:
        case_sensitive = True

settings = Settings()
