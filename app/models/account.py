from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.database.db import Base


class Account(Base):
    """Table format for the Account entity.

    Attributes:
        __tablename__: the users table name\n
        id: account id column\n
        account_number: driver name column\n
        user_id: driver phone number column\n
        balance: account balance column\n
        driver_id: driver id column\n
        user_id: user id column\n
        user: defines relationship with user\n
        driver: defines relationship with driver
    """

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

    def __init__(self,
                 account_number: str,
                 balance=0,
                 user_id=None,
                 driver_id=None
                 ):
        self.account_number = account_number
        self.balance = balance
        self.user_id = user_id
        self.driver_id = driver_id
