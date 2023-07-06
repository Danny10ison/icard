"""Module contains base model for driver"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.db import Base


class Driver(Base):
    """Table format for the User entity.

    Attributes:
        __tablename__: the users table name\n
        id: driver id column\n
        name: driver name column\n
        phone_number: driver phone number column\n
        account: defines relationship to driver account table
    """

    __tablename__ = "drivers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    phone_number = Column(String(255), nullable=False, unique=True)

    # Define the relationship to the Account model
    account = relationship("Account", back_populates="driver")
