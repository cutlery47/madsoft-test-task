from fastapi import APIRouter, UploadFile
from fastapi.responses import JSONResponse

from src.abstract.abstract_controller import AbstractController

import httpx

class Controller(AbstractController):

    def __init__(self):
        self.router = APIRouter(prefix="/api/v1")
        self.set_routes()

    def set_routes(self):

        @self.router.get("/memes/")
        async def get_memes():
            async with httpx.AsyncClient() as client:
                response = await client.get("http://127.0.0.1:8000/private-api/v1/memes/")
                return JSONResponse(status_code=response.status_code,
                                    content=response.json())

        @self.router.get("/memes/{meme_id}")
        async def get_meme(meme_id: int):
            async with httpx.AsyncClient() as client:
                response = await client.get(f"http://127.0.0.1:8000/private-api/v1/memes/{meme_id}")
                return JSONResponse(status_code=response.status_code,
                                    content=response.json())


        @self.router.post("/memes")
        async def add_meme(file: UploadFile):
            async with httpx.AsyncClient() as client:
                response = await client.post("http://127.0.0.1:8000/private-api/v1/memes/", files={'file': file})
                return JSONResponse(status_code=response.status_code,
                                    content=response.json())

        @self.router.put("/memes/{meme_id}")
        async def update_meme(meme_id: int, file: UploadFile):
            async with httpx.AsyncClient() as client:
                response = await client.put(f"http://127.0.0.1:8000/private-api/v1/memes/{meme_id}", files={'file': file})
                return JSONResponse(status_code=response.status_code,
                                    content=response.json())

        @self.router.delete("/memes/{meme_id}")
        async def delete_meme(meme_id: int):
            async with httpx.AsyncClient() as client:
                response = await client.delete(f"http://127.0.0.1:8000/private-api/v1/memes/{meme_id}")
                return JSONResponse(status_code=response.status_code,
                                    content=response.json())

    def get_router(self) -> APIRouter:
        return self.router
