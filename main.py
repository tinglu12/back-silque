from typing import Union

from fastapi import FastAPI
from app import models
from app import database
from app.models.User import User
from app.routers.v1.router import router as api_v1_router
from app.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(api_v1_router, prefix="/api/v1")


origins = [
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}