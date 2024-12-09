from .heartratesalerts_service import HeartRatesAlertsService
from .alertcontacts_service import AlertContactsService
from .batterystatus_service import BatteryStatusService
from .NotificationSettings_service import  NotificationSettingsService
from .smartwatches_service import SmartwatchesService
from .heartratesalerts_service import HeartRatesAlertsService
from .heartrates_service import HeartRatesService
from .locationalerts_service import LocationAlertsService
from .owners_service import OwnersService
from .locations_service import LocationsService
from .batteryalerts_service import BatteryAlertsService

alertcontacts_service = AlertContactsService()
batterystatus_service = BatteryStatusService()
smartwatches_service = SmartwatchesService()
heartratesalerts_service = HeartRatesAlertsService()
heartrates_service = HeartRatesService()
locationalerts_service = LocationAlertsService()
owners_service = OwnersService()
locations_service = LocationsService()
batteryalerts_service = BatteryAlertsService()
NotificationSettings_service = NotificationSettingsService()
