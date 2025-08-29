"""
Profile controller module.
Defines HTTP endpoints for profile operations (create, retrieve, update, delete).
"""
from flask import Blueprint, Response, jsonify
from flask_jwt_extended import jwt_required
from src.api.v1.services import ProfileService
from src.config.sqlmodel_config import db
from src.api.v1.dtos import ProfileInfoDto
from src.decorators import parse_body

profile_bl = Blueprint("profile", __name__, url_prefix="/<uuid:account_id>/profiles")
profile_service = ProfileService()


@profile_bl.post("/")
@parse_body
def create_profile(account_id, dto: ProfileInfoDto) -> tuple[Response, int]:
    """
    Create a new profile for a given account.
    Args:
        account_id (UUID): The account's unique identifier.
        dto (ProfileInfoDto): The profile data transfer object.
    Returns:
        tuple[Response, int]: The created profile as JSON and HTTP status code 201.
    """
    result = profile_service.create_profile(account_id, dto, db())
    return jsonify(result.as_json()), 201


@profile_bl.get("/")
def get_profiles(account_id) -> tuple[Response, int]:
    """
    Retrieve all profiles for a given account.
    Args:
        account_id (UUID): The account's unique identifier.
    Returns:
        tuple[Response, int]: The list of profiles as JSON and HTTP status code 200.
    """
    result = profile_service.get_profiles(account_id, db())
    return jsonify(result.serialize()), 200


@profile_bl.get("/<uuid:profile_id>")
def get_profile(account_id, profile_id) -> tuple[Response, int]:
    """
    Retrieve a specific profile by account and profile ID.
    Args:
        account_id (UUID): The account's unique identifier.
        profile_id (UUID): The profile's unique identifier.
    Returns:
        tuple[Response, int]: The profile as JSON and HTTP status code 200.
    """
    result = profile_service.get_profile(account_id, profile_id, db())
    return jsonify(result.as_json()), 200


@profile_bl.delete("/<uuid:profile_id>")
def delete_profile(account_id, profile_id) -> tuple[Response, int]:
    """
    Delete a specific profile by account and profile ID.
    Args:
        account_id (UUID): The account's unique identifier.
        profile_id (UUID): The profile's unique identifier.
    Returns:
        tuple[Response, int]: The deleted profile as JSON and HTTP status code 204.
    """
    result = profile_service.delete_profile(account_id, profile_id, db())
    return jsonify(result.as_json()), 204


@profile_bl.put("/<uuid:profile_id>")
@parse_body
def update_profile(account_id, profile_id, dto: ProfileInfoDto) -> tuple[Response, int]:
    """
    Update a specific profile by account and profile ID.
    Args:
        account_id (UUID): The account's unique identifier.
        profile_id (UUID): The profile's unique identifier.
        dto (ProfileInfoDto): The profile data transfer object.
    Returns:
        tuple[Response, int]: The updated profile as JSON and HTTP status code 202.
    """
    result = profile_service.update_profile(account_id, profile_id, dto, db())
    return jsonify(result.as_json()), 202
