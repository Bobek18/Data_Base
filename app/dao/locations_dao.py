from .general_dao import GeneralDAO
from ..domain import Location


class LocationsDAO(GeneralDAO):
    _domain_type = Location
