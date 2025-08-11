from fastapi import APIRouter
from . import upload


#Routers start with api/v1 in main.py
router = APIRouter()
router.include_router(upload.router)