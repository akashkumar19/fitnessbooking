from pydantic import BaseModel, EmailStr
from datetime import datetime

class BookingRequest(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr

class FitnessClassOut(BaseModel):
    id: int
    name: str
    instructor: str
    date_time: datetime
    available_slots: int

class BookingOut(BaseModel):
    id: int
    class_id: int
    client_name: str
    client_email: EmailStr
