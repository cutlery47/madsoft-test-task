from sqlalchemy.orm import Mapped, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs

from src.storage.models.annotated_types import pk, str_256, timestamp

class Base(DeclarativeBase, AsyncAttrs):
    pass

class Meme(Base):
    __tablename__ = "memes"

    id: Mapped[pk]
    size: Mapped[int]
    object_name: Mapped[str_256]
    bucket_name: Mapped[str_256]
    etag: Mapped[str_256]
    created_at: Mapped[timestamp]
