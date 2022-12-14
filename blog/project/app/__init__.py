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

    assets = Environment()
    assets.init_app(app)

    
    with app.app_context():
        from .assets import compile_assets
        from .home import home
        from .resources import resources
        from .auth import auth
        from .posts import posts

        db.create_all()
        app.register_blueprint(home.home_bp)
        app.register_blueprint(resources.resources_bp)
        app.register_blueprint(auth.auth_bp)
        app.register_blueprint(posts.posts_bp)
        compile_assets(assets)
        return app
