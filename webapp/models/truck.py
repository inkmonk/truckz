from .core import db

class Truck(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('truck_owner.id'))
    truck_model_id = db.Column(db.Integer, db.ForeignKey('truck_model.id'))
    registration_number = db.Column(db.Unicode(50))
    max_weight_in_kg = db.Column(db.Numeric(precision=8, scale=2))
    capacity_in_cubic_meters = db.Column(db.Numeric(precision=8, scale=2))

    owner = db.relationship("TruckOwner")
    truck_model = db.relationship("TruckModel")
