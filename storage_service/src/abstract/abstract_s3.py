from src.schemas.meme import InFileMemeDTO, DatabaseMemeDTO, InDatabaseMemeDTO, FileMemeDTO

from typing import List

from abc import ABC, abstractmethod

class AbstractS3(ABC):

    @abstractmethod
    def get(self, memes: List[DatabaseMemeDTO]) -> List[FileMemeDTO]:
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
    def delete(self, meme: DatabaseMemeDTO) -> bool:
        """
        Deleting meme from S3
        :param meme:
        :return:
        """

    @abstractmethod
    def rollback(self, steps: int) -> bool:
        """
        Reverting last steps-amount operations
        :param steps:
        :return:
        """