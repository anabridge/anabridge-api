from flask import Flask
import logging
import os
from flask_cors import CORS
from config import app_config
from dotenv import load_dotenv
load_dotenv


def create_app(environment):
    app = Flask(__name__)
    app.config.from_object(app_config[environment])

    CORS(app)

    # importing blue prints

    from controllers.transform import transform_bp

    # register the blueprints
    app.register_blueprint(transform_bp)

    return app


application = create_app(os.getenv("FLASK_ENV"))

if __name__ == '__main__':
    application.run(debug=True)
