from flask import Blueprint, session, request, abort

from models import APIResponse
from decorators.auth import authenticated
from validation import expect_json
from orm import Trip, Position, Car, db
from core import car_statistics, read_fuel_prices


position_blueprint = Blueprint("position", __name__)


@position_blueprint.route("", methods=["POST", "GET"])
@authenticated
def position():
    user = session.get("user")

    if request.method == "POST":
        data = expect_json({"trip_id": int, "lat": float, "lon": float})

        trip = Trip.query.filter_by(id=data["trip_id"], user_id=user["id"]).first()
        if trip is None:
            abort(400, "Your user does not have access to any trip with that id")
        if not trip.active:
            abort(400, "This trip is not active")

        position = Position(
            lat=data["lat"],
            lon=data["lon"],
            trip_id=data["trip_id"],
            user_id=user["id"],
        )
        db.session.add(position)
        db.session.commit()

        # get all positions
        positions = Position.query.filter_by(trip_id=id).all()

        # get the current car
        car = Car.query.filter_by(id=trip.car_id).first()

        statistics = car_statistics(car, positions, read_fuel_prices())

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

    return APIResponse().serialize()


@position_blueprint.route("/<int:id>", methods=["GET"])
@authenticated
def position_id(id: int):
    user = session.get("user")
    position = Position.query.filter_by(id=id, user_id=user["id"]).first()

    if position is None:
        abort(404, "No position with that id found")

    return APIResponse(response=position).serialize()
