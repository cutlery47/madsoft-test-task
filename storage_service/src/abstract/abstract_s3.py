from src.schemas.meme import InFileMemeDTO, DatabaseMemeDTO, InDatabaseMemeDTO

from abc import ABC, abstractmethod

class AbstractS3(ABC):

    @abstractmethod
    def get(self, memes: list[DatabaseMemeDTO]):
        """
        Retrieving memes from S3
        :param memes:
        :return:
        """

    @abstractmethod
    def upload(self, in_meme: InFileMemeDTO) -> InDatabaseMemeDTO:
        """
        Uploading meme to S3
        :param in_meme:
        :return:
        """

    @abstractmethod
    def delete(self, meme: DatabaseMemeDTO):
        """
        Deleting meme from S3
        :param meme:
        :return:
        """