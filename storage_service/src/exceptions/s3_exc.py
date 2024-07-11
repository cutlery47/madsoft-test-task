from fastapi import HTTPException
from starlette import status

class S3Exception(HTTPException):
    pass

class S3MemeNotFoundException(S3Exception):
    status_code = status.HTTP_404_NOT_FOUND

    def __init__(self, detail="Requested meme was not found"):
        self.detail = detail

class InternalS3Exception(S3Exception):
    status_code = status.HTTP_404_NOT_FOUND

    def __init__(self, detail="An error occurred when processing your request"):
        self.detail = detail
