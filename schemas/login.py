from pydantic import BaseModel, validator


class LoginParam(BaseModel):
    """serialize Login body"""
    national_code: str
    mobile_number: str
    captcha: str

    @validator('national_code')
    def n_not_null(cls, value):
        if value is None:
            raise ValueError("کد ملی الزامی است")
        return value

    @validator('mobile_number')
    def m_not_null(cls, value):
        if value is None:
            raise ValueError("شماره موبایل الزامی است")
        return value

    @validator('captcha')
    def c_not_null(cls, value):
        if value is None:
            raise ValueError("کد امنیتی الزامی است")
        return value
