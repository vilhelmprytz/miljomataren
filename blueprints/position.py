from flask import Blueprint

from models import APIResponse
from decorators.auth import authenticated


position_blueprint = Blueprint("position", __name__)


@position_blueprint.route("/", methods=["POST", "GET"])
@authenticated
def position():
    return APIResponse().serialize()


@position_blueprint.route("/<int:id>", methods=["GET", "DELETE", "PUT"])
@authenticated
def position_id(id: int):
    return APIResponse(response={"id": id}).serialize()
