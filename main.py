from typing import Union

from fastapi import FastAPI
from app import models
from app import database
from app.models.User import User
from app.routers.v1.router import router as api_v1_router
from app.database import engine, Base

app = FastAPI()
app.include_router(api_v1_router, prefix="/api/v1")

database.Base.metadata.drop_all(bind=engine)
database.Base.metadata.create_all(bind=engine)



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}