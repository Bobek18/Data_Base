from .general_service import GeneralService
from ..dao import batteryalerts_dao


class BatteryAlertsService(GeneralService):
    _dao =batteryalerts_dao
