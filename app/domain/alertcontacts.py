from __future__ import annotations
from typing import Dict, Any
from app import db

class AlertContact(db.Model):
    __tablename__ = 'alertcontacts'

    contact_id = db.Column(db.Integer, primary_key=True)
    contact_name = db.Column(db.String(45), nullable=False)
    contact_phone = db.Column(db.String(45), nullable=False)

    def __repr__(self) -> str:
        return f"AlertContact(contact_id={self.contact_id}, contact_name='{self.contact_name}', " \
               f"contact_phone='{self.contact_phone}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'contact_id': self.contact_id,
            'contact_name': self.contact_name,
            'contact_phone': self.contact_phone,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> AlertContact:
        alert_contact = AlertContact(
            contact_name=dto_dict.get('contact_name'),
            contact_phone=dto_dict.get('contact_phone'),
        )
        return alert_contact
