from src.abstract.abstract_service import AbstractService
from src.abstract.abstract_s3 import AbstractS3
from src.abstract.abstract_repository import AbstractCRUDRepository
from src.schemas.meme import InFileMemeDTO

from fastapi import UploadFile

class Service(AbstractService):

    def __init__(self, s3: AbstractS3, repository: AbstractCRUDRepository):
        self.s3 = s3
        self.repository = repository

    async def get(self, id_: int):
        meme = self.repository.read(id_)
        return self.s3.get(names=[meme])

    async def get_all(self):
        memes = self.repository.read()
        return self.s3.get(names=memes)

    async def add(self, meme: InFileMemeDTO):
        uploaded = self.s3.upload(meme)
        self.repository.create(uploaded)

    async def delete(self, id_: int):
        meme = self.repository.delete(id_)


    async def update(self, id_: int, item):
        pass
