#!/usr/bin/env python

__author__ = "Vilhelm Prytz"
__email__ = "vilhelm@prytznet.se"

import sys
from pathlib import Path

# add parent folder
sys.path.append(str(Path(__file__).parent.parent.absolute()))

from app import db, app  # noqa: E402
from orm import User  # noqa: E402

email = input("Enter email: ")

user = User(email=email)

with app.app_context():
    db.session.add(user)
    db.session.commit()
