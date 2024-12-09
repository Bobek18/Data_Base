from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import notificationsettings_controller
from ..domain.notificationsettings import NotificationSetting

notificationsettings_bp = Blueprint('referee_has_referee_team', __name__, url_prefix='/referee_has_referee_team')


@notificationsettings_bp.route('', methods=['GET'])
def get_all_referee_has_referee_teams() -> Response:
    return make_response(jsonify(notificationsettings_controller.find_all()), HTTPStatus.OK)


@notificationsettings_bp.route('', methods=['POST'])
def create_referee_has_referee_team() -> Response:
    content = request.get_json()
    referee_has_referee_team = NotificationSetting.create_from_dto(content)
    notificationsettings_controller.create(referee_has_referee_team)
    return make_response(jsonify(referee_has_referee_team.put_into_dto()), HTTPStatus.CREATED)


@notificationsettings_bp.route('/<int:referee_has_referee_team_id>', methods=['GET'])
def get_referee_has_referee_team(referee_has_referee_team_id: int) -> Response:
    return make_response(jsonify(notificationsettings_controller.find_by_id(referee_has_referee_team_id)), HTTPStatus.OK)


@notificationsettings_bp.route('/<int:referee_has_referee_team_id>', methods=['PUT'])
def update_referee_has_referee_team(referee_has_referee_team_id: int) -> Response:
    content = request.get_json()
    referee_has_referee_team = NotificationSetting.create_from_dto(content)
    notificationsettings_controller.update(referee_has_referee_team_id, referee_has_referee_team)
    return make_response("RefereeHasRefereeTeam updated", HTTPStatus.OK)


@notificationsettings_bp.route('/<int:referee_has_referee_team_id>', methods=['PATCH'])
def patch_referee_has_referee_team(referee_has_referee_team_id: int) -> Response:
    content = request.get_json()
    notificationsettings_controller.patch(referee_has_referee_team_id, content)
    return make_response("RefereeHasRefereeTeam updated", HTTPStatus.OK)


@notificationsettings_bp.route('/<int:referee_has_referee_team_id>', methods=['DELETE'])
def delete_referee_has_referee_team(referee_has_referee_team_id: int) -> Response:
    notificationsettings_controller.delete(referee_has_referee_team_id)
    return make_response("RefereeHasRefereeTeam deleted", HTTPStatus.OK)
