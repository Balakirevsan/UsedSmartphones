import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

MONGO_DETAILS = os.getenv("MONGO_DETAILS")
DATABASE_NAME = os.getenv("DATABASE_NAME")

if not MONGO_DETAILS or not DATABASE_NAME:
    raise ValueError("MONGO_DETAILS and DATABASE_NAME must be set in the .env file")

client = AsyncIOMotorClient(MONGO_DETAILS)
db = client[DATABASE_NAME]