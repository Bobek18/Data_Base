from .general_controller import GeneralController
from ..service import heartratesalerts_service


class HeartRateAlertsController(GeneralController):
    _service = heartratesalerts_service
