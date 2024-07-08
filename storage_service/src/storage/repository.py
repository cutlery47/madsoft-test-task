from src.abstract.abstract_repository import AbstractCRUDRepository
from src.storage.models.meme import Meme


class Repository(AbstractCRUDRepository):

    async def read(self, *filters) -> Meme:
        pass

    async def create(self, item: Meme):
        pass

    async def update(self, item: Meme, *filters):
        pass

    async def delete(self, *filters):
        pass
