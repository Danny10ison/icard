from pydantic import BaseModel


class AccountBase(BaseModel):
    account_number: str
    balance: float = 0

    class Config:
        orm_mode = True


class AccountCreate(AccountBase):
    user_id: int = None
    driver_id: int = None


class AccountTopUp(BaseModel):
    balance: float = None


class AccountWithdraw(BaseModel):
    balance: float = None


class AccountDetails(BaseModel):
    account_number: str
    balance: float
    user_id: int = None
    driver_id: int = None


class AccountDelete(BaseModel):
    account_number: str
