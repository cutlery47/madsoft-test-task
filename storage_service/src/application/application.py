from src.abstract.abstract_application import AbstractApplication
from src.abstract.abstract_controller import AbstractController

from fastapi.applications import ASGIApp, FastAPI
from fastapi.testclient import TestClient

import os

PORT = os.getenv("STORAGE_SERVICE_PORT")

class Application(AbstractApplication):

    def __init__(self, controller=AbstractController):
        self.controller = controller

        self._app = FastAPI()
        # При создании объекта приложения сразу же настраиваем рауты
        self._app.include_router(self.controller.get_router())

    def asgi_app(self) -> ASGIApp:
        return self._app

    def test_client(self) -> TestClient:
        return TestClient(app=self._app, follow_redirects=True)

