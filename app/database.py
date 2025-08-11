from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
import boto3

load_dotenv()

if os.getenv("DATABASE_URL") is None:
    raise ValueError("DATABASE_URL environment variable is not set")

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

if OS.getenv("AWS_ACCESS_KEY_ID") is None or os.getenv("AWS_SECRET_ACCESS_KEY") is None:
    raise ValueError("AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY environment variables must be set")

s3 = boto3.client(
    "s3",
    endpoint_url="http://localhost:4566",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID", "test"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY", "test"),
    region_name=os.getenv("AWS_DEFAULT_REGION", "us-east-1"),
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_s3():
    return s3