from datetime import date

from sqlalchemy import BigInteger, CheckConstraint, Date, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Publicacion(Base):
    __tablename__ = "publicaciones"
    __table_args__ = (
        CheckConstraint("tipo IN ('propiedad', 'auto')", name="ck_publicaciones_tipo"),
        CheckConstraint(
            "estado IN ('proximo', 'realizado', 'cancelado')",
            name="ck_publicaciones_estado",
        ),
        CheckConstraint("precio > 0", name="ck_publicaciones_precio_positivo"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(120))
    tipo: Mapped[str] = mapped_column(String(20))
    precio: Mapped[int] = mapped_column(BigInteger)
    comuna: Mapped[str] = mapped_column(String(60))
    estado: Mapped[str] = mapped_column(String(20), default="proximo")
    fecha_remate: Mapped[date] = mapped_column(Date)
