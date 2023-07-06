import uuid

from app.database.db import SessionLocal
from app.models.account import Account
from app.schemas.account import AccountCreate
from app.database.db import SessionLocal


def generate_account_number():
    account_number = str(uuid.uuid4().int)[:12]
    return account_number


# Create a new account
def create_account(account_data: AccountCreate,
                   user_id: int = None,
                   driver_id: int = None
                   ):
    with SessionLocal() as session:
        account = Account(
            account_number=generate_account_number(),
            balance=account_data.balance,
            user_id=user_id,
            driver_id=driver_id
        )
        session.add(account)
        session.commit()
        session.refresh(account)
        return account.account_number


# Get an account by user ID or driver ID
def get_account_by_user_or_driver_id(user_id: int = None,
                                     driver_id: int = None
                                     ):
    with SessionLocal() as session:
        if user_id:
            account = session.query(Account).filter_by(user_id=user_id).first()
        elif driver_id:
            account = session.query(
                Account).filter_by(driver_id=driver_id).first()
        else:
            raise ValueError("Invalid user or driver ID provided.")

        if account:
            return account
        else:
            raise ValueError("Account not found.")


# Delete an account by user ID or driver ID
def delete_account_by_user_or_driver_id(user_id: int = None,
                                        driver_id: int = None
                                        ):
    with SessionLocal() as session:
        if user_id:
            account = session.query(Account).filter_by(user_id=user_id).first()
        elif driver_id:
            account = session.query(
                Account).filter_by(driver_id=driver_id).first()
        else:
            raise ValueError("Invalid user or driver ID provided.")

        if account:
            session.delete(account)
            session.commit()
            return account.account_number
        else:
            raise ValueError("Account not found.")


# Withdraw from account balance by user ID or driver ID
def withdraw_from_account(amount: float,
                          user_id: int = None,
                          driver_id: int = None
                          ):
    with SessionLocal() as session:
        if user_id:
            account = session.query(Account).filter_by(user_id=user_id).first()
        elif driver_id:
            account = session.query(
                Account).filter_by(driver_id=driver_id).first()
        else:
            raise ValueError("Invalid user or driver ID provided.")

        if account:
            if account.balance >= amount:
                account.balance -= amount
                session.commit()
                return account.balance
            else:
                raise ValueError("Insufficient balance.")
        else:
            raise ValueError("Account not found.")


# Top up account balance by user ID or driver ID
def top_up_account(amount: float, user_id: int = None, driver_id: int = None):
    with SessionLocal() as session:
        if user_id:
            account = session.query(Account).filter_by(user_id=user_id).first()
        elif driver_id:
            account = session.query(
                Account).filter_by(driver_id=driver_id).first()
        else:
            raise ValueError("Invalid user or driver ID provided.")

        if account:
            account.balance += amount
            session.commit()
            return account.balance
        else:
            raise ValueError("Account not found.")


def pay_driver(user_id: int, driver_id: int, amount: float):
    with SessionLocal() as session:
        # Withdraw the amount from the user's account
        user_account = withdraw_from_account(amount, user_id=user_id)

        # Top up the amount to the driver's account
        driver_account = top_up_account(amount, driver_id=driver_id)

        # Return the updated balances
        return user_account, driver_account
