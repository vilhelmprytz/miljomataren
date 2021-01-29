from flask import Blueprint

from config import GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET
from models import APIResponse

GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"

auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.route("/login")
def login():
    return APIResponse().serialize()


@auth_blueprint.route("/callback")
def callback():
    return APIResponse().serialize()
