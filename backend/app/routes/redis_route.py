# app/routes/redis_route.py
from fastapi import APIRouter, HTTPException
from app.config.redis_config import redis_client
from typing import Optional
import logging

router = APIRouter(prefix="/redis", tags=["redis"])

logger = logging.getLogger(__name__)

@router.post("/set/{key}")
async def set_value(key: str, value: str):
    try:
        redis_client.set(key, value)
        return {"message": f"Successfully set {key}={value}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get/{key}", response_model=dict)
async def get_value(key: str) -> dict:
    try:
        value = redis_client.get(key)
        logger.info(f"Retrieved value from Redis: {value}")  # Log the value
        if value is None:
            raise HTTPException(status_code=404, detail="Key not found")
        return {"key": key, "value": value.decode('utf-8') if isinstance(value, bytes) else str(value)}  # Ensure value is a string
    except Exception as e:
        logger.error(f"Error retrieving value from Redis: {e}")  # Log the error
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/delete/{key}")
async def delete_value(key: str):
    try:
        if redis_client.delete(key):
            return {"message": f"Successfully deleted {key}"}
        raise HTTPException(status_code=404, detail="Key not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))