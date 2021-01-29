from flask import Blueprint

from models import APIResponse
from decorators.auth import authenticated


trip_blueprint = Blueprint("trip", __name__)


@trip_blueprint.route("/", methods=["POST", "GET"])
@authenticated
def trip():
    return APIResponse().serialize()


@trip_blueprint.route("/<int:id>", methods=["GET", "DELETE", "PUT"])
@authenticated
def trip_id(id: int):
    return APIResponse(response={"id": id}).serialize()
