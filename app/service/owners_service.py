from .general_service import GeneralService
from ..dao import owners_dao


class OwnersService(GeneralService):
    _dao = owners_dao
