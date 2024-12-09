from __future__ import annotations
from typing import Dict, Any
from app import db


class Location(db.Model):
    __tablename__ = 'locations'

    location_id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Numeric(10, 6), nullable=False)  # Десяткове число з точністю
    longitude = db.Column(db.Numeric(10, 6), nullable=False)  # Десяткове число з точністю
    measurement_time = db.Column(db.DateTime, nullable=False)
    locationalerts_alert_id = db.Column(db.Integer, db.ForeignKey('locationalerts.alert_id'), nullable=True)

    def __repr__(self) -> str:
        return f"Location(location_id={self.location_id}, latitude={self.latitude}, longitude={self.longitude}, " \
               f"measurement_time='{self.measurement_time}', locationalerts_alert_id={self.locationalerts_alert_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'location_id': self.location_id,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'measurement_time': self.measurement_time,
            'locationalerts_alert_id': self.locationalerts_alert_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Location:
        location = Location(
            latitude=dto_dict.get('latitude'),
            longitude=dto_dict.get('longitude'),
            measurement_time=dto_dict.get('measurement_time'),
            locationalerts_alert_id=dto_dict.get('locationalerts_alert_id'),
        )
        return location
