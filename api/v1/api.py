from fastapi import APIRouter

from api.v1.endpoints import login
from api.v1.endpoints import verify

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(verify.router, tags=["verifiy"])
#api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
#api_router.include_router(items.router, prefix="/items", tags=["items"])
