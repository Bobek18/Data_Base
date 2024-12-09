from __future__ import annotations
from typing import Dict, Any
from app import db


class HeartRate(db.Model):
    __tablename__ = 'heartrates'

    rate_id = db.Column(db.Integer, primary_key=True)
    heart_rate = db.Column(db.Integer, nullable=False)
    measurement_time = db.Column(db.DateTime, nullable=False)
    user_name = db.Column(db.String(45), nullable=False)
    heartratealerts_alert_id = db.Column(db.Integer, db.ForeignKey('heartratealerts.alert_id'), nullable=True)

    def __repr__(self) -> str:
        return f"HeartRate(rate_id={self.rate_id}, heart_rate={self.heart_rate}, " \
               f"measurement_time='{self.measurement_time}', user_name='{self.user_name}', " \
               f"heartratealerts_alert_id={self.heartratealerts_alert_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'rate_id': self.rate_id,
            'heart_rate': self.heart_rate,
            'measurement_time': self.measurement_time,
            'user_name': self.user_name,
            'heartratealerts_alert_id': self.heartratealerts_alert_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> HeartRate:
        heartrate = HeartRate(
            heart_rate=dto_dict.get('heart_rate'),
            measurement_time=dto_dict.get('measurement_time'),
            user_name=dto_dict.get('user_name'),
            heartratealerts_alert_id=dto_dict.get('heartratealerts_alert_id'),
        )
        return heartrate
