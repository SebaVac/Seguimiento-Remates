from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app import models  # noqa: F401  (registra las tablas en Base.metadata)
from app.database import Base, engine
from app.routers import publicaciones


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    # Crea las tablas que falten al arrancar (no modifica las existentes)
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="Seguimiento Remates", lifespan=lifespan)

app.include_router(publicaciones.router)


@app.get("/health")
def health() -> dict[str, str]:
    """Indica que la API está viva."""
    return {"status": "ok"}
