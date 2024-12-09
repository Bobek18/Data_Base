from .general_service import GeneralService
from ..dao import smartwatches_dao


class SmartwatchesService(GeneralService):
    _dao = smartwatches_dao
