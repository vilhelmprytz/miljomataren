#!/usr/bin/env python

from flask import Flask
from werkzeug.exceptions import HTTPException
from json import dumps

from orm import db
from models import APIResponse

# environment variables
from config import DATABASE_USERNAME, DATABASE_NAME, DATABASE_PASSWORD, DATABASE_HOST

app = Flask(__name__)

# config
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# init db
db.init_app(app)

with app.app_context():
    db.create_all()


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


if __name__ == "__main__":
    app.run(host="0.0.0.0")
