from typing import Annotated
import uuid

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy import Column, true
from sqlalchemy import Integer, String
from sqlalchemy.orm import Session

from app.database import Base
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

class User(Base):
    __tablename__ = "users"

    id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, index=True, unique=True, nullable=False)
    email = Column(String, index=True, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

