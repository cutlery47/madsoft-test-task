from src.abstract.abstract_service import AbstractService
from src.abstract.abstract_s3 import AbstractS3
from src.abstract.abstract_repository import AbstractCRUDRepository
from src.schemas.meme import InFileMemeDTO, DatabaseMemeDTO, FileMemeDTO
from src.storage.models.meme import Meme
from src.application.utils import meme_to_dict

from typing import List

class Service(AbstractService):

    def __init__(self, s3: AbstractS3, repository: AbstractCRUDRepository):
        self.s3 = s3
        self.repository = repository

    async def get(self, id_: int) -> FileMemeDTO:
        meme = await self.repository.read(Meme.id == id_)
        s3_meme = DatabaseMemeDTO.model_validate(meme_to_dict(meme[0]), from_attributes=True)
        return self.s3.get(memes=[s3_meme])[0]

    async def get_all(self) -> List[FileMemeDTO]:
        memes = await self.repository.read()
        s3_memes = [DatabaseMemeDTO.model_validate(meme, from_attributes=True) for meme in memes]
        return self.s3.get(memes=s3_memes)

    async def add(self, meme: InFileMemeDTO):
        uploaded_meme = self.s3.upload(meme)
        database_meme = Meme(**uploaded_meme.model_dump())
        await self.repository.create(database_meme)

    async def delete(self, id_: int):
        database_meme = await self.repository.read(Meme.id == id_)
        s3_meme = DatabaseMemeDTO.model_validate(database_meme[0], from_attributes=True)

        self.s3.delete(s3_meme)
        await self.repository.delete(Meme.id == id_)

        return True

    async def update(self, id_: int, meme: InFileMemeDTO):
        database_meme = await self.repository.read(Meme.id == id_)
        s3_meme = DatabaseMemeDTO.model_validate(database_meme[0], from_attributes=True)
        self.s3.delete(s3_meme)
        new_s3_meme = self.s3.upload(meme)
        new_database_meme = Meme(**new_s3_meme.model_dump())
        await self.repository.update(new_database_meme, Meme.id == id_)
