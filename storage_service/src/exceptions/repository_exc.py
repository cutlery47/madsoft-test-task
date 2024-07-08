from fastapi import HTTPException
from starlette import status

class RepositoryException(HTTPException):
    pass

class DatabaseMemeNotFoundException(RepositoryException):
    status_code = status.HTTP_404_NOT_FOUND

    def __init__(self, detail="Requested meme was not found"):
        self.detail = detail

class InternalRepositoryException(RepositoryException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    def __init__(self, detail="An error occurred when processing your request"):
        self.detail = detail
