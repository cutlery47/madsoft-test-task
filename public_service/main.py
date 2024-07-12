from src.application.factory import ApplicationFactory
from src.application.application import Application
from src.application.controller import Controller

app = ApplicationFactory(
    Application=Application,
    Controller=Controller
).create()
