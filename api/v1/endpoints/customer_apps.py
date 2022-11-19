from fastapi import APIRouter, Body, Depends, HTTPException, Header
from typing import List, Union

from schemas import LoginParam
from service.client.customer import CustomerClient
from service.redis import RedisClient

router = APIRouter()

@router.get("/apps/")
async def customer_apps(token: Union[List[str], None] = Header(default=None)):
    national_code = RedisClient.get_token(token[0])
    if national_code is None:
       return {
           "id": 400,
           "message": "شما مجوز دسترسی به سامانه را ندارید لطفا مجدد تلاش کنید"
       }
    result = CustomerClient.customer_apps(national_code)
    return result
