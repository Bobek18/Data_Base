from .general_dao import GeneralDAO
from ..domain import BatteryStatus


class BatteryStatusDAO(GeneralDAO):
    _domain_type = BatteryStatus
