from src.abstract.abstract_s3 import AbstractS3
from src.schemas.meme import InFileMemeDTO, InDatabaseMemeDTO, DatabaseMemeDTO, FileMemeDTO
from src.exceptions.s3_exc import S3MemeNotFoundException

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

    def get(self, memes: [DatabaseMemeDTO]) -> [FileMemeDTO]:

        result = []

        for meme in memes:
            s3_meme = self._minio.get_object(bucket_name=meme.bucket_name, object_name=meme.object_name)
            result.append(s3_meme)

        return result

    def delete(self, meme: DatabaseMemeDTO):

        if not self._minio.get_object(bucket_name=meme.bucket_name, object_name=meme.object_name):
            raise S3MemeNotFoundException()

        self._minio.remove_object(bucket_name=meme.bucket_name, object_name=meme.object_name)
