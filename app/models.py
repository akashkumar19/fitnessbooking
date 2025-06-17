from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class FitnessClass(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    instructor: str
    date_time: datetime  # stored in UTC
    available_slots: int

class Booking(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    class_id: int = Field(foreign_key="fitnessclass.id")
    client_name: str
    client_email: str
