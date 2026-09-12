from flask import Flask

from .config import Config
from .extensions import db


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)


    with app.app_context():

        from . import models

        db.create_all()


    from .routes.main import main_bp
    from .routes.api import api_bp
    from .routes.security import security_bp
    from .routes.report import report_bp


    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(security_bp)
    app.register_blueprint(report_bp)


    return app
