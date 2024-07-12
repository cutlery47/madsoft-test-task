from abc import ABC, abstractmethod

from fastapi.routing import APIRouter

class AbstractController(ABC):

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
