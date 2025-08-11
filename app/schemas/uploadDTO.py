from fastapi import UploadFile
from fastapi.params import File
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


class FileUploadDTO(BaseModel):
    tags: Optional[List[str]] = None