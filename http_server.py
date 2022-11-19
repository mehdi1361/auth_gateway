#!/usr/bin/env python3

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from api.v1.api import api_router
from core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    config = uvicorn.Config(
        "http_server:app",
        host=settings.SERVER,
        port=settings.PORT,
        log_level="info",
        reload=True
    )
    server = uvicorn.Server(config)
    server.run()
