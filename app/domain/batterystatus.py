from __future__ import annotations
from typing import Dict, Any
from app import db


class BatteryStatus(db.Model):
    __tablename__ = 'batterystatus'

    battery_id = db.Column(db.Integer, primary_key=True)
    battery_level = db.Column(db.Integer, nullable=False)
    measurement_time = db.Column(db.DateTime, nullable=False)
    batteryalerts_alert_id = db.Column(db.Integer, db.ForeignKey('batteryalerts.alert_id'), nullable=True)

    def __repr__(self) -> str:
        return f"BatteryStatus(battery_id={self.battery_id}, battery_level={self.battery_level}, " \
               f"measurement_time='{self.measurement_time}', batteryalerts_alert_id={self.batteryalerts_alert_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'battery_id': self.battery_id,
            'battery_level': self.battery_level,
            'measurement_time': self.measurement_time,
            'batteryalerts_alert_id': self.batteryalerts_alert_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> BatteryStatus:
        battery_status = BatteryStatus(
            battery_level=dto_dict.get('battery_level'),
            measurement_time=dto_dict.get('measurement_time'),
            batteryalerts_alert_id=dto_dict.get('batteryalerts_alert_id'),
        )
        return battery_status
