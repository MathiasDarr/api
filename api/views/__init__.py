from api.views.api import api
from api.views.base_api import blueprint as base_api

def mount_app_blueprints(app):
    app.register_blueprint(api)
    app.register_blueprint(base_api)
