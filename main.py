from fastapi import FastAPI

from apps.routers import search
from database import engine

app = FastAPI()

# models.Base.metadata.create_all(bind=engine)

app.include_router(search.router)
