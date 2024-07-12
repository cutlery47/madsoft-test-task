from src.abstract.abstract_factory import AbstractFactory
from src.abstract.abstract_application import AbstractApplication
from src.abstract.abstract_controller import AbstractController


class ApplicationFactory(AbstractFactory):

    def __init__(self,
                 Application: AbstractApplication.__class__,
                 Controller: AbstractController.__class__):

        controller = Controller()

        self.application = Application(controller=controller)


    def create(self):
        return self.application.asgi_app()
