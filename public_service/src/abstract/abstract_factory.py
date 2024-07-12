from abc import ABC, abstractmethod

class AbstractFactory(ABC):

    @abstractmethod
    def create(self):
        """
        creates an app instance
        :return:
        """
        raise NotImplementedError
