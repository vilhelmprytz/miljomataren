from functools import wraps
from flask import session, abort


def authenticated(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("authenticated"):
            abort(401, "Not authenticated")

        return f(*args, **kwargs)

    return decorated_function
