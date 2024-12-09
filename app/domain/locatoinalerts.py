from __future__ import annotations
from typing import Dict, Any
from app import db


class LocationAlert(db.Model):
    __tablename__ = 'locationalerts'

    alert_id = db.Column(db.Integer, primary_key=True)
    alert_time = db.Column(db.DateTime, nullable=False)
    alert_type = db.Column(db.String(45), nullable=False)

    def __repr__(self) -> str:
        return f"LocationAlert(alert_id={self.alert_id}, alert_time='{self.alert_time}', " \
               f"alert_type='{self.alert_type}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'alert_id': self.alert_id,
            'alert_time': self.alert_time,
            'alert_type': self.alert_type,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> LocationAlert:
        location_alert = LocationAlert(
            alert_time=dto_dict.get('alert_time'),
            alert_type=dto_dict.get('alert_type'),
        )
        return location_alert
