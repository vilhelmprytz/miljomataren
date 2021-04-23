from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()


@dataclass
class User(db.Model):
    # a table cannot be named "user" (default value) in PostgreSQL
    __tablename__ = "users"

    id: int = db.Column(db.Integer, primary_key=True)
    email: str = db.Column(db.String(320), unique=True, nullable=False)
    cars = db.relationship("Car", backref="user", lazy=True)
    trips = db.relationship("Trip", backref="user", lazy=True)

    time_created: db.DateTime = db.Column(db.DateTime, server_default=func.now())
    time_updated: db.DateTime = db.Column(
        db.DateTime, server_default=func.now(), onupdate=func.now()
    )


@dataclass
class Car(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    registration_number: str = db.Column(db.String(6), unique=True, nullable=False)
    fuel_type: str = db.Column(db.String(6), nullable=False)
    fuel_consumption: float = db.Column(db.Float, nullable=False)  # l/100km
    co2_emissions: float = db.Column(db.Float, nullable=False)  # g/km
    leasing: bool = db.Column(db.Boolean, nullable=False)
    leasing_cost: int = db.Column(db.Integer, nullable=True)  # yearly
    insurance_cost: int = db.Column(db.Integer, nullable=False)  # yearly
    service_cost: int = db.Column(db.Integer, nullable=False)  # yearly
    annual_mileage: float = db.Column(db.Float, nullable=False)  # yearly, km

    trips = db.relationship("Trip", backref="car", lazy=True)
    user_id: int = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    time_created: db.DateTime = db.Column(db.DateTime, server_default=func.now())
    time_updated: db.DateTime = db.Column(
        db.DateTime, server_default=func.now(), onupdate=func.now()
    )


@dataclass
class Trip(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    active: bool = db.Column(db.Boolean, nullable=False)

    trip_started: db.DateTime = db.Column(db.DateTime, server_default=func.now())
    trip_ended: db.DateTime = db.Column(db.DateTime, nullable=True)

    positions = db.relationship("Position", backref=db.backref("trip", lazy=True))
    car_id: int = db.Column(db.Integer, db.ForeignKey("car.id"), nullable=False)
    user_id: int = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    time_updated: db.DateTime = db.Column(
        db.DateTime, server_default=func.now(), onupdate=func.now()
    )


@dataclass
class Position(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    lat: float = db.Column(db.Float, nullable=False)
    lon: float = db.Column(db.Float, nullable=False)

    trip_id: int = db.Column(db.Integer, db.ForeignKey("trip.id"), nullable=False)
    user_id: int = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    time_created: db.DateTime = db.Column(db.DateTime, server_default=func.now())
    time_updated: db.DateTime = db.Column(
        db.DateTime, server_default=func.now(), onupdate=func.now()
    )


@dataclass
class Token(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    user_id: int = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    token: str = db.Column(db.String(50), unique=True, nullable=False)

    time_created: db.DateTime = db.Column(db.DateTime, server_default=func.now())
    time_updated: db.DateTime = db.Column(
        db.DateTime, server_default=func.now(), onupdate=func.now()
    )
