from .general_service import GeneralService
from ..dao import locationalerts_dao


class LocationAlertsService(GeneralService):
    _dao = locationalerts_dao
