from fastapi import FastAPI, File, UploadFile, Form, Depends
from typing import List, Optional
from fastapi import APIRouter
from app.schemas.uploadDTO import FileUploadDTO
from app.services import upload_services
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter(prefix="/upload", tags=["Upload"])

@router.post("")
async def upload_multiple_files(
    files: List[UploadFile] = File(...),
    tags: Optional[str] = Form(None),  # Optional tags as form field
    db: Session = Depends(get_db),
):
    print(f"Files: {files}")
    print(f"Tags: {tags}")
    return await upload_services.uploads_file(files, tags, db)