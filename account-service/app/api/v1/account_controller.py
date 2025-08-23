"""
Account controller module.
Defines HTTP endpoints for account operations (create, retrieve, update, delete).
"""
from flask import Blueprint, jsonify, Response
from app.config.sqlmodel_config import db
from flask_jwt_extended import jwt_required
from app.services import AccountService
from app.orchestrators import AccountOrchestrator
from app.dtos import CreateAccountDto, AccountInfoDto
from app.decorators import parse_body

account_bl = Blueprint("account", __name__, url_prefix="/accounts")
account_orchestrator = AccountOrchestrator()
account_service = AccountService()


@account_bl.post("/")
@parse_body
def create_account(dto: CreateAccountDto) -> tuple[Response, int]:
    """
    Create a new account.
    Returns:
        tuple[Response, int]: The created account as JSON and HTTP status code 201.
    """
    result = account_orchestrator.register_account(dto, db())
    return jsonify(result.as_json()), 201


@account_bl.get("/<uuid:account_id>")
def get_account(account_id) -> tuple[Response, int]:
    """
    Retrieve an account by its ID.
    Args:
        account_id (UUID): The account's unique identifier.
    Returns:
        tuple[Response, int]: The account as JSON and HTTP status code 200.
    """
    result = account_service.get_account(account_id, db())
    return jsonify(result.as_json()), 200


@account_bl.get("/")
def get_accounts() -> tuple[Response, int]:
    """
    Retrieve all accounts.
    Returns:
        tuple[Response, int]: The list of accounts as JSON and HTTP status code 200.
    """
    result = account_service.get_accounts(db())
    return jsonify(result.serialize(deep=False)), 200

@account_bl.put("/<uuid:account_id>")
@parse_body
def update_account(account_id, dto: AccountInfoDto) -> tuple[Response, int]:
    """
    Update an account by its ID.
    Args:
        account_id (UUID): The account's unique identifier.
    Returns:
        tuple[Response, int]: The updated account as JSON and HTTP status code 202.
    """
    result = account_service.update_account(account_id, dto, db())
    return jsonify(result.as_json()), 202


@account_bl.delete("/<uuid:account_id>")
def delete_account(account_id) -> tuple[Response, int]:
    """
    Delete an account by its ID.
    Args:
        account_id (UUID): The account's unique identifier.
    Returns:
        tuple[Response, int]: Empty JSON and HTTP status code 204.
    """
    account_service.delete_account(account_id, db())
    return jsonify(), 204
