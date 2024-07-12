from src.abstract.abstract_application import AbstractApplication
from src.abstract.abstract_controller import AbstractController

from fastapi import FastAPI

class Application(AbstractApplication):

    def __init__(self, controller: AbstractController):
        self.controller = controller
        self._app = FastAPI()
        self._app.include_router(self.controller.get_router())

    def asgi_app(self) -> FastAPI:
        return self._app
