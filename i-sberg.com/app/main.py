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
