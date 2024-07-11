from typing import List

from src.abstract.abstract_repository import AbstractCRUDRepository
from src.storage.models.meme import Meme
from src.exceptions.repository_exc import DatabaseMemeNotFoundException

from datetime import datetime


class MockRepository(AbstractCRUDRepository):

    def __init__(self):
        self.storage = {}

    async def create(self, item: Meme):
        item.id = len(self.storage.keys()) + 1
        item.created_at = datetime.now()
        self.storage[item.id] = item

    async def delete(self, id_: int):
        if not self.storage.pop(id_, None):
            raise DatabaseMemeNotFoundException()

    async def read(self, id_: int = None) -> List[Meme]:
        if not id_:
            return [*self.storage.values()]
        else:
            meme = self.storage.get(id_)
            if not meme:
                raise DatabaseMemeNotFoundException()
            else:
                return [meme]


    async def update(self, item: Meme, id_: int):
        if not self.storage.get(id_):
            raise DatabaseMemeNotFoundException()
        else:
            self.storage[id_] = item
