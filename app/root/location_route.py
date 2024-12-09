from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import location_controller, smartwatches_controller
from ..domain.smartwatches import Smartwatch

location_bp = Blueprint('match', __name__, url_prefix='/match')


@location_bp.route('', methods=['GET'])
def get_all_matches() -> Response:
    return make_response(jsonify(smartwatches_controller.find_all()), HTTPStatus.OK)


@location_bp.route('', methods=['POST'])
def create_match() -> Response:
    content = request.get_json()
    match = Smartwatch.create_from_dto(content)
    smartwatches_controller.create(match)
    return make_response(jsonify(match.put_into_dto()), HTTPStatus.CREATED)


@location_bp.route('/<int:location_id>', methods=['GET'])
def get_match(match_id: int) -> Response:
    return make_response(jsonify(smartwatches_controller.find_by_id(match_id)), HTTPStatus.OK)


@location_bp.route('/<int:location_id>', methods=['PUT'])
def update_match(match_id: int) -> Response:
    content = request.get_json()
    match = Smartwatch.create_from_dto(content)
    smartwatches_controller.update(match_id, match)
    return make_response("location updated", HTTPStatus.OK)


@location_bp.route('/<int:location_id>', methods=['PATCH'])
def patch_match(match_id: int) -> Response:
    content = request.get_json()
    smartwatches_controller.patch(match_id, content)
    return make_response("location updated", HTTPStatus.OK)


@location_bp.route('/<int:location_id>', methods=['DELETE'])
def delete_match(match_id: int) -> Response:
    smartwatches_controller.delete(match_id)
    return make_response("location deleted", HTTPStatus.OK)
