import grpc
from fastapi import APIRouter, Body, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from schemas import LoginParam
from service.client.customer import CustomerClient

router = APIRouter()

@router.post("/login/")
async def login_request(param: LoginParam):
    try:
        result = CustomerClient.login_by_national_code(param.national_code)
        return JSONResponse(
            content={"id": result.id, "message": result.message},
            status_code=status.HTTP_200_OK
        )

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
