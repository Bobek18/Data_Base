from __future__ import annotations
from typing import Dict, Any
from app import db


class Owner(db.Model):
    __tablename__ = 'owners'

    owner_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45), nullable=False)
    last_name = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), nullable=False)
    phone_number = db.Column(db.String(45), nullable=False)

    def __repr__(self) -> str:
        return f"Owner(owner_id={self.owner_id}, first_name='{self.first_name}', " \
               f"last_name='{self.last_name}', email='{self.email}', phone_number='{self.phone_number}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'owner_id': self.owner_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone_number': self.phone_number,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Owner:
        owner = Owner(
            first_name=dto_dict.get('first_name'),
            last_name=dto_dict.get('last_name'),
            email=dto_dict.get('email'),
            phone_number=dto_dict.get('phone_number'),
        )
        return owner
