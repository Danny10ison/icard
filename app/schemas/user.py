from pydantic import BaseModel, Field


class UserBase(BaseModel):

    name: str
    email: str
    phone_number: str


class UserCreate(UserBase):

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "johndoe@example.com",
                "phone_number": "1234567890"
            }
        }


class UserUpdate(BaseModel):
    name: str = None
    email: str = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "johndoe@example.com"
            }
        }


class UserLogin(BaseModel):
    # Adding regex validation for phone_number
    phone_number: str = Field(..., regex=r"^\d{10}$")

    class Config:
        schema_extra = {
            "example": {
                "phone_number": "1234567890"
            }
        }


class UserDelete(BaseModel):
    user_id: int

    class Config:
        schema_extra = {
            "example": {
                "user_id": 123
            }
        }
