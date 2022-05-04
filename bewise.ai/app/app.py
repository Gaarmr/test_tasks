from fastapi import FastAPI
from ..database.models import Questions


from database import database
from models import UserCreate


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/users", response_model=list[Questions])
async def get_users():
    query = "SELECT id, email FROM users"
    users = await database.fetch_all(query)
    return users


@app.post("/users", response_model=Questions)
async def create_user(user_create: UserCreate):
    query = "INSERT INTO users (email) VALUES (:email) RETURNING id, email"
    user = await database.fetch_one(query, {"email": user_create.email})
    return user
