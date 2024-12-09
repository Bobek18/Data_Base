from .general_dao import GeneralDAO
from ..domain import NotificationSetting


class NotificationSettingsDAO(GeneralDAO):
    _domain_type = NotificationSetting
