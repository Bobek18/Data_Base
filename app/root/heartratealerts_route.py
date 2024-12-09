from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import heartratealerts_controller
from ..domain.heartratesalerts import HeartRateAlert

heartratealerts_bp = Blueprint('referee', __name__, url_prefix='/referee')


@heartratealerts_bp.get('')
def get_all_referees() -> Response:
    return make_response(jsonify(heartratealerts_bp.find_all()), HTTPStatus.OK)


@heartratealerts_bp.post('')
def create_referee() -> Response:
    content = request.get_json()
    referee = HeartRateAlert.create_from_dto(content)
    heartratealerts_bp.create(referee)
    return make_response(jsonify(referee.put_into_dto()), HTTPStatus.CREATED)


@heartratealerts_bp.get('/<int:referee_id>')
def get_referee(referee_id: int) -> Response:
    return make_response(jsonify(heartratealerts_bp.find_by_id(referee_id)), HTTPStatus.OK)


@heartratealerts_bp.put('/<int:referee_id>')
def update_referee(referee_id: int) -> Response:
    content = request.get_json()
    referee = HeartRateAlert.create_from_dto(content)
    heartratealerts_bp.update(referee_id, referee)
    return make_response("Referee updated", HTTPStatus.OK)


@heartratealerts_bp.patch('/<int:referee_id>')
def patch_referee(referee_id: int) -> Response:
    content = request.get_json()
    heartratealerts_bp.patch(referee_id, content)
    return make_response("Referee updated", HTTPStatus.OK)


@heartratealerts_bp.delete('/<int:referee_id>')
def delete_referee(referee_id: int) -> Response:
    heartratealerts_bp.delete(referee_id)
    return make_response("Referee deleted", HTTPStatus.OK)
