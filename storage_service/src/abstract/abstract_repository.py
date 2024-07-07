from abc import ABC, abstractmethod

class AbstractCRUDRepository(ABC):

    @abstractmethod
    def create(self, item):
        """
        Adding an item to a storage
        :param item: A new piece of data to be stored
        :return:
        """
        raise NotImplementedError

    @abstractmethod
    def read(self, *filters):
        """
        Retrieving data, which satisfies the filters
        :param filters: Data parameters
        :return:
        """
        raise NotImplementedError

    @abstractmethod
    def update(self, item, *filters):
        """
        Updating data, which satisfies the filters, with the new item data
        :param item: New item data
        :param filters: Data parameters
        :return:
        """

    @abstractmethod
    def delete(self, *filters):
        """
        Deleting data, which satisfies the filters
        :param filters: Data parameters
        :return:
        """