from fastapi import APIRouter, Body, Depends, HTTPException, status, Request, Response
from fastapi.responses import JSONResponse, StreamingResponse
from fast_captcha import img_captcha

router = APIRouter()

@router.get("/captcha/")
async def get_captcha(request: Request):
    import ipdb; ipdb.set_trace()
    img, text = img_captcha()
    import ipdb; ipdb.set_trace()
    request.session["captcha"] = text
    return StreamingResponse(content=img, media_type='image/jpeg')
