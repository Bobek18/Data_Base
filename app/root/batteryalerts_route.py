from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import batteryalerts_controller
from ..domain.batteryalerts import BatteryAlert

batteryalerts_bp = Blueprint('stadium', __name__, url_prefix='/stadium')


@batteryalerts_bp.route('', methods=['GET'])
def get_all_stadiums() -> Response:
    return make_response(jsonify(batteryalerts_controller.find_all()), HTTPStatus.OK)


@batteryalerts_bp.route('', methods=['POST'])
def create_stadium() -> Response:
    content = request.get_json()
    stadium = BatteryAlert.create_from_dto(content)
    batteryalerts_controller.create(stadium)
    return make_response(jsonify(stadium.put_into_dto()), HTTPStatus.CREATED)


@batteryalerts_bp.route('/<int:stadium_id>', methods=['GET'])
def get_stadium(stadium_id: int) -> Response:
    return make_response(jsonify(batteryalerts_controller.find_by_id(stadium_id)), HTTPStatus.OK)


@batteryalerts_bp.route('/<int:stadium_id>', methods=['PUT'])
def update_stadium(stadium_id: int) -> Response:
    content = request.get_json()
    stadium = BatteryAlert.create_from_dto(content)
    batteryalerts_controller.update(stadium_id, stadium)
    return make_response("Stadium updated", HTTPStatus.OK)


@batteryalerts_bp.route('/<int:stadium_id>', methods=['PATCH'])
def patch_stadium(stadium_id: int) -> Response:
    content = request.get_json()
    batteryalerts_controller.patch(stadium_id, content)
    return make_response("Stadium updated", HTTPStatus.OK)


@batteryalerts_bp.route('/<int:stadium_id>', methods=['DELETE'])
def delete_stadium(stadium_id: int) -> Response:
    batteryalerts_controller.delete(stadium_id)
    return make_response("Stadium deleted", HTTPStatus.OK)
