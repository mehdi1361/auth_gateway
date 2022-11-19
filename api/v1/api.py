from fastapi import APIRouter

from api.v1.endpoints import login
from api.v1.endpoints import verify
from api.v1.endpoints import customer_apps

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(verify.router, tags=["verifiy"])
api_router.include_router(customer_apps.router, tags=["apps"])
#api_router.include_router(items.router, prefix="/items", tags=["items"])
