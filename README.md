# 🧘‍♀️ Fitness Studio Booking API

A simple booking API built using **FastAPI** for a fictional fitness studio offering classes like Yoga, Zumba, and HIIT. Clients can view classes, book a spot, and check their bookings.

---

## 🚀 Features

- View upcoming fitness classes
- Book a class with available slots
- Get bookings by email
- Timezone-aware (IST to UTC handling)
- SQLite (file-based or in-memory)
- Clean, modular codebase using FastAPI + SQLModel
- Logging, input validation, and error handling

---

## 📂 Project Structure

```
fitness_booking/
├── app/
│   ├── main.py              # FastAPI app instance
│   ├── models.py            # SQLModel ORM models
│   ├── schemas.py           # Pydantic request/response models
│   ├── crud.py              # Database logic
│   ├── routes/api.py        # API routes
│   ├── database.py          # DB init & seed
│   ├── utils.py             # Timezone conversion
│   └── tests/test_api.py    # Testcases
├── Dockerfile               # Docker setup
├── requirements.txt         # Python dependencies
├── README.md                # You're reading it!
└── .postman_collection.json  # Postman collection
```

---

## 🛠️ Tech Stack

- **FastAPI** – modern Python web framework
- **SQLModel** – ORM powered by SQLAlchemy and Pydantic
- **SQLite** – lightweight, easy-to-use DB
- **Uvicorn + Gunicorn** – production ASGI server
- **Pydantic** – input/output validation

---

## 🧪 Setup Instructions

### 📦 1. Clone & Install Dependencies

```bash
git clone https://github.com/akashkumar19/fitnessbooking.git
cd fitness-booking
pip install -r requirements.txt
```

### 🗃️ 2. Run the API

```bash
uvicorn app.main:app --reload
```

Visit: [http://localhost:8000/docs](http://localhost:8000/docs) for Swagger UI.

---

## 🐳 Docker Setup

Build and run with Docker:

```bash
docker build -t fitness-api .
docker run -p 8000:8000 fitness-api
```

---

## 🔗 API Endpoints

### 🔍 GET /classes

**Description**: Get all upcoming fitness classes.

**Request**:
```http
GET /classes
```

**Response**:
```json
[
  {
    "id": 1,
    "name": "Yoga",
    "instructor": "Ravi",
    "date_time": "2025-06-18T02:30:00Z",
    "available_slots": 10
  }
]
```

---

### ✅ POST /book

**Description**: Book a fitness class.

**Request**:
```json
{
  "class_id": 1,
  "client_name": "Alice",
  "client_email": "alice@example.com"
}
```

**Response**:
```json
{
  "id": 3,
  "class_id": 1,
  "client_name": "Alice",
  "client_email": "alice@example.com"
}
```

---

### 📥 GET /bookings?email={email}

**Description**: Get bookings by email.

**Example**:
```http
GET /bookings?email=alice@example.com
```

---

## 📫 Sample cURL Requests

### Get Classes
```bash
curl http://localhost:8000/classes
```

### Book a Class
```bash
curl -X POST http://localhost:8000/book \
-H "Content-Type: application/json" \
-d '{"class_id": 1, "client_name": "Alice", "client_email": "alice@example.com"}'
```

### Get Bookings
```bash
curl http://localhost:8000/bookings?email=alice@example.com
```

---

## 🕓 Timezone Management

- All class times are stored in **UTC**
- Original creation is based in **IST (Asia/Kolkata)**
- Times will automatically adjust based on the timezone logic if you extend for clients in other regions.

---

## ✅ Validation & Error Handling

- Input validation using Pydantic (`EmailStr`, required fields)
- Overbooking prevention
- Class not found errors
- Detached SQLAlchemy session fix via `session.refresh`

---

## 🧪 Testing


```bash
python -m venv .venv
pip install -r requirements.txt
pytest app/tests/
```

---

## 📁 Postman Collection

Import the file below into Postman to test endpoints:

- `.postman_collection.json`

---

## 📹 Loom Walkthrough

> [Loom](https://www.loom.com/share/bafab55c108e4fb7abb5fb676c77f562?sid=f7f29a90-b917-4db7-bd40-5eca7240f824)


---
