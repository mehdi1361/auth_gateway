from fastapi import APIRouter, Body, Depends, HTTPException
from schemas import LoginParam
from service.client.customer import CustomerClient

router = APIRouter()

@router.post("/login/")
async def login_request(param: LoginParam):
    result = CustomerClient.login_by_national_code(param.national_code)
    return {"id": result.id, "message": result.message}
