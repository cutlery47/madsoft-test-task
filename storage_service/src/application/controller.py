import os

from src.abstract.abstract_service import AbstractService
from src.schemas.meme import InFileMemeDTO

from fastapi import APIRouter, UploadFile, Response

from io import BytesIO

class Controller:

    def __init__(self, service: AbstractService):
        self.service = service
        self.router = APIRouter(prefix="/private-api/v1")
        self.set_routes()

    def get_router(self) -> APIRouter:
        return self.router

    def set_routes(self):

        # настройка раутов

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
                                 file=BytesIO(file.file.read()))
            await self.service.add(meme)
            return "Meme was successfully uploaded"

        @self.router.put("/memes/{meme_id}")
        async def update_meme(meme_id: int, file: UploadFile):
            meme = InFileMemeDTO(object_name=file.filename,
                                 size=file.size,
                                 file=BytesIO(file.file.read()))
            await self.service.update(meme_id, meme)
            return "Meme was successfully updated"

        @self.router.delete("/memes/{meme_id}")
        async def delete_meme(meme_id: int):
            await self.service.delete(meme_id)
            return "Meme was successfully deleted"
