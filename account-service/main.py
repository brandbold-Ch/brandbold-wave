from flask import Flask, jsonify, Response, g
from app.api.v1 import admin_bl
from app.api.v1 import device_bl
from app.api.v1 import auth_bl
from app.api.v1 import account_bl
from app.exceptions.exceptions import (
    BaseExceptionError,
    InvalidTokenException,
    ExpiredTokenException,
    NotFoundTokenException
)
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = Flask(__name__, )
app.config['MAX_CONTENT_LENGTH'] = 7 * 1024 * 1024 * 1024
app.config["SECRET_KEY"] = "my_secret"
app.config["JWT_SECRET_KEY"] = app.config["SECRET_KEY"]

CORS(app)
jwt = JWTManager(app)


@app.errorhandler(BaseExceptionError)
def handle_errors(error: BaseExceptionError) -> tuple[Response, int]:
    return jsonify(error.to_dict()), error.http_code


@jwt.invalid_token_loader
def invalid_token_cb(error) -> tuple[Response, int]:
    exc = InvalidTokenException(error.__repr__())
    return jsonify(exc.to_dict()), exc.http_code


@jwt.expired_token_loader
def expired_token_cb(jwt_header, jwt_payload) -> tuple[Response, int]:
    exc = ExpiredTokenException("Your token has expired")
    return jsonify(exc.to_dict()), exc.http_code


@jwt.unauthorized_loader
def missing_token_cb(error) -> tuple[Response, int]:
    exc = NotFoundTokenException(error.__repr__())
    return jsonify(exc.to_dict()), exc.http_code


@app.teardown_appcontext
def remove_session(exception=None):
    session = g.pop("session", None)
    if session is not None:
        session.close()


CORS(admin_bl)
CORS(auth_bl)
CORS(account_bl)
CORS(device_bl)

app.register_blueprint(account_bl)
app.register_blueprint(admin_bl)
app.register_blueprint(auth_bl)
app.register_blueprint(device_bl)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
    