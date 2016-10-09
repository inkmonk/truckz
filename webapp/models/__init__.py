from .core import db

from flask.ext.security import SQLAlchemyUserDatastore

from .user import User, Role
from .truck_operator import TruckOperator
from .truck_model import TruckModel
from .truck import Truck


user_datastore = SQLAlchemyUserDatastore(db, User, Role)
