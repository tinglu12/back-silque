from fastapi import APIRouter


router = APIRouter(prefix="/upload", tags=["Upload"])

@router.post("")
def upload_file():
    return {"message": "File uploaded successfully"}