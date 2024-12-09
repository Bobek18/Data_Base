from .locationalerts_dao import LocationAlertsDAO
from .smartwatches_dao import SmartWatchesDAO
from .batterystatus_dao import BatteryStatusDAO
from .heartrates_dao import HeartRatesDAO
from .NotificationSettings_dao import NotificationSettingsDAO
from .alertcontacts_dao import AlertContactsDAO
from .owners_dao import OwnersDAO
from .heartratesalerts_dao import HeartRatesAlertsDAO
from .locations_dao import LocationsDAO
from .batteryalerts_dao import BatteryAlertsDAO

player_stat_dao = LocationAlertsDAO()
match_stat_dao = SmartWatchesDAO()
referee_dao = BatteryStatusDAO()
start_lineup_dao = HeartRatesDAO()
league_dao = NotificationSettingsDAO()
stadium_dao = AlertContactsDAO()
team_dao = OwnersDAO()
referee_team_dao = HeartRatesAlertsDAO()
match_dao = LocationsDAO()
goal_dao = BatteryAlertsDAO()