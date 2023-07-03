from fastapi import FastAPI, HTTPException
from fastapi.openapi.utils import get_openapi

from app.database.db import Base, engine

from app.schemas.user import UserCreate, UserUpdate
from app.schemas.driver import DriverCreate, DriverUpdate
from app.schemas.account import AccountCreate, AccountBase
from app.database.crud.crud_account import create_account, get_account_by_user_or_driver_id, delete_account_by_user_or_driver_id, withdraw_from_account, top_up_account


from app.database.crud import crud_user, crud_account, crud_driver

app = FastAPI(
    title="iCard",
    description="inDrive's virtual payment system",
    version="1.0.0"
    )

# Customizing the Swagger UI
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )
    # Modify the OpenAPI schema as needed
    openapi_schema["info"]["x-logo"] = {
        "url": "https://indrive.com/favicon.svg",
        "altText": "inDrve Logo",
    }
    openapi_schema["info"]["contact"] = {
        "name": "Daniel Osei",
        "email": "pagesngod@gmail.com",
    }
    openapi_schema["info"]["license"] = {
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    }
    return openapi_schema

app.openapi = custom_openapi

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {
        "api": "iCard - Virtual payment card for inDrive",
        "version": "v1.0.0",
        "year": "2023"
        }

###############################################################################
# Users
###############################################################################

@app.get("/users")
def get_all_users():
    try:
        users = crud_user.get_all_users()
        return {"users": users}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/users/{user_id}")
def get_user_details(user_id: int):
    try:
        user = crud_user.get_user_details(user_id)
        if user:
            return {"user": user}
        else:
            raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/users/signup")
def register_user(user: UserCreate):
    try:
        user_id = crud_user.user_signup(user)
        return {"message": "User created successfully", "user_id": user_id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/users/login")
def user_login(phone_number: str):
    try:
        user_id = crud_user.user_login(phone_number)
        if user_id:
            return {"message": "User login successful", "user_id": user_id}
        else:
            raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: UserUpdate):
    try:
        crud_user.update_user(user_id, updated_user.email, updated_user.name)
        return {"message": "User updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    try:
        result = crud_user.delete_user(user_id)
        if result:
            return {"message": "User deleted successfully", "user_id": user_id}
        else:
            raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

###############################################################################
# Drivers
###############################################################################

@app.get("/drivers")
def get_all_drivers():
    try:
        drivers = crud_driver.get_all_drivers()
        return {"drivers": drivers}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/drivers/{driver_id}")
def get_driver_details(driver_id: int):
    try:
        driver = crud_driver.get_driver_details(driver_id)
        if driver:
            return {"driver": driver}
        else:
            raise HTTPException(status_code=404, detail="Driver not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/drivers")
def create_driver(driver: DriverCreate):
    try:
        driver_id = crud_driver.create_driver(driver)
        return {"message": "Driver created successfully", "driver_id": driver_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/drivers/{driver_id}")
def update_driver(driver_id: int, updated_driver: DriverUpdate):
    try:
        crud_driver.update_driver(driver_id, updated_driver)
        return {"message": "Driver updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/drivers/{driver_id}")
def delete_driver(driver_id: int):
    try:
        result = crud_driver.delete_driver(driver_id)
        if result:
            return {"message": "Driver deleted successfully", "driver_id": driver_id}
        else:
            raise HTTPException(status_code=404, detail="Driver not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


#########################################################
# account
#########################################################

@app.post("/accounts/create")
def create_account(account_data: AccountCreate, user_id: int = None, driver_id: int = None):
    try:
        account_number = create_account(account_data, user_id=user_id, driver_id=driver_id)
        return {"account_number": account_number}
    except ValueError as e:
        return {"error": str(e)}

@app.get("/accounts/details")
def get_account_details(user_id: int = None, driver_id: int = None):
    try:
        account = get_account_by_user_or_driver_id(user_id=user_id, driver_id=driver_id)
        return {"account": AccountBase.from_orm(account)}
    except ValueError as e:
        return {"error": str(e)}

@app.delete("/accounts")
def delete_account(user_id: int = None, driver_id: int = None):
    try:
        account_number = delete_account_by_user_or_driver_id(user_id=user_id, driver_id=driver_id)
        return {"account_number": account_number}
    except ValueError as e:
        return {"error": str(e)}

@app.post("/accounts/withdraw")
def withdraw_from_account(amount: float, user_id: int = None, driver_id: int = None):
    try:
        balance = withdraw_from_account(amount, user_id=user_id, driver_id=driver_id)
        return {"balance": balance}
    except ValueError as e:
        return {"error": str(e)}

@app.post("/accounts/top-up")
def top_up_account(amount: float, user_id: int = None, driver_id: int = None):
    try:
        balance = top_up_account(amount, user_id=user_id, driver_id=driver_id)
        return {"balance": balance}
    except ValueError as e:
        return {"error": str(e)}
