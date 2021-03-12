from flask import Blueprint, session

from models import APIResponse
from decorators.auth import authenticated

user_blueprint = Blueprint("user", __name__)


@user_blueprint.route("", methods=["POST", "GET"])
@authenticated
def user():
    user = session.get("user")

    return APIResponse(response=user).serialize()


@user_blueprint.route("/<int:id>", methods=["GET", "DELETE", "PUT"])
@authenticated
def user_id(id: int):
    return APIResponse(response={"id": id}).serialize()
