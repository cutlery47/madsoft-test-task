from dotenv import find_dotenv, load_dotenv

env_path = find_dotenv('storage.env')
load_dotenv(env_path)

from src.application.factory import ApplicationFactory
from src.application.application import Application
from src.application.controller import Controller
from src.application.service import Service
from src.storage.repository import Repository
from src.storage.s3 import MinioS3

app = ApplicationFactory(
    Application=Application,
    Controller=Controller,
    Service=Service,
    Repository=Repository,
    S3=MinioS3
).create().asgi_app()

