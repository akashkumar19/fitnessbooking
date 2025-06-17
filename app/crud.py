from sqlmodel import Session, select
from app.models import FitnessClass, Booking
from app.schemas import BookingRequest
from app.database import engine
from fastapi import HTTPException

def get_classes():
    with Session(engine) as session:
        return session.exec(select(FitnessClass)).all()

def create_booking(data: BookingRequest):
    with Session(engine) as session:
        fc = session.get(FitnessClass, data.class_id)
        if not fc:
            raise HTTPException(status_code=404, detail="Class not found")
        if fc.available_slots <= 0:
            raise HTTPException(status_code=400, detail="No slots available")

        booking = Booking(**data.dict())
        session.add(booking)
        fc.available_slots -= 1
        session.commit()
        session.refresh(booking)
        return booking

def get_bookings_by_email(email: str):
    with Session(engine) as session:
        return session.exec(select(Booking).where(Booking.client_email == email)).all()
