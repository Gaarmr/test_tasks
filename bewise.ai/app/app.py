from fastapi import FastAPI

app = FastAPI(title="FastAPI, Questions")


@app.get("/")
def read_root():
    return {"hello": "world"}