from __future__ import annotations
from typing import Dict, Any
from app import db

class Smartwatch(db.Model):
    __tablename__ = 'smartwatches'

    watch_id = db.Column(db.Integer, primary_key=True)
    serial_number = db.Column(db.String(45), nullable=False)
    user_name = db.Column(db.String(45), nullable=False)
    locations_location_id = db.Column(db.Integer, db.ForeignKey('locations.location_id'), nullable=False)
    alertcontacts_contact_id = db.Column(db.Integer, db.ForeignKey('alertcontacts.contact_id'), nullable=False)
    heartrates_rate_id = db.Column(db.Integer, db.ForeignKey('heartrates.rate_id'), nullable=False)
    batterystatus_battery_id = db.Column(db.Integer, db.ForeignKey('batterystatus.battery_id'), nullable=False)

    def __repr__(self) -> str:
        return f"Smartwatch(watch_id={self.watch_id}, serial_number='{self.serial_number}', user_name='{self.user_name}', " \
               f"locations_location_id={self.locations_location_id}, alertcontacts_contact_id={self.alertcontacts_contact_id}, " \
               f"heartrates_rate_id={self.heartrates_rate_id}, batterystatus_battery_id={self.batterystatus_battery_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'watch_id': self.watch_id,
            'serial_number': self.serial_number,
            'user_name': self.user_name,
            'locations_location_id': self.locations_location_id,
            'alertcontacts_contact_id': self.alertcontacts_contact_id,
            'heartrates_rate_id': self.heartrates_rate_id,
            'batterystatus_battery_id': self.batterystatus_battery_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Smartwatch:
        smartwatch = Smartwatch(
            serial_number=dto_dict.get('serial_number'),
            user_name=dto_dict.get('user_name'),
            locations_location_id=dto_dict.get('locations_location_id'),
            alertcontacts_contact_id=dto_dict.get('alertcontacts_contact_id'),
            heartrates_rate_id=dto_dict.get('heartrates_rate_id'),
            batterystatus_battery_id=dto_dict.get('batterystatus_battery_id'),
        )
        return smartwatch
