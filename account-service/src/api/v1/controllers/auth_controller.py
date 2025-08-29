"""
Auth controller module.
Defines HTTP endpoints for authentication operations (login).
"""
from datetime import timedelta
from flask import Blueprint, jsonify, Response
from flask_jwt_extended import create_access_token
from src.config.sqlmodel_config import db
from src.api.v1.services import AuthService
from src.api.v1.dtos.login_dto import LoginDto
from src.decorators import parse_body

auth_bl = Blueprint("auth", __name__, url_prefix="/auth")
auth_service = AuthService()


@auth_bl.post("/login")
@parse_body
def login(dto: LoginDto) -> tuple[Response, int]:
    """
    Authenticate a user and return a JWT access token.
    Returns:
        tuple[Response, int]: The access token and user data as JSON, and HTTP status code 200.
    """
    account = auth_service.get_auth(dto.username, dto.password, db())
    token = create_access_token(
        identity=account.id, expires_delta=timedelta(days=2)
    )

    return jsonify({
        "access_token": token,
        "data": account.as_json()
    }), 200
