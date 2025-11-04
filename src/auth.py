from functools import wraps

from flask import jsonify, request

from .models import ApiClient


def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('X-API-KEY')
        if not api_key:
            return jsonify({"message": "API key is missing"}), 401

        client = ApiClient.query.filter_by(api_key=api_key).first()
        if not client:
            return jsonify({"message": "Invalid API key"}), 401

        return f(*args, **kwargs)
    return decorated_function
