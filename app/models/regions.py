from sqlalchemy import String
from sqlalchemy.orm import Mapped, relationship, mapped_column
from app.models.base import Base


class Region(Base):
    __tablename__ = "regions"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    countries: Mapped[list["Country"]] = relationship(
        "Country", back_populates="region"
    )
