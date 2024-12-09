from .general_service import GeneralService
from ..dao import NotificationSettings_dao


class NotificationSettingsService(GeneralService):
    _dao = NotificationSettings_dao
