from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from app.db import engine
from app.models import Base
from app.routers import items

app = FastAPI(title="FastAPI Backend", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def on_startup():
    # Crea tablas en python_test si no existen
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/health")
async def health():
    async with engine.begin() as conn:
        await conn.execute(text("SELECT DATABASE()"))
    return {"status": "ok"}


# Rutas
app.include_router(items.router, prefix="/api", tags=["items"])
