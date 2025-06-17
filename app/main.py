from fastapi import FastAPI
from app.routes import api
from app.database import init_db

app = FastAPI(title="Fitness Studio Booking API")

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(api.router)
