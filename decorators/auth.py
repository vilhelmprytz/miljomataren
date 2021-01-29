from functools import wraps


def authenticated(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # do authentication validation here
        # fixme
        return f(*args, **kwargs)

    return decorated_function
