from fastapi import FastAPI

from app.db import database, Questions


app = FastAPI(title="FastAPI, Docker, and Traefik")


@app.get("/")
async def read_root():
    return await Questions.objects.all()


@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()
    # create a dummy entry
    await Questions.objects.get_or_create(question="Было два козла, сколько?", answer='Два', created_at='Севодня')


@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()


