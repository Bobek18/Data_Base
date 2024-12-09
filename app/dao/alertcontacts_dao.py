from app.domain import AlertContact
from .general_dao import GeneralDAO

class AlertContactsDAO(GeneralDAO):
    _domain_type = AlertContact
