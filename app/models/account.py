from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.database.db import Base

class Account(Base):
    """Table format for the Account entity."""

    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    account_number = Column(String(12), nullable=False, unique=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    driver_id = Column(Integer, ForeignKey("drivers.id"))
    balance = Column(Float, nullable=False)

    # Define the relationship to the User model
    user = relationship("User", back_populates="account", uselist=False)

    # Define the relationship to the Driver model
    driver = relationship("Driver", back_populates="account", uselist=False)

    def __init__(self, account_number: str, balance=0, user=None, driver=None):
        self.account_number = account_number
        self.balance = balance
        self.user = user
        self.driver = driver
