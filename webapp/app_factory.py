from flask import Flask
from .views import admin_api_bp
from .models import db, user_datastore
from .core import security
import template_filters
from .forms import LoginForm


def create_app(database=db):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('webapp.config')
    app.config.from_pyfile('application.cfg.py')
    database.init_app(app)

    security.init_app(
        app, user_datastore)

    app.register_blueprint(admin_api_bp, url_prefix='/admin-api/v1')
    app.jinja_env.filters['timestampize'] = template_filters.timestampize
    app.jinja_env.filters['hash_hmac'] = template_filters.hash_hmac
    app.jinja_env.filters['json'] = template_filters.json_dumps
    app.jinja_env.filters['todict'] = template_filters.todict
    return app
