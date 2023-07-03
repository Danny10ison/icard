#!/usr/bin/python3
"""Module contains base model for database"""
from sqlalchemy import Column, Integer, String, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship

from app.database.db import Base

class User(Base):
    """Table format for the User entity."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    phone_number = Column(String(255), nullable=False, unique=True)

    # Define the relationship to the Account model
    account = relationship("Account", back_populates="user")
