from pydantic import BaseModel


class VerifiyResponse(BaseModel):
    """serialize Login body"""
    national_code: str
