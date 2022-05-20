from collections import Counter
import secrets

from fastapi import FastAPI
from fastapi import status
import random

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


@app.post("/devices/", status_code=status.HTTP_201_CREATED)
async def create_devices():
    dev_type_list = ['emeter', 'zigbee', 'lora', 'gsm']
    dev_list = []
    dev_id_list = []

    for dev in range(10):
        dev_type = random.choice(dev_type_list)
        dev_id = secrets.token_hex(6)
        dev_list.append({'dev_id': dev_id, 'dev_type': dev_type})
        dev_id_list.append(dev_id)

    async with database.transaction():
        query = 'INSERT INTO devices (dev_id, dev_type) VALUES (:dev_id, :dev_type)'
        await database.execute_many(query, dev_list)

        dev_id_rand = random.sample(dev_id_list, 5)
        dev_id_query = 'SELECT id FROM devices WHERE dev_id = ANY (:dev_ids)'
        dev_id_db = await database.fetch_all(dev_id_query, {'dev_ids': dev_id_rand})

        endpoint_list = [{'device_id': dev.id, 'comment': 'I was born!'} for dev in dev_id_db]
        query = 'INSERT INTO  endpoints (device_id, comment) VALUES (:device_id, :comment)'
        await database.execute_many(query, endpoint_list)


@app.get("/devices/")
async def get_devices():
    devices_query = '''
        SELECT dev_type, count(*) as dev_count FROM devices 
        LEFT JOIN endpoints ON devices.id = endpoints.device_id
        WHERE endpoints.id IS NULL
        GROUP BY dev_type
        '''

    result = await database.fetch_all(devices_query)
    return {i.dev_type: i.dev_count for i in result}

