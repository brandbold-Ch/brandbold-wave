from flask import Blueprint, request, jsonify, Response
from app.config.sqlmodel_config import db
from app.services import UserService
from app.orchestrators import UserOrchestrator
from flask_jwt_extended import jwt_required
from app.dtos import CreateUserDto, UpdateUserDto

user_bl = Blueprint("user", __name__, url_prefix="/users")

user_orchestrator = UserOrchestrator()
user_service = UserService()


@user_bl.post("/")
def create_user() -> tuple[Response, int]:
    model = CreateUserDto.model_validate(request.get_json())
    result = user_orchestrator.register_user(model, db())
    return jsonify(result.as_json()), 201


@user_bl.get("/<uuid:user_id>")
@jwt_required()
def get_user(user_id) -> tuple[Response, int]:
    result = user_service.get_user(user_id, db())
    return jsonify(result.as_json()), 200


@user_bl.get("/")
@jwt_required()
def get_users() -> tuple[Response, int]:
    result = user_service.get_users(db())
    return jsonify(result.serialize(deep=False)), 200


@user_bl.put("/<uuid:user_id>")
@jwt_required()
def update_user(user_id) -> tuple[Response, int]:
    model = UpdateUserDto.model_validate(request.get_json())
    result = user_service.update_user(
        user_id,
        request.get_json(),
        db()
    )
    return jsonify(result.as_json()), 202


@user_bl.delete("/<uuid:user_id>")
@jwt_required()
def delete_user(user_id) -> tuple[Response, int]:
    user_service.delete_user(user_id, db())
    return jsonify(...), 204
