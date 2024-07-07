from src.abstract.abstract_factory import AbstractApplicationFactory
from src.abstract.abstract_application import AbstractApplication
from src.abstract.abstract_controller import AbstractController
from src.abstract.abstract_service import AbstractService
from src.abstract.abstract_repository import AbstractCRUDRepository
from src.abstract.abstract_s3 import AbstractS3


class ApplicationFactory(AbstractApplicationFactory):

    def __init__(self,
                 Application: AbstractApplication.__class__,
                 Controller: AbstractController.__class__,
                 Service: AbstractService.__class__,
                 Repository: AbstractCRUDRepository.__class__,
                 S3: AbstractS3.__class__
                 ):

        s3 = S3()

        repository = Repository()

        service = Service(s3=s3, repository=repository)

        controller = Controller(service=service)

        self.application = Application(controller=controller)


    def create(self) -> AbstractApplication:
        return self.application
