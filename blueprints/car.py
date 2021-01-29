from flask import Blueprint

from models import APIResponse
from decorators.auth import authenticated


car_blueprint = Blueprint("car", __name__)


@car_blueprint.route("/", methods=["POST", "GET"])
@authenticated
def car():
    return APIResponse().serialize()


@car_blueprint.route("/<int:id>", methods=["GET", "DELETE", "PUT"])
@authenticated
def car_id(id: int):
    return APIResponse(response={"id": id}).serialize()
