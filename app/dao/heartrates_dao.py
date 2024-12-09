from .general_dao import GeneralDAO
from ..domain import HeartRate


class HeartRatesDAO(GeneralDAO):
    _domain_type = HeartRate
