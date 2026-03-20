
import os
from flask import Flask
from . import db

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'negozio.sqlite'),
    )
    os.makedirs(app.instance_path, exist_ok=True)
    db.init_app(app)
    from .main import bp
    app.register_blueprint(bp)
    return app