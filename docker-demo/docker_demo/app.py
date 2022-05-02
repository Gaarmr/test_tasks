from fastapi import FastAPI

from docker_demo.database import database
from docker_demo.models import User
from docker_demo.models import UserCreate


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/users", response_model=list[User])
async def get_users():
    query = "SELECT id, email FROM users"
    users = await database.fetch_all(query)
    return users


@app.post("/users", response_model=User)
async def create_user(user_create: UserCreate):
    query = "INSERT INTO users (email) VALUES (:email) RETURNING id, email"
    user = await database.fetch_one(query, {"email": user_create.email})
    return user
