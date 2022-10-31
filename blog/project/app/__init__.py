from flask import Flask
from flask_assets import Environment, Bundle
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from config import Config


db = SQLAlchemy()


def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)
    
    db.init_app(app)
    assets = Environment(app)
    assets.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    with app.app_context():
        from .assets import compile_assets
        from .home import home
        from .resources import resources

        app.register_blueprint(home.home_bp)
        app.register_blueprint(resources.resources_bp)
        compile_assets(assets)
        return app
