import grpc
from fastapi import APIRouter, Body, Depends, HTTPException
from schemas import LoginParam
from service.client.customer import CustomerClient

router = APIRouter()

@router.post("/login/")
async def login_request(param: LoginParam):
    try:
        result = CustomerClient.login_by_national_code(param.national_code)
        return {"id": result.id, "message": result.message}

    except grpc.RpcError as e:
        if e.code() == grpc.StatusCode.NOT_FOUND:
            return {"id": 400, "message": "کاربر یافت نشد"}
