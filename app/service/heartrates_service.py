from .general_service import GeneralService
from ..dao import heartrates_dao


class HeartRatesService(GeneralService):
    _dao = heartrates_dao
