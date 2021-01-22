from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(320), unique=True, nullable=False)


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    registration_number = db.Column(db.String(6), unique=True, nullable=False)
    fuel_type = db.Column(db.String(6), nullable=False)
    fuel_consumption = db.Column(db.Float, nullable=False)
    leasing = db.Column(db.Boolean, nullable=False)
    leasing_cost = db.Column(db.Integer, nullable=True)
    insurance_cost = db.Column(db.Integer, nullable=True)
    service_cost = db.Column(db.Integer, nullable=True)

    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    owner = db.relationship("Car", backref=db.backref("cars", lazy=True))

    time_created = db.Column(db.DateTime, server_default=func.now())
    time_updated = db.Column(
        db.DateTime, server_default=func.now(), onupdate=func.now()
    )


class Trip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Boolean, nullable=False)

    trip_started = db.Column(db.DateTime, server_default=func.now())
    trip_ended = db.Column(db.DateTime, nullable=True)

    car_id = db.Column(db.Integer, db.ForeignKey("car.id"), nullable=False)
    car = db.relationship("Car", backref=db.backref("trips", lazy=True))

    time_updated = db.Column(
        db.DateTime, server_default=func.now(), onupdate=func.now()
    )


class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lon = db.Column(db.Float, nullable=False)
    lat = db.Column(db.Float, nullable=False)

    trip_id = db.Column(db.Integer, db.ForeignKey("trip.id"), nullable=False)
    trip = db.relationship("Car", backref=db.backref("positions", lazy=True))

    time_created = db.Column(db.DateTime, server_default=func.now())
    time_updated = db.Column(
        db.DateTime, server_default=func.now(), onupdate=func.now()
    )
