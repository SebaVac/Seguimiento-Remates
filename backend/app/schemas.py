from datetime import date
from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field, StringConstraints

Tipo = Literal["propiedad", "auto"]
Estado = Literal["proximo", "realizado", "cancelado"]

# Máximo que cabe en un BigInteger de PostgreSQL
MAX_BIGINT = 9_223_372_036_854_775_807


class PublicacionIn(BaseModel):
    """Datos que envía el cliente al crear (POST) o reemplazar (PUT)."""

    model_config = ConfigDict(extra="forbid")

    titulo: Annotated[
        str, StringConstraints(strip_whitespace=True, min_length=3, max_length=120)
    ]
    tipo: Tipo
    precio: Annotated[int, Field(gt=0, le=MAX_BIGINT, description="Pesos chilenos")]
    comuna: Annotated[
        str, StringConstraints(strip_whitespace=True, min_length=2, max_length=60)
    ]
    estado: Estado = "proximo"
    fecha_remate: date


class PublicacionOut(PublicacionIn):
    """Lo que devuelve la API: los mismos campos más el id."""

    model_config = ConfigDict(from_attributes=True)

    id: int
