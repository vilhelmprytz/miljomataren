#!/usr/bin/env python

from flask import Flask
from werkzeug.exceptions import HTTPException
from json import dumps
from flask_session import Session
from redis import Redis
from datetime import timedelta

from orm import db
from models import APIResponse
from config import (
    DATABASE_USERNAME,
    DATABASE_NAME,
    DATABASE_PASSWORD,
    DATABASE_HOST,
    REDIS_HOST,
)

from blueprints.auth import auth_blueprint
from blueprints.car import car_blueprint
from blueprints.position import position_blueprint
from blueprints.trip import trip_blueprint
from blueprints.user import user_blueprint
from blueprints.token import token_blueprint

app = Flask(__name__)

# config
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SESSION_TYPE"] = "redis"
app.config["SESSION_REDIS"] = Redis(host=REDIS_HOST, db=0)
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(hours=24)

# init db
db.init_app(app)

with app.app_context():
    db.create_all()

# redis session
Session(app)


# all error pages are now JSON instead of HTML
@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()

    response.data = dumps(
        APIResponse(
            code=e.code, name=e.name, description=e.description, response={}
        ).__dict__
    )

    response.content_type = "application/json"
    return response, e.code


# register blueprints
app.register_blueprint(auth_blueprint, url_prefix="/api/auth")
app.register_blueprint(car_blueprint, url_prefix="/api/car")
app.register_blueprint(position_blueprint, url_prefix="/api/position")
app.register_blueprint(trip_blueprint, url_prefix="/api/trip")
app.register_blueprint(user_blueprint, url_prefix="/api/user")
app.register_blueprint(token_blueprint, url_prefix="/api/token")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
