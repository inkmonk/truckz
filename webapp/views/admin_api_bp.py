from flask.ext.security import login_required, current_user
from flask import Blueprint, abort
from flask_sqlalchemy_booster.responses import as_processed_list, as_obj
from ..models import TruckModel, Truck, TruckOwner, User


admin_api_bp = Blueprint('admin_api_bp', __name__)


@admin_api_bp.before_request
def restrict_bp_to_admins():
    if not current_user.has_role('admin'):
        abort(403)


@admin_api_bp.route("/trucks")
@as_processed_list
def list_trucks():
    """
    GET /admin-api/v1/trucks
    """
    return Truck


@admin_api_bp.route("/trucks/<int:truck_id>")
@as_obj
def get_truck(truck_id):
    """
    GET /admin-api/v1/trucks/12
    """
    return Truck.get(truck_id)


@admin_api_bp.route("/truck-models")
@as_processed_list
def list_truck_models():
    """
    GET /admin-api/v1/truck-models
    """
    return TruckModel


@admin_api_bp.route("/truck-models/<int:truck_model_id>")
@as_obj
def get_truck_model(truck_model_id):
    """
    GET /admin-api/v1/truck-models/12
    """
    return TruckModel.get(truck_model_id)


@admin_api_bp.route("/users")
@as_processed_list
def list_users():
    """
    GET /admin-api/v1/users
    """
    return User


@admin_api_bp.route("/users/<int:user_id>")
@as_obj
def get_user(user_id):
    """
    GET /admin-api/v1/user/12
    """
    return User.get(user_id)


@admin_api_bp.route("/truck-owners")
@as_processed_list
def list_truck_owners():
    """
    GET /admin-api/v1/truck-owners
    """
    return TruckOwner


@admin_api_bp.route("/truck-owners/<int:truck_owner_id>")
@as_obj
def get_truck_owner(truck_owner_id):
    """
    GET /admin-api/v1/truck-owners/12
    """
    return TruckOwner.get(truck_owner_id)
