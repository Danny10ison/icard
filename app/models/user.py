"""Module contains base model for user table"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.db import Base


class User(Base):
    """Table format for the User entity.

    Attributes:
        __tablename__: the users table name\n
        id: user id column
        name: user name column
        phone_number: user phone number column
        account: defines relationship to user account table
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    phone_number = Column(String(255), nullable=False, unique=True)

    # Define the relationship to the Account model
    account = relationship("Account", back_populates="user")
