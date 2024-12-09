from .general_controller import GeneralController
from ..service import smartwatches_service


class SmartWatchesController(GeneralController):
    _service = smartwatches_service