from flask import Blueprint, request, session, abort

from models import APIResponse
from orm import db, Trip, Car, Position
from validation import expect_json
from core import car_statistics

from decorators.auth import authenticated
from decorators.trip import deactive_stale_trips

trip_blueprint = Blueprint("trip", __name__)


@trip_blueprint.route("", methods=["POST", "GET"])
@authenticated
@deactive_stale_trips
def trip():
    user = session.get("user")

    if request.method == "POST":
        data = expect_json({"car_id": int})

        car = Car.query.filter_by(id=data["car_id"], user_id=user["id"]).first()
        if car is None:
            abort(400, "Your user does not have access to any car with that id")

        trip = Trip(active=True, car_id=car.id, user_id=user["id"])
        db.session.add(trip)
        db.session.commit()

        return APIResponse(response=trip).serialize()

    trips = Trip.query.filter_by(user_id=user["id"]).all()

    return APIResponse(response=trips).serialize()


@trip_blueprint.route("/<int:id>", methods=["GET", "DELETE", "PUT"])
@authenticated
@deactive_stale_trips
def trip_id(id: int):
    user = session.get("user")
    trip = Trip.query.filter_by(id=id, user_id=user["id"]).first()

    if trip is None:
        abort(404, "No trip with that id found")

    # get all positions
    positions = Position.query.filter_by(trip_id=id).all()

    # get the current car
    car = Car.query.filter_by(id=trip.car_id).first()

    statistics = car_statistics(car, positions)

    return APIResponse(
        response={
            "id": trip.id,
            "active": trip.active,
            "trip_started": trip.trip_started,
            "trip_ended": trip.trip_ended,
            "positions": positions,
            "car_id": trip.car_id,
            "user_id": trip.user_id,
            "time_updated": trip.time_updated,
            "statistics": statistics,
        }
    ).serialize()
