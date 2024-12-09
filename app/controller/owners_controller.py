from .general_controller import GeneralController
from ..service import owners_service


class OwnersController(GeneralController):
    _service = owners_service
