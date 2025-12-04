from sqlalchemy import String
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column
from app.models.base import Base


class Country(Base):
    __tablename__ = "countries"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    population: Mapped[int] = mapped_column(Integer, nullable=False)

    region_id: Mapped[int] = mapped_column(
        ForeignKey("regions.id", ondelete="CASCADE"), nullable=False
    )

    region: Mapped["Region"] = relationship("Region", back_populates="countries")
