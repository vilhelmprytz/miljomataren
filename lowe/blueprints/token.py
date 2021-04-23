from flask import Blueprint, request, session, abort

from models import APIResponse
from decorators.auth import authenticated
from core import random_secret
from orm import db, Token


token_blueprint = Blueprint("token", __name__)


@token_blueprint.route("", methods=["POST", "GET"])
@authenticated
def token_index():
    user = session.get("user")

    if request.method == "POST":
        token = Token(user_id=user["id"], token=random_secret(50))
        db.session.add(token)
        db.session.commit()

        return APIResponse(response=token).serialize()

    tokens = Token.query.filter_by(user_id=user["id"]).all()

    return APIResponse(response=tokens).serialize()


@token_blueprint.route("/<int:id>", methods=["GET", "DELETE", "PUT"])
@authenticated
def token_id(id: int):
    # FIXME: ability to edit details with PUT

    user = session.get("user")
    token = Token.query.filter_by(id=id, user_id=user["id"]).first()

    if token is None:
        abort(404, "No token with that id found")

    if request.method == "DELETE":
        db.session.delete(token)
        db.session.commit()

        return APIResponse().serialize()

    return APIResponse(response=token).serialize()
