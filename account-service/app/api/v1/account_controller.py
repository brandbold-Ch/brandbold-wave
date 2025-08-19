from flask import Blueprint, request, jsonify, Response
from app.config.sqlmodel_config import db
from app.services import AccountService
from app.orchestrators import AccountOrchestrator
from flask_jwt_extended import jwt_required
from app.dtos import CreateAccountDto, UpdateAccountDto

account_bl = Blueprint("account", __name__, url_prefix="/accounts")
account_orchestrator = AccountOrchestrator()
account_service = AccountService()


@account_bl.post("/")
def create_account() -> tuple[Response, int]:
    validated_model = CreateAccountDto.model_validate(request.get_json())
    result = account_orchestrator.register_account(validated_model, db())
    return jsonify(result.as_json()), 201


@account_bl.get("/<uuid:account_id>")
def get_account(account_id) -> tuple[Response, int]:
    result = account_service.get_account(account_id, db())
    return jsonify(result.as_json()), 200


@account_bl.get("/")
def get_accounts() -> tuple[Response, int]:
    result = account_service.get_accounts(db())
    return jsonify(result.serialize(deep=False)), 200


@account_bl.put("/<uuid:account_id>")
@jwt_required()
def update_account(account_id) -> tuple[Response, int]:
    validated_model = UpdateAccountDto.model_validate(request.get_json())
    result = account_service.update_account(
        account_id,
        validated_model,
        db()
    )
    return jsonify(result.as_json()), 202


@account_bl.delete("/<uuid:account_id>")
@jwt_required()
def delete_account(account_id) -> tuple[Response, int]:
    account_service.delete_account(account_id, db())
    return jsonify(...), 204
