from app.schemas.user import UserCreate
from app.models.user import User
from app.database.db import SessionLocal


# User Signup
def user_signup(user_data: UserCreate):
    with SessionLocal() as session:
        existing_user = session.query(
            User).filter_by(phone_number=user_data.phone_number).first()
        if existing_user:
            raise ValueError(
                "User with the provided phone number already exists.")

        user = User(**user_data.dict())
        session.add(user)
        session.commit()
        session.refresh(user)

        return user.id


# User Login
def user_login(phone_number: str):
    with SessionLocal() as session:
        user = session.query(User).filter_by(phone_number=phone_number).first()
        if user is None:
            raise Exception("User not found")
        return user.id


# Update User Email and Name
def update_user(user_id: int, email: str, name: str):
    with SessionLocal() as session:
        user = session.query(User).get(user_id)
        if user:
            user.email = email
            user.name = name
            session.commit()
        else:
            raise ValueError("User not found.")


# Get User Details
def get_user_details(user_id: int):
    with SessionLocal() as session:
        user = session.query(User).get(user_id)
        if user:
            return user
        else:
            raise ValueError("User not found.")


# Get All Users
def get_all_users():
    with SessionLocal() as session:
        users = session.query(User).all()
        return users


# Delete User
def delete_user(user_id: int):
    with SessionLocal() as session:
        user = session.query(User).get(user_id)
        if user:
            deleted_user_id = user.id
            session.delete(user)
            session.commit()
            return deleted_user_id
        else:
            raise ValueError("User not found.")


# Get User by Phone Number
def get_user_by_phone_number(phone_number: str):
    with SessionLocal() as session:
        user = session.query(User).filter_by(phone_number=phone_number).first()
        if user:
            return user.phone_number
        else:
            return None
