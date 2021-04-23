from functools import wraps
from datetime import datetime
from flask import session

from orm import db, Trip, Position


def deactive_stale_trips(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = session.get("user")

        # iterate over all the user trips
        for trip in Trip.query.filter_by(user_id=user["id"], active=True).all():
            # get all positions for trip
            positions = Position.query.filter_by(trip_id=trip.id).all()

            t1 = datetime.now()
            t2 = (
                trip.trip_started if len(positions) == 0 else positions[-1].time_created
            )

            diff = (t1 - t2).seconds

            # trips that have no new GPS data for more than 60 seconds are considered inactive
            if diff > 60:
                trip.active = False
                # trip end time will be last registered position, if any
                # otherwise it will be current time
                trip.trip_ended = (
                    datetime.now()
                    if len(positions) == 0
                    else positions[-1].time_created
                )

                db.session.add(trip)
                db.session.commit()

        return f(*args, **kwargs)

    return decorated_function
