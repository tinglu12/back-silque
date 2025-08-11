from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy.orm import Session

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, unique=True, nullable=False)
    email = Column(String, index=True, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

