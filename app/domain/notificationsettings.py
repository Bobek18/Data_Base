from __future__ import annotations
from typing import Dict, Any
from app import db

class NotificationSetting(db.Model):
    __tablename__ = 'NotificationSettings'

    setting_id = db.Column(db.Integer, primary_key=True)
    is_heart_rate_alert_enabled = db.Column(db.Boolean, nullable=False)
    is_battery_alert_enabled = db.Column(db.Boolean, nullable=False)
    is_location_alert_enabled = db.Column(db.Boolean, nullable=False)
    smartwatch_watch_id = db.Column(db.Integer, db.ForeignKey('smartwatches.watch_id'), nullable=False)

    def __repr__(self) -> str:
        return f"NotificationSetting(setting_id={self.setting_id}, " \
               f"is_heart_rate_alert_enabled={self.is_heart_rate_alert_enabled}, " \
               f"is_battery_alert_enabled={self.is_battery_alert_enabled}, " \
               f"is_location_alert_enabled={self.is_location_alert_enabled}, " \
               f"sportwatch_watch_id={self.smartwatch_watch_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'setting_id': self.setting_id,
            'is_heart_rate_alert_enabled': self.is_heart_rate_alert_enabled,
            'is_battery_alert_enabled': self.is_battery_alert_enabled,
            'is_location_alert_enabled': self.is_location_alert_enabled,
            'smartwatch_watch_id': self.smartwatch_watch_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> NotificationSetting:
        notification_setting = NotificationSetting(
            is_heart_rate_alert_enabled=dto_dict.get('is_heart_rate_alert_enabled'),
            is_battery_alert_enabled=dto_dict.get('is_battery_alert_enabled'),
            is_location_alert_enabled=dto_dict.get('is_location_alert_enabled'),
            smartwatch_watch_id=dto_dict.get('smartwatch_watch_id'),
        )
        return notification_setting
