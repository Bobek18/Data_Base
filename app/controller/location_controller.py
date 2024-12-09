from .general_controller import GeneralController
from ..service import locations_service


class LocationController(GeneralController):
    _service = locations_service

