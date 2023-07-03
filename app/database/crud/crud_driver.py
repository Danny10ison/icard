from app.schemas.driver import DriverCreate, DriverUpdate
from app.models.driver import Driver
from app.database.db import SessionLocal

# Create a new driver
def create_driver(driver_data: DriverCreate):
    with SessionLocal() as session:
        driver = Driver(**driver_data.dict())
        session.add(driver)
        session.commit()
        session.refresh(driver)
        return driver.id

# Get a driver by ID
def get_driver_details(driver_id: int):
    with SessionLocal() as session:
        driver = session.query(Driver).get(driver_id)
        if driver:
            return driver
        else:
            raise ValueError("Driver not found.")

# Update driver details
def update_driver(driver_id: int, driver_data: DriverUpdate):
    with SessionLocal() as session:
        driver = session.query(Driver).get(driver_id)
        if driver:
            for field, value in driver_data.dict(exclude_unset=True).items():
                setattr(driver, field, value)
            session.commit()
        else:
            raise ValueError("Driver not found.")

# Delete a driver
def delete_driver(driver_id: int):
    with SessionLocal() as session:
        driver = session.query(Driver).get(driver_id)
        if driver:
            session.delete(driver)
            session.commit()
            return driver.id
        else:
            raise ValueError("Driver not found.")

# Get all drivers
def get_all_drivers():
    with SessionLocal() as session:
        drivers = session.query(Driver).all()
        return drivers
