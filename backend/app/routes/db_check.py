from fastapi import APIRouter
from app.config.database import db

router = APIRouter()

@router.get("/db-check")
async def db_check():
    try:
        # Проверяем подключение, запросив список коллекций
        collections = await db.list_collection_names()
        return {"status": "connected", "collections": collections}
    except Exception as e:
        return {"status": "error", "message": str(e)}