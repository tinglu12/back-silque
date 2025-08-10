from fastapi import APIRouter
from . import upload

router = APIRouter()
router.include_router(upload.router)