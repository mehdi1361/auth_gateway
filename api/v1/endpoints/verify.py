import grpc
from fastapi import APIRouter, Body, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from schemas import VerifyParam
from service.client.customer import CustomerClient
from core.utils import AuthJWT
from service.redis import RedisClient

router = APIRouter()

@router.post("/verify/")
async def verify_request(param: VerifyParam):

    try:
        result = CustomerClient.verified(
            national_code=param.national_code,
            verification_code=param.verification_code
        )

        if result.id == 200:
            token = AuthJWT.generate(param.national_code)
            RedisClient.delete_token_with_national_code(param.national_code)

            set_to_redis = RedisClient.set_token(
                token=token,
                national_code=param.national_code
            )
            if set_to_redis:
                return {
                    "id": result.id,
                    "message": result.message,
                    "token": token
                }

        return {"id": 400, "message": "خطا در تایید کاربر"}

    except grpc.RpcError as e:
        if e.code() == grpc.StatusCode.NOT_FOUND:
            return JSONResponse(
                content={"id": 400, "message": "کاربر یافت نشد"},
                status_code=status.HTTP_400_BAD_REQUEST
            )

        return JSONResponse(
            content={"id": 400, "message": str(e)},
            status_code=status.HTTP_400_BAD_REQUEST
        )
