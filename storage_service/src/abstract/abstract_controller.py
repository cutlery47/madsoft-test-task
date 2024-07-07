from abc import ABC, abstractmethod

from fastapi import APIRouter

from src.abstract.abstract_service import AbstractService

class AbstractController(ABC):

    @abstractmethod
    def __init__(self, service: AbstractService):
        raise NotImplementedError

    @abstractmethod
    def get_router(self) -> APIRouter:
        """
        Returns a FastAPI router
        :return:
        """
        raise NotImplementedError

    @abstractmethod
    def set_routes(self):
        """
        Sets url routes for given router
        :return:
        """
        raise NotImplementedError
