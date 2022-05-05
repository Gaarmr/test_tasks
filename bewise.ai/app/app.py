from fastapi import FastAPI
import requests
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
    await Questions.objects.get_or_create(question="Было три козла, сколько?", answer='Три', created_at='Вчера')


@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()


@app.post("/get_question/{question_count}")
async def get_question(question_count: int):
    r = requests.get(url='https://jservice.io/api/random?', params=question_count)
    return await r.text  

    # await Questions.objects.get_or_create(question="Было два козла, сколько?", answer='Два', created_at='Севодня')
    # return await Questions.objects.fields('id')