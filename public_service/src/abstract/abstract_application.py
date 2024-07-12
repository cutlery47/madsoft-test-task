from abc import ABC, abstractmethod

from fastapi import FastAPI

class AbstractApplication(ABC):

    @abstractmethod
    def asgi_app(self) -> FastAPI:
        """
        :return: asgi application
        """
        raise NotImplementedError
