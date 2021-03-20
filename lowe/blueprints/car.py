from flask import Blueprint, request, session, abort

from models import APIResponse
from decorators.auth import authenticated
from validation import expect_json
from orm import db, Car


car_blueprint = Blueprint("car", __name__)


@car_blueprint.route("", methods=["POST", "GET"])
@authenticated
def car():
    user = session.get("user")

    if request.method == "POST":
        # We expect different parameters dependning on whether the
        # vehicle is leasing or not. Leasing typically has the
        # insurance cost included and may even include service costs.
        # This model is simplified.
        data = expect_json(
            {
                "registration_number": str,
                "fuel_type": str,
                "fuel_consumption": float,
                "co2_emissions": float,
                "insurance_cost": int,  # yearly
                "service_cost": int,  # yearly average
                "annual_mileage": float,  # yearly average
            }
        )

        if expect_json({"leasing": bool})["leasing"]:
            data = {**data, **expect_json({"leasing": bool, "leasing_cost": bool})}

        car = Car(
            registration_number=data["registration_number"],
            fuel_type=data["fuel_type"],
            fuel_consumption=data["fuel_consumption"],
            co2_emissions=data["co2_emissions"],
            leasing=data["leasing"],
            leasing_cost=data["leasing_cost"] if data["leasing"] else 0,
            insurance_cost=data["insurance_cost"],
            service_cost=data["service_cost"],
            annual_mileage=data["annual_mileage"],
            user_id=user["id"],
        )
        db.session.add(car)
        db.session.commit()

        return APIResponse(response=car).serialize()

    cars = Car.query.filter_by(user_id=user["id"]).all()

    return APIResponse(response=cars).serialize()


@car_blueprint.route("/<int:id>", methods=["GET", "DELETE", "PUT"])
@authenticated
def car_id(id: int):
    # FIXME: ability to edit details with PUT

    user = session.get("user")
    car = Car.query.filter_by(id=id, user_id=user["id"]).first()

    if car is None:
        abort(404, "No car with that id found")

    if request.method == "DELETE":
        db.session.delete(car)
        db.session.commit()

        return APIResponse().serialize()

    return APIResponse(response=car).serialize()
