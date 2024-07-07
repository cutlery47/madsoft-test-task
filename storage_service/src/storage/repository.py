from src.abstract.abstract_repository import AbstractCRUDRepository

class Repository(AbstractCRUDRepository):

    def read(self, *filters):
        pass

    def create(self, item):
        pass

    def update(self, item, *filters):
        pass

    def delete(self, *filters):
        pass