from abc import ABC, abstractmethod
from fastapi import FastAPI

from src.abstract.abstract_service import AbstractService

class AbstractApplication(ABC):

    @abstractmethod
    def __init__(self, service: AbstractService):
        raise NotImplementedError

    @abstractmethod
    def asgi_app(self) -> FastAPI:
        """
        Returns runnable asgi app
        :return: FastAPI app
        """
