from .core import db

class TruckOperator(db.Model):

    _autogenerate_dict_struct_if_none_ = True

    id = db.Column(db.Integer, primary_key=True, unique=True)
    company_name = db.Column(db.Unicode(100), unique=True)
    city = db.Column(db.Unicode(100), unique=True)

    employees = db.relationship("User")