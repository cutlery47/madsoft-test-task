from src.application.application import Application
from src.application.factory import ApplicationFactory
from src.application.controller import Controller
from src.application.service import Service
from tests.mock.mock_repository import MockRepository
from tests.mock.mock_s3 import MockS3

from fastapi.testclient import TestClient

import pytest

@pytest.fixture
def app():
    app = ApplicationFactory(
        Application=Application,
        Controller=Controller,
        Service=Service,
        Repository=MockRepository,
        S3=MockS3
    ).create()
    return app

@pytest.fixture
def client(app) -> TestClient:
    return app.test_client()
