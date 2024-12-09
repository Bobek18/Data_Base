from .general_dao import GeneralDAO
from ..domain import BatteryAlert


class BatteryAlertsDAO(GeneralDAO):
    _domain_type = BatteryAlert
