from .general_service import GeneralService
from ..dao import batterystatus_dao


class BatteryStatusService(GeneralService):
    _dao = batterystatus_dao
