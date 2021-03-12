from flask import Blueprint, request

from models import APIResponse
from decorators.auth import authenticated
from validation import expect_json
from orm import db, Car


car_blueprint = Blueprint("car", __name__)


@car_blueprint.route("", methods=["POST", "GET"])
@authenticated
def car():
    if request.method == "POST":
        # We expect different parameters dependning on whether the
        # vehicle is leasing or not. Leasing typically has the
        # insurance cost included and may even include service costs.
        # This model is simplified.
        data = expect_json(
            {
                "registration_number": str,
                "fuel_type": str,
                "insurance_cost": int,
                "service_cost": int,
            }
        )

        if expect_json({"leasing": bool})["leasing"]:
            data = {**data, **expect_json({"leasing": bool, "leasing_cost": bool})}

        car = Car(
            registration_number=data["registration_number"],
            fuel_type=data["fuel_type"],
            fuel_consumption=0,  # FIXME!
            leasing=data["leasing"],
            leasing_cost=data["leasing_cost"],
            insurance_cost=data["insurance_cost"],
            service_cost=data["service_cost"],
        )
        db.session.add(car)
        db.session.commit()

    return APIResponse().serialize()


@car_blueprint.route("/<int:id>", methods=["GET", "DELETE", "PUT"])
@authenticated
def car_id(id: int):
    return APIResponse(response={"id": id}).serialize()
