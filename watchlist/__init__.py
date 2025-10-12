from flask import Flask
from sqlalchemy import select

from watchlist.settings import config
from watchlist.blueprints.main import main_bp
from watchlist.blueprints.auth import auth_bp
from watchlist.models import User
from watchlist.extensions import db, login_manager
from watchlist.errors import register_errors
from watchlist.commands import register_commands


def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    db.init_app(app)
    login_manager.init_app(app)

    register_errors(app)
    register_commands(app)

    @app.context_processor
    def inject_user():
        user = db.session.execute(select(User)).scalar()
        return dict(user=user)

    return app
