from abc import ABC, abstractmethod

from src.storage.models.meme import Meme
from typing import List


class AbstractCRUDRepository(ABC):

    @abstractmethod
    async def create(self, item: Meme):
        """
        Adding an item to a storage
        :param item: A new piece of data to be stored
        :return:
        """
        raise NotImplementedError

    @abstractmethod
    async def read(self, id_: int | None) -> List[Meme]:
        """
        Retrieving data, which satisfies the filters
        :param id_: Data parameters
        :return:
        """
        raise NotImplementedError

    @abstractmethod
    async def update(self, item: Meme, id_: int):
        """
        Updating data, which satisfies the filters, with the new item data
        :param item: New item data
        :param id_: Data parameters
        :return:
        """

    @abstractmethod
    async def delete(self, id_: int):
        """
        Deleting data, which satisfies the filters
        :param id_: Data parameters
        :return:
        """