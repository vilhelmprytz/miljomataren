from functools import wraps
from flask import session, abort, request
from orm import Token, User


def authenticated(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth = False
        if "authorization" in request.headers:
            tokens = Token.query.filter_by(token=request.headers["authorization"]).all()
            if len(tokens) != 0:
                token = tokens[0]
                auth = True

                user = User.query.filter_by(id=token.user_id)
                if len(user.all()) == 0:
                    abort(401, "User does not exist")
                user = user.first()

                user = {
                    "id": user.id,
                    "email": user.email,
                    "picture": "",
                    "name": "",
                }

                session["user"] = user

        if session.get("authenticated"):
            auth = True

        if not auth:
            abort(401, "Not authenticated")

        return f(*args, **kwargs)

    return decorated_function
