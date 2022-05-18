import aioredis
from fastapi import FastAPI


app = FastAPI(title='i-sberg.com')


@app.on_event("startup")
async def startup():
    pass


@app.on_event("shutdown")
async def shutdown():
    pass


@app.post("/anagrams/")
async def anagrams():
    pass


@app.post("/devices/")
async def anagrams(devices_count: int):
    pass


@app.get("/get_devices_list/")
async def anagrams(devices_count: int):
    pass
