from src.abstract.abstract_s3 import AbstractS3
from src.schemas.meme import InFileMemeDTO, InDatabaseMemeDTO

from minio import Minio

import os

ENDPOINT = os.getenv('MINIO_ENDPOINT')
ACCESS = os.getenv('MINIO_ACCESS')
PASSWD = os.getenv('MINIO_PASSWRD')
BUCKET = os.getenv('MINIO_BUCKET')

class MinioS3(AbstractS3):

    def __init__(self):
        self._minio = Minio(endpoint=ENDPOINT,
                            access_key=ACCESS,
                            secret_key=PASSWD,
                            region='ru',
                            secure=False)

        if not self._minio.bucket_exists(BUCKET):
            self._minio.make_bucket(BUCKET)

    def upload(self, meme: InFileMemeDTO) -> InDatabaseMemeDTO:

        uploaded = self._minio.put_object(bucket_name=BUCKET,
                                          object_name=meme.object_name,
                                          data=meme.file,
                                          length=meme.size)

        return InDatabaseMemeDTO(object_name=uploaded.object_name,
                                 bucket_name=uploaded.bucket_name,
                                 size=meme.size,
                                 etag=uploaded.etag)


    def get(self, link: str):
        pass

    def delete(self, link: str):
        pass


