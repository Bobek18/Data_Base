from .general_dao import GeneralDAO
from ..domain import HeartRateAlert


class HeartRatesAlertsDAO(GeneralDAO):
    _domain_type = HeartRateAlert
