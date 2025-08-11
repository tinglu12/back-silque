from importlib.resources import files
import os
from typing import List, Optional
from fastapi import UploadFile
from app.schemas.uploadDTO import FileUploadDTO
import uuid
from app.database import get_s3, get_db
from app.models.Clothe import Clothe



async def uploads_file(files: List[UploadFile], tags: Optional[str] = None):
    uploaded_filenames = []
    s3 = get_s3()

    db = next(get_db())
    for file in files:
        # You can process each file here, e.g., save it to disk
        contents = await file.read()
        # Example: Save the file
        file_extension = file.filename.split(".")[-1]
        filename = f"{file.filename}-{uuid.uuid4()}.{file_extension}"
        s3.put_object(
            Bucket=os.getenv("S3_BUCKET_NAME"),
            Key=f"{filename}",
            Body=contents
        )
        clothes = Clothe(image_url=filename)
        db.add(clothes)
        db.commit()

        uploaded_filenames.append(filename)
    
    # Handle tags if provided
    tags_info = f" with tags: {tags}" if tags else ""
    
    return {
        "message": f"File uploaded successfully{tags_info}",
        "uploaded_files": uploaded_filenames,
        "tags": tags
    }