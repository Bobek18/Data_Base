from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import smartwatches_controller
from ..domain.smartwatches import Smartwatch

smartwatches_bp = Blueprint('player', __name__, url_prefix='/player')


@smartwatches_bp.route('', methods=['GET'])
def get_all_players() -> Response:
    return make_response(jsonify(smartwatches_controller.find_all()), HTTPStatus.OK)


@smartwatches_bp.route('', methods=['POST'])
def create_player() -> Response:
    content = request.get_json()
    player = Smartwatch.create_from_dto(content)
    smartwatches_controller.create(player)
    return make_response(jsonify(player.put_into_dto()), HTTPStatus.CREATED)


@smartwatches_bp.route('/<int:player_id>', methods=['GET'])
def get_player(player_id: int) -> Response:
    return make_response(jsonify(smartwatches_controller.find_by_id(player_id)), HTTPStatus.OK)


@smartwatches_bp.route('/<int:player_id>', methods=['PUT'])
def update_player(player_id: int) -> Response:
    content = request.get_json()
    player = Smartwatch.create_from_dto(content)
    smartwatches_controller.update(player_id, player)
    return make_response("Player updated", HTTPStatus.OK)


@smartwatches_bp.route('/<int:player_id>', methods=['PATCH'])
def patch_player(player_id: int) -> Response:
    content = request.get_json()
    smartwatches_controller.patch(player_id, content)
    return make_response("Player updated", HTTPStatus.OK)


@smartwatches_bp.route('/<int:player_id>', methods=['DELETE'])
def delete_player(player_id: int) -> Response:
    smartwatches_controller.delete(player_id)
    return make_response("Player deleted", HTTPStatus.OK)
