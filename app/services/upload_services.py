from importlib.resources import files
import os
from typing import List, Optional
from fastapi import UploadFile
from sqlalchemy.orm import Session
from app.schemas.uploadDTO import FileUploadDTO
import uuid
from app.database import get_s3
from app.models.Clothe import Clothe



async def uploads_file(files: List[UploadFile], tags: Optional[str] = None, db: Session | None = None):
    if db is None:
        raise ValueError("Database session is required")

    uploaded_filenames: List[str] = []
    s3 = get_s3()

    for file in files:
        contents = await file.read()
        file_extension = file.filename.split(".")[-1]
        filename = f"{file.filename}-{uuid.uuid4()}.{file_extension}"
        s3.put_object(
            Bucket=os.getenv("S3_BUCKET_NAME"),
            Key=f"{filename}",
            Body=contents,
        )
        clothes = Clothe(image_url=filename)
        db.add(clothes)

        uploaded_filenames.append(filename)

    # Commit once after processing all files
    db.commit()
    
    # Handle tags if provided
    tags_info = f" with tags: {tags}" if tags else ""
    
    return {
        "message": f"File uploaded successfully{tags_info}",
        "uploaded_files": uploaded_filenames,
        "tags": tags
    }