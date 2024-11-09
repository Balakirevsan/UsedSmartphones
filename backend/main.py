import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import db_check
from app.routes import user_route
from app.routes import redis_route
from app.routes import role_route  # Import roles router
from app.models.role import Role
from app.config.database import db
from contextlib import asynccontextmanager

logging.basicConfig(level=logging.INFO)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup actions
    default_roles = [
        "super admin",
        "admin",
        "service_company",
        "contractor",
        "subcontractor",
        "service_technician",
        "house_technician",
        "visitor"
    ]
    existing_roles = await db["roles"].find().to_list(1000)
    existing_role_names = {role["name"] for role in existing_roles}
    roles_to_create = [Role(name=role) for role in default_roles if role not in existing_role_names]
    
    if roles_to_create:
        await db["roles"].insert_many([role.dict() for role in roles_to_create])
        logging.info("Default roles have been initialized.")
    else:
        logging.info("Default roles already exist.")
    
    yield  # Application runs here

    # Shutdown actions (if any)
    # ...existing code...

app = FastAPI(lifespan=lifespan)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(role_route.router)  # Include roles router
app.include_router(redis_route.router)
app.include_router(db_check.router)
app.include_router(user_route.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI backend!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)