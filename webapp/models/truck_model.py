from .core import db


class TruckModel(db.Model):

    _autogenerate_dict_struct_if_none_ = True
    id = db.Column(db.Integer, primary_key=True, unique=True)
    company_name = db.Column(db.Unicode(100))
    model_name = db.Column(db.Unicode(100))
    max_weight_in_kg = db.Column(db.Numeric(precision=8, scale=2))
    capacity_in_cubic_meters = db.Column(db.Numeric(precision=8, scale=2))
