from flask import request, abort


def expect_json(keys: dict):
    if request.json == None:
        abort(400, "Request is not valid JSON")
    for k, v in keys.items():
        if k not in request.json:
            abort(400, f"No key {k}")
        if type(request.json[k]) != v:
            abort(400, f"Key {k} is not of type {v}")
    return request.json
