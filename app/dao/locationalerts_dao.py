from .general_dao import GeneralDAO
from ..domain import LocationAlert


class LocationAlertsDAO(GeneralDAO):
    _domain_type = LocationAlert
