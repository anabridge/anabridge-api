from flask import Blueprint, jsonify
import app
import logging
from routes import api

transform_bp = Blueprint('device_status', __name__)


@transform_bp.route(api.route['transform'], methods=['GET'])
def transform():
    pass
