
from fastapi import APIRouter, Body, Depends, HTTPException
from schemas import VerifyParam
from service.client.customer import CustomerClient

router = APIRouter()

@router.post("/verify/")
async def verify_request(param: VerifyParam):
    result = CustomerClient.verified(
        national_code=param.national_code,
        verification_code=param.verification_code
    )
    return {"id": result.id, "message": result.message}
