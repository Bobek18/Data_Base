from .general_controller import GeneralController
from ..service import batterystatus_service


class BatteryStatusController(GeneralController):
    _service = batterystatus_service
