from fastapi import APIRouter, Query
from app import crud
from app.schemas import BookingRequest, FitnessClassOut, BookingOut
from app.utils import to_timezone

router = APIRouter()

@router.get("/classes", response_model=list[FitnessClassOut])
def get_classes():
    classes = crud.get_classes()
    return [c for c in classes]

@router.post("/book", response_model=BookingOut)
def book_class(request: BookingRequest):
    return crud.create_booking(request)

@router.get("/bookings", response_model=list[BookingOut])
def bookings(email: str = Query(...)):
    return crud.get_bookings_by_email(email)
