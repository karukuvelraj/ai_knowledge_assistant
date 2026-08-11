from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings
from app.db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="GenAI Learning Project" 
)


app.include_router(api_router)