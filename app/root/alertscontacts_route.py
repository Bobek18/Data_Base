from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import alertscontacts_controller, smartwatches_controller
from ..domain.alertcontacts import AlertContact

alertscontacts_bp = Blueprint('league', __name__, url_prefix='/league')

@alertscontacts_bp.route('', methods=['GET'])
def get_all_alertscontacts() -> Response:
    print('root', alertscontacts_controller.find_all())
    return make_response(jsonify(alertscontacts_controller.find_all()), HTTPStatus.OK)

@alertscontacts_bp.route('', methods=['POST'])
def create_alertscontacts() -> Response:
    content = request.get_json()
    league = AlertContact.create_from_dto(content)
    alertscontacts_controller.create(league)
    return make_response(jsonify(league.put_into_dto()), HTTPStatus.CREATED)

@alertscontacts_bp.route('/<int:league_id>', methods=['GET'])
def get_alertscontacts(league_id: int) -> Response:
    # Викликаємо find_by_id через контролер
    return make_response(jsonify(alertscontacts_controller.find_by_id(league_id)), HTTPStatus.OK)

@alertscontacts_bp.route('/<int:league_id>', methods=['PUT'])
def update_alertscontacts(league_id: int) -> Response:
    content = request.get_json()
    league = AlertContact.create_from_dto(content)
    alertscontacts_controller.update(league_id, league)
    return make_response("League updated", HTTPStatus.OK)

@alertscontacts_bp.route('/<int:league_id>', methods=['PATCH'])
def patch_alertscontacts(league_id: int) -> Response:
    content = request.get_json()
    alertscontacts_controller.patch(league_id, content)
    return make_response("League updated", HTTPStatus.OK)

@alertscontacts_bp.route('/<int:league_id>', methods=['DELETE'])
def delete_alertscontacts(league_id: int) -> Response:
    alertscontacts_controller.delete(league_id)
    return make_response("League deleted", HTTPStatus.OK)

# Додаємо новий метод
@alertscontacts_bp.route('/smartwatches', methods=['GET'])
def get_all_alertcontacts_smartwatches() -> Response:
    alert_contacts = alertscontacts_controller.find_all()
    result = []

    for alert_contact in alert_contacts:
        smartwatches = smartwatches_controller.find_by_alert_contact_id(alert_contact['id'])
        result.append({
            'alert_contact': alert_contact,
            'smartwatches': smartwatches
        })

    return make_response(jsonify(result), HTTPStatus.OK)