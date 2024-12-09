from .general_controller import GeneralController
from ..service import heartrates_service


class HeartRatesController(GeneralController):
    _service = heartrates_service
