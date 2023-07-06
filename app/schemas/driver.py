from pydantic import BaseModel, Field


class DriverBase(BaseModel):
    name: str
    email: str
    phone_number: str


class DriverCreate(DriverBase):
    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "johndoe@example.com",
                "phone_number": "1234567890"
            }
        }


class DriverLogin(BaseModel):
    # Adding regex validation for phone_number
    phone_number: str = Field(..., regex=r"^\d{10}$")

    class Config:
        schema_extra = {
            "example": {
                "phone_number": "1234567890"
            }
        }


class DriverUpdate(BaseModel):
    name: str = None
    email: str = None

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "johndoe@example.com"
            }
        }


class DriverDelete(BaseModel):
    driver_id: int

    class Config:
        schema_extra = {
            "example": {
                "driver_id": 123
            }
        }
