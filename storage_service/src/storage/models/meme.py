from sqlalchemy.orm import Mapped, DeclarativeBase

from src.storage.models.annotated_types import pk, str_256, timestamp

class Meme(DeclarativeBase):

    id: Mapped[pk]
    size: Mapped[int]
    bucket_name: Mapped[str_256]
    etag: Mapped[str_256]
    created_at: Mapped[timestamp]