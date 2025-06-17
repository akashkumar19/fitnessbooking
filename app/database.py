from sqlmodel import Session, SQLModel, create_engine
from app.models import FitnessClass
from datetime import datetime
import pytz

IST = pytz.timezone("Asia/Kolkata")
engine = create_engine("sqlite:///booking.db", echo=False)

def init_db():
    SQLModel.metadata.create_all(engine)
    seed_data()

def seed_data():
    with Session(engine) as session:
        if session.query(FitnessClass).count() == 0:
            classes = [
                FitnessClass(name="Yoga", instructor="Ravi", date_time=IST.localize(datetime(2025, 6, 18, 8, 0)).astimezone(pytz.UTC), available_slots=10),
                FitnessClass(name="Zumba", instructor="Anita", date_time=IST.localize(datetime(2025, 6, 18, 10, 0)).astimezone(pytz.UTC), available_slots=8),
                FitnessClass(name="HIIT", instructor="Raj", date_time=IST.localize(datetime(2025, 6, 19, 9, 0)).astimezone(pytz.UTC), available_slots=5),
            ]
            session.add_all(classes)
            session.commit()
