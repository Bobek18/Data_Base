from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import heartrates_controller
from ..domain.heartrates import HeartRate

heartrates_bp = Blueprint('player_has_start_lineup', __name__, url_prefix='/player_has_start_lineup')


@heartrates_bp.route('', methods=['GET'])
def get_all_player_has_start_lineups() -> Response:
    return make_response(jsonify(heartrates_controller.find_all()), HTTPStatus.OK)


@heartrates_bp.route('', methods=['POST'])
def create_player_has_start_lineup() -> Response:
    content = request.get_json()
    player_has_start_lineup = HeartRate.create_from_dto(content)
    heartrates_controller.create(player_has_start_lineup)
    return make_response(jsonify(player_has_start_lineup.put_into_dto()), HTTPStatus.CREATED)


@heartrates_bp.route('/<int:player_has_start_lineup_id>', methods=['GET'])
def get_player_has_start_lineup(player_has_start_lineup_id: int) -> Response:
    return make_response(jsonify(heartrates_controller.find_by_id(player_has_start_lineup_id)), HTTPStatus.OK)


@heartrates_bp.route('/<int:player_has_start_lineup_id>', methods=['PUT'])
def update_player_has_start_lineup(player_has_start_lineup_id: int) -> Response:
    content = request.get_json()
    player_has_start_lineup = HeartRate.create_from_dto(content)
    heartrates_controller.update(player_has_start_lineup_id, player_has_start_lineup)
    return make_response("PlayerHasStartLineup updated", HTTPStatus.OK)


@heartrates_bp.route('/<int:player_has_start_lineup_id>', methods=['PATCH'])
def patch_player_has_start_lineup(player_has_start_lineup_id: int) -> Response:
    content = request.get_json()
    heartrates_controller.patch(player_has_start_lineup_id, content)
    return make_response("PlayerHasStartLineup updated", HTTPStatus.OK)


@heartrates_bp.route('/<int:player_has_start_lineup_id>', methods=['DELETE'])
def delete_player_has_start_lineup(player_has_start_lineup_id: int) -> Response:
    heartrates_controller.delete(player_has_start_lineup_id)
    return make_response("PlayerHasStartLineup deleted", HTTPStatus.OK)
