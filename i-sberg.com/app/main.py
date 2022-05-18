from collections import Counter

from fastapi import FastAPI

from app.db import database
from app.redis import redis
from app.models import AnagramQuery, AnagramResponse


app = FastAPI(title='i-sberg.com')


@app.on_event("startup")
async def startup():
    await database.connect()
    await redis.initialize()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
    await redis.close()


@app.post("/anagrams/", response_model=AnagramResponse)
async def anagrams(request: AnagramQuery):
    if Counter(request.str_1) == Counter(request.str_2):
        anagrams_count = await redis.incr('anagrams_count')
        return AnagramResponse(is_anagram=True, anagrams_count=anagrams_count)
    else:
        anagrams_count = await redis.get('anagrams_count') or 0
        return AnagramResponse(is_anagram=False, anagrams_count=anagrams_count)


@app.post("/devices/")
async def create_devices():
    pass


@app.get("/devices/")
async def get_devices():
    pass
