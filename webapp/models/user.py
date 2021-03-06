from flask.ext.security import UserMixin, RoleMixin
from .core import db


class Role(db.Model, RoleMixin):

    __tablename__ = 'role'

    _autogenerate_dict_struct_if_none_ = True

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(30), unique=True)
    description = db.Column(db.String(200))

    def __init__(self, name=None, description=None):
        self.name = name
        self.description = description


role_user = db.Table(
    'role_user',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class User(db.Model, UserMixin):

    __tablename__ = 'user'

    _autogenerate_dict_struct_if_none_ = True

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.Unicode(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    active = db.Column(db.Boolean())
    roles = db.relationship(
        'Role', secondary=role_user,
        backref=db.backref('users', lazy='dynamic'))
    employing_truck_operator_id = db.Column(
        db.Integer, db.ForeignKey('truck_operator.id'))

    employing_truck_operator = db.relationship("TruckOperator")

