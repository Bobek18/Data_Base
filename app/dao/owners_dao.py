from .general_dao import GeneralDAO
from ..domain import Owner


class OwnersDAO(GeneralDAO):
    _domain_type = Owner