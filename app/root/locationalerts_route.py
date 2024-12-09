from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import locationalerts_controller
from ..domain.locatoinalerts import LocationAlert

locationalerts_bp = Blueprint('match_stat', __name__, url_prefix='/match_stat')


@locationalerts_bp.route('', methods=['GET'])
def get_all_match_stats() -> Response:
    return make_response(jsonify(locationalerts_controller.find_all()), HTTPStatus.OK)


@locationalerts_bp.route('', methods=['POST'])
def create_match_stat() -> Response:
    content = request.get_json()
    match_stat = LocationAlert.create_from_dto(content)
    locationalerts_bp.create(match_stat)
    return make_response(jsonify(match_stat.put_into_dto()), HTTPStatus.CREATED)


@locationalerts_bp.route('/<int:match_stat_id>', methods=['GET'])
def get_match_stat(match_stat_id: int) -> Response:
    return make_response(jsonify(locationalerts_controller.find_by_id(match_stat_id)), HTTPStatus.OK)


@locationalerts_bp.route('/<int:match_stat_id>', methods=['PUT'])
def update_match_stat(match_stat_id: int) -> Response:
    content = request.get_json()
    match_stat = LocationAlert.create_from_dto(content)
    locationalerts_controller.update(match_stat_id, match_stat)
    return make_response("MatchStat updated", HTTPStatus.OK)


@locationalerts_bp.route('/<int:match_stat_id>', methods=['PATCH'])
def patch_match_stat(match_stat_id: int) -> Response:
    content = request.get_json()
    locationalerts_controller.patch(match_stat_id, content)
    return make_response("MatchStat updated", HTTPStatus.OK)


@locationalerts_bp.route('/<int:match_stat_id>', methods=['DELETE'])
def delete_match_stat(match_stat_id: int) -> Response:
    locationalerts_controller.delete(match_stat_id)
    return make_response("MatchStat deleted", HTTPStatus.OK)
