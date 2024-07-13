from src.application.factory import ApplicationFactory
from src.application.application import Application
from src.application.controller import Controller

from dotenv import find_dotenv, load_dotenv

env_path = find_dotenv('storage.env')
load_dotenv(env_path)

app = ApplicationFactory(
    Application=Application,
    Controller=Controller
).create()
