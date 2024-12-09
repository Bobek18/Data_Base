from .general_controller import GeneralController
from ..service import NotificationSettings_service


class NotificationSettingsController(GeneralController):
    _service = NotificationSettings_service
