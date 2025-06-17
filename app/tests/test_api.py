import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, Session
from app.main import app
from app.database import engine
from app.models import FitnessClass
from sqlmodel import select

from datetime import datetime
import pytz

client = TestClient(app)


def create_db_and_seed():
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        if not session.exec(select(FitnessClass)).first():
            ist = pytz.timezone("Asia/Kolkata")
            session.add_all(
                [
                    FitnessClass(
                        name="Yoga",
                        instructor="Ravi",
                        date_time=ist.localize(datetime(2025, 6, 18, 8, 0, 0)),
                        available_slots=10,
                    ),
                    FitnessClass(
                        name="Zumba",
                        instructor="Anjali",
                        date_time=ist.localize(datetime(2025, 6, 18, 10, 0, 0)),
                        available_slots=10,
                    ),
                ]
            )
            session.commit()


@pytest.fixture(autouse=True)
def setup():
    create_db_and_seed()


def test_get_classes():
    response = client.get("/classes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_post_booking_success():
    # This test assumes class_id=1 exists with available slots
    response = client.post(
        "/book", json={"class_id": 1, "client_name": "Test User", "client_email": "testuser@example.com"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["client_name"] == "Test User"
    assert data["client_email"] == "testuser@example.com"
    assert data["class_id"] == 1


def test_post_booking_overbooking():
    # Fill all slots and then test one more booking
    for _ in range(10):  # Assuming the default class has 10 slots
        client.post("/book", json={"class_id": 2, "client_name": "User", "client_email": "user@example.com"})
    # This booking should fail
    response = client.post(
        "/book", json={"class_id": 2, "client_name": "Overbooked User", "client_email": "fail@example.com"}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "No slots available"


def test_get_bookings_by_email():
    email = "testuser@example.com"
    response = client.get(f"/bookings?email={email}")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    for booking in data:
        assert booking["client_email"] == email
