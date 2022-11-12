
from fastapi import APIRouter, Body, Depends, HTTPException
from schemas import VerifyParam

router = APIRouter()

@router.post("/verify/")
async def verify_request(param: VerifyParam):
    return param
