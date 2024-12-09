from .general_dao import GeneralDAO
from ..domain import smartwatches


class SmartWatchesDAO(GeneralDAO):
    _domain_type = smartwatches

