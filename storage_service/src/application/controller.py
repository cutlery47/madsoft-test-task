from src.abstract.abstract_service import AbstractService
from src.schemas.meme import InFileMemeDTO

from fastapi import APIRouter, UploadFile

class Controller:

    def __init__(self, service: AbstractService):
        self.service = service
        self.router = APIRouter(prefix="/private-api/v1")
        self.set_routes()

    def get_router(self) -> APIRouter:
        return self.router

    def set_routes(self):

        @self.router.get("/memes/")
        async def get_memes():
            return await self.service.get_all()

        @self.router.get("/memes/{meme_id}")
        async def get_meme(meme_id: int):
            return await self.service.get(meme_id)

        @self.router.post("/memes/")
        async def add_meme(file: UploadFile):
            meme = InFileMemeDTO(object_name=file.filename,
                                 size=file.size,
                                 file=file.file)
            return await self.service.add(meme)

        @self.router.put("/memes/{meme_id}")
        async def update_meme(meme_id: int, file: UploadFile):
            meme = InFileMemeDTO(object_name=file.filename,
                                 size=file.size,
                                 file=file.file)
            return await self.service.update(meme_id, meme)

        @self.router.delete("/memes/{meme_id}")
        async def delete_meme(meme_id: int):
            return await self.service.delete(meme_id)
