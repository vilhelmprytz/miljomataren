from flask import Blueprint, request, session, abort

from models import APIResponse
from decorators.auth import authenticated
from orm import db, Trip, Car
from validation import expect_json


trip_blueprint = Blueprint("trip", __name__)


@trip_blueprint.route("", methods=["POST", "GET"])
@authenticated
def trip():
    user = session.get("user")

    if request.method == "POST":
        data = expect_json({"car_id": int})

        car = Car.query.filter_by(id=data["car_id"], user_id=user["id"]).all()
        if len(car) == 0:
            abort(400, "You user does not have access to any car with that id")

        trip = Trip(active=True, car_id=car.id, user_id=user["id"])
        db.session.add(trip)
        db.session.commit()

        return APIResponse().serialize()

    trips = Trip.query.filter_by(user_id=user["id"]).all()

    return APIResponse(response=trips).serialize()


@trip_blueprint.route("/<int:id>", methods=["GET", "DELETE", "PUT"])
@authenticated
def trip_id(id: int):
    user = session.get("user")
    trip = Trip.query.filter_by(id=id, user_id=user["id"]).all()

    if len(trip) != 1:
        abort(404, "No trip with that id found")

    return APIResponse(response=trip[0]).serialize()
