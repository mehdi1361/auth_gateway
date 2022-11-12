from pydantic import BaseModel


class VerifyParam(BaseModel):
    """serialize Verifiy body"""
    national_code: str
    verification_code: str
