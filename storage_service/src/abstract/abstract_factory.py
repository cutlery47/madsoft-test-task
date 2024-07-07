from abc import abstractmethod, ABC

from src.abstract.abstract_application import AbstractApplication
from src.abstract.abstract_controller import AbstractController
from src.abstract.abstract_service import AbstractService
from src.abstract.abstract_repository import AbstractCRUDRepository
from src.abstract.abstract_s3 import AbstractS3

class AbstractApplicationFactory(ABC):

    @abstractmethod
    def __init__(self,
                 Application: AbstractApplication.__class__,
                 Controller: AbstractController.__class__,
                 Service: AbstractService.__class__,
                 Repository: AbstractCRUDRepository.__class__,
                 S3: AbstractS3.__class__
                 ):
        raise NotImplementedError

    @abstractmethod
    def create(self) -> AbstractApplication:
        """
        Creates and sets up an application instance
        :return: AbstractApplication
        """