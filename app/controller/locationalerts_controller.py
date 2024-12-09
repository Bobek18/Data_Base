from .general_controller import GeneralController
from ..service import locationalerts_service


class LocationAlertsController(GeneralController):
    _service = locationalerts_service
