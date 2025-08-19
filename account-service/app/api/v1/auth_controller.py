from datetime import timedelta
from flask import Blueprint, request, jsonify, Response
from app.config.sqlmodel_config import db
from app.services import AuthService
from flask_jwt_extended import create_access_token
from app.dtos.login_dto import LoginDto

auth_bl = Blueprint("auth", __name__, url_prefix="/auth")
auth_service = AuthService()


@auth_bl.post("/login")
def login() -> tuple[Response, int]:
    valited_model = LoginDto.model_validate(request.get_json())
    account = auth_service.get_auth(valited_model.username, 
                                 valited_model.password, db())
    token = create_access_token(
        identity=account.id,
        expires_delta=timedelta(days=2)
    )

    return jsonify({
        "access_token": token,
        "data": account.as_json()
    }), 200
