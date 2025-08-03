from typing import Union

from fastapi import FastAPI
from app.routers.v1.router import router as api_v1_router

app = FastAPI()
app.include_router(api_v1_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}