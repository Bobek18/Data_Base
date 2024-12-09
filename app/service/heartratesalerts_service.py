from .general_service import GeneralService
from ..dao import heartratesalerts_dao


class HeartRatesAlertsService(GeneralService):
    _dao = heartratesalerts_dao
