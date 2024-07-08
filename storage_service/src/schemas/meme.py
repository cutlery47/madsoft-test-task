from pydantic import BaseModel, PositiveInt, ConfigDict
from datetime import datetime
from io import BytesIO


class BaseMemeDTO(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    object_name: str
    size: PositiveInt

class InDatabaseMemeDTO(BaseMemeDTO):
    bucket_name: str
    etag: str

class DatabaseMemeDTO(InDatabaseMemeDTO):
    created_at: datetime


class InFileMemeDTO(BaseMemeDTO):

    file: BytesIO

class FileMemeDTO(DatabaseMemeDTO):

    file: BytesIO






