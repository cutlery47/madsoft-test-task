from src.abstract.abstract_s3 import AbstractS3
from src.abstract.abstract_repository import AbstractCRUDRepository
from src.schemas.meme import InFileMemeDTO

from abc import ABC, abstractmethod

class AbstractService(ABC):

    @abstractmethod
    def __init__(self,
                 s3: AbstractS3,
                 repository: AbstractCRUDRepository):
        raise NotImplementedError

    @abstractmethod
    def get(self, id_: int):
        """
        Retrieving data by id
        :param id_:
        :return:
        """
        raise NotImplementedError

    @abstractmethod
    def get_all(self):
        """
        Retrieving all the data
        :return:
        """
        raise NotImplementedError

    @abstractmethod
    def add(self, meme: InFileMemeDTO):
        """
        Adding a new meme
        :param meme:
        :return:
        """

    @abstractmethod
    def delete(self, id_: int):
        """
        Deleting an item by id
        :param id_:
        :return:
        """

    @abstractmethod
    def update(self, id_: int, meme: InFileMemeDTO):
        """
        Updating aa meme by id
        :param id_:
        :param meme:
        :return:
        """