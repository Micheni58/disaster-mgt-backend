# server/app/main.py
from fastapi import FastAPI
from app.core.database import engine, Base
from app.models.User import User
# Import your user API router
from app.resources.user_resource import router as user_router

app = FastAPI(title="Disaster Management API")

# Create database tables
Base.metadata.create_all(bind=engine)

app.include_router(user_router)

@app.get("/")
def index():
    return {"message": "Welcome to the crisis management API!!"}