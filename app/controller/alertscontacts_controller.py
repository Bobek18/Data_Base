from .general_controller import GeneralController
from ..service import alertcontacts_service


class AlertsContactsController(GeneralController):
    _service = alertcontacts_service
