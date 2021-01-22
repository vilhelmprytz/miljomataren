#!/usr/bin/env python

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import environ
from orm import db

app = Flask(__name__)

# environment variables
DATABASE_USERNAME = environ.get("DATABASE_USERNAME", "miljomataren")
DATABASE_NAME = environ.get("DATABASE_NAME", "miljomataren")
DATABASE_PASSWORD = environ.get("DATABASE_PASSWORD", "password")
DATABASE_HOST = environ.get("DATABASE_HOST", "127.0.0.1")

# config
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# init db
db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
