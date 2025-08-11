from fastapi import FastAPI, File, UploadFile, Form
from typing import List, Optional
from fastapi import APIRouter
from app.schemas.uploadDTO import FileUploadDTO
from app.services import upload_services

router = APIRouter(prefix="/upload", tags=["Upload"])

@router.post("")
async def upload_multiple_files(
    files: List[UploadFile] = File(...),
    tags: Optional[str] = Form(None)  # Optional tags as form field
):
   print(f"Files: {files}")
   print(f"Tags: {tags}")
   return await upload_services.uploads_file(files, tags)