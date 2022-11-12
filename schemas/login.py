from pydantic import BaseModel


class LoginParam(BaseModel):
    """serialize Login body"""
    national_code: str
