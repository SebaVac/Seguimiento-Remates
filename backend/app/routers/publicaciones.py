from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Publicacion
from app.schemas import PublicacionIn, PublicacionOut

router = APIRouter(prefix="/publicaciones", tags=["publicaciones"])

DbSession = Annotated[Session, Depends(get_db)]


def obtener_o_404(db: Session, publicacion_id: int) -> Publicacion:
    publicacion = db.get(Publicacion, publicacion_id)
    if publicacion is None:
        raise HTTPException(status_code=404, detail="Publicación no encontrada")
    return publicacion


@router.post("", response_model=PublicacionOut, status_code=status.HTTP_201_CREATED)
def crear_publicacion(datos: PublicacionIn, db: DbSession) -> Publicacion:
    publicacion = Publicacion(**datos.model_dump())
    db.add(publicacion)
    db.commit()
    db.refresh(publicacion)
    return publicacion


@router.get("", response_model=list[PublicacionOut])
def listar_publicaciones(db: DbSession) -> list[Publicacion]:
    return list(db.scalars(select(Publicacion).order_by(Publicacion.id)))


@router.get("/{publicacion_id}", response_model=PublicacionOut)
def obtener_publicacion(publicacion_id: int, db: DbSession) -> Publicacion:
    return obtener_o_404(db, publicacion_id)


@router.put("/{publicacion_id}", response_model=PublicacionOut)
def reemplazar_publicacion(
    publicacion_id: int, datos: PublicacionIn, db: DbSession
) -> Publicacion:
    publicacion = obtener_o_404(db, publicacion_id)
    for campo, valor in datos.model_dump().items():
        setattr(publicacion, campo, valor)
    db.commit()
    db.refresh(publicacion)
    return publicacion


@router.delete("/{publicacion_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_publicacion(publicacion_id: int, db: DbSession) -> Response:
    publicacion = obtener_o_404(db, publicacion_id)
    db.delete(publicacion)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
