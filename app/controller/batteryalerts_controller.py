from .general_controller import GeneralController
from ..service import batteryalerts_service


class BatteryAlertsController(GeneralController):
    _service = batteryalerts_service
