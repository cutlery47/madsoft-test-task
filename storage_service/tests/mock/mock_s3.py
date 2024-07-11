from typing import List

from src.abstract.abstract_s3 import AbstractS3
from src.schemas.meme import InFileMemeDTO, InDatabaseMemeDTO, DatabaseMemeDTO, FileMemeDTO


class MockS3(AbstractS3):

    def __init__(self):
        self.bucket = {'meme-storage': {}}

    def upload(self, in_meme: InFileMemeDTO) -> InDatabaseMemeDTO:
        data = InDatabaseMemeDTO(object_name=in_meme.object_name,
                                 size=in_meme.size,
                                 bucket_name='meme-storage',
                                 etag='123123',
                                 link=in_meme.object_name)
        self.bucket['meme-storage'][in_meme.object_name] = data
        return data

    def get(self, memes: List[DatabaseMemeDTO]) -> List[FileMemeDTO]:
        res = []
        for meme in memes:
            res.append(self.bucket['meme-storage'].get(meme.object_name))
        return res

    def delete(self, meme: DatabaseMemeDTO):
        print(meme.object_name)
        self.bucket['meme-storage'].pop(meme.object_name)
