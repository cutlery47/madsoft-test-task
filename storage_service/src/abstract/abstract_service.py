from src.abstract.abstract_s3 import AbstractS3
from src.abstract.abstract_repository import AbstractCRUDRepository
from src.schemas.meme import InFileMemeDTO, FileMemeDTO

from typing import List

from abc import ABC, abstractmethod

class AbstractService(ABC):

    @abstractmethod
    def __init__(self,
                 s3: AbstractS3,
                 repository: AbstractCRUDRepository):
        raise NotImplementedError

    @abstractmethod
    async def get(self, id_: int) -> FileMemeDTO:
        """
        Retrieving data by id
        :param id_:
        :return:
        """
        raise NotImplementedError

    @abstractmethod
    async def get_all(self) -> List[FileMemeDTO]:
        """
        Retrieving all the data
        :return:
        """
        raise NotImplementedError

    @abstractmethod
    async def add(self, meme: InFileMemeDTO) -> bool:
        """
        Adding a new meme
        :param meme:
        :return:
        """

    @abstractmethod
    async def delete(self, id_: int) -> bool:
        """
        Deleting an item by id
        :param id_:
        :return:
        """

    @abstractmethod
    async def update(self, id_: int, meme: InFileMemeDTO) -> bool:
        """
        Updating aa meme by id
        :param id_:
        :param meme:
        :return:
        """