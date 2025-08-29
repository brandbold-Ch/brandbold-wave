
"""
Main entry point for the Account Service Flask application.
Initializes the Flask app, configures JWT, CORS, error handlers, and registers blueprints for API endpoints.
"""
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask import Flask, jsonify, Response, g, send_from_directory
from src.web.views.admin_views import admin_bl
from src.api.v1.controllers import (
    device_bl, auth_bl, account_bl, profile_bl
)
from src.exceptions.exceptions import (
    BaseExceptionError,
    InvalidTokenException,
    ExpiredTokenException,
    NotFoundTokenException
)

app = Flask(
    __name__, static_folder="src/web/static/images", static_url_path="/images"
)
app.config['MAX_CONTENT_LENGTH'] = 7 * 1024 * 1024 * 1024
app.config["SECRET_KEY"] = "my_secret"
app.config["JWT_SECRET_KEY"] = app.config["SECRET_KEY"]

CORS(app)
jwt = JWTManager(app)


@app.get("/avatars/<string:avatar>")
def get_avatar(avatar) -> Response:
    """
    Serve a PNG avatar image from the avatars static directory.

    Args:
        avatar (str): The filename of the avatar image to retrieve.

    Returns:
        Response: The image file as a Flask response with MIME type image/png.
    """
    return send_from_directory(
        "app/web/static/images/avatars", avatar, mimetype="image/png"
    )
    
    
@app.errorhandler(BaseExceptionError)
def handle_errors(error: BaseExceptionError) -> tuple[Response, int]:
    """
    Handle custom application exceptions and return a JSON response.

    Args:
        error (BaseExceptionError): The custom exception instance.

    Returns:
        tuple[Response, int]: JSON response and HTTP status code.
    """
    return jsonify(error.to_dict()), error.http_code


@jwt.invalid_token_loader
def invalid_token_cb(error) -> tuple[Response, int]:
    """
    Handle invalid JWT token errors.

    Args:
        error (str): Error message from JWT manager.

    Returns:
        tuple[Response, int]: JSON response and HTTP status code.
    """
    exc = InvalidTokenException(error)
    return jsonify(exc.to_dict()), exc.http_code


@jwt.expired_token_loader
def expired_token_cb(jwt_header, jwt_payload) -> tuple[Response, int]:
    """
    Handle expired JWT token errors.

    Args:
        jwt_header (dict): JWT header.
        jwt_payload (dict): JWT payload.

    Returns:
        tuple[Response, int]: JSON response and HTTP status code.
    """
    exc = ExpiredTokenException("Your token has expired")
    return jsonify(exc.to_dict()), exc.http_code


@jwt.unauthorized_loader
def missing_token_cb(error) -> tuple[Response, int]:
    """
    Handle missing JWT token errors.

    Args:
        error (str): Error message from JWT manager.

    Returns:
        tuple[Response, int]: JSON response and HTTP status code.
    """
    exc = NotFoundTokenException(error)
    return jsonify(exc.to_dict()), exc.http_code


@app.teardown_appcontext
def remove_session(exception):
    """
    Remove and close the database session at the end of the app context.

    Args:
        exception (Exception, optional): Exception raised, if any.
    """
    session = g.pop("session", None)
    if session is not None:
        session.close()


account_bl.register_blueprint(device_bl)
account_bl.register_blueprint(profile_bl)
app.register_blueprint(account_bl)
app.register_blueprint(admin_bl)
app.register_blueprint(auth_bl)


if __name__ == "__main__":
    """
    Run the Flask application in debug mode on all interfaces at port 5000.
    """
    app.run(debug=True, host="0.0.0.0", port=5000)
    