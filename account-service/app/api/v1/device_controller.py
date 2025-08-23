"""
Device controller module.
Defines HTTP endpoints for device operations (create, retrieve, update, delete).
"""
from flask import Blueprint, Response, jsonify
from app.config.sqlmodel_config import db
from flask_jwt_extended import jwt_required
from app.services import DeviceService
from app.dtos import DeviceInfoDto
from app.decorators import parse_body

device_bl = Blueprint("device", __name__, url_prefix="/<uuid:account_id>/devices")
device_service = DeviceService()


@device_bl.post("/")
@parse_body
def create_device(account_id, dto: DeviceInfoDto) -> tuple[Response, int]:
    """
    Create a new device for a given account.
    Args:
        account_id (UUID): The account's unique identifier.
    Returns:
        tuple[Response, int]: The created device as JSON and HTTP status code 201.
    """
    result = device_service.create_device(account_id, dto, db())
    return jsonify(result.as_json()), 201


@device_bl.get("/")
def get_devices(account_id) -> tuple[Response, int]:
    """
    Retrieve all devices for a given account.
    Args:
        account_id (UUID): The account's unique identifier.
    Returns:
        tuple[Response, int]: The list of devices as JSON and HTTP status code 200.
    """
    result = device_service.get_devices(account_id, db())
    return jsonify(result.serialize()), 200


@device_bl.get("/<uuid:device_id>")
def get_device(account_id, device_id) -> tuple[Response, int]:
    """
    Retrieve a specific device by account and device ID.
    Args:
        account_id (UUID): The account's unique identifier.
        device_id (UUID): The device's unique identifier.
    Returns:
        tuple[Response, int]: The device as JSON and HTTP status code 200.
    """
    result = device_service.get_device(account_id, device_id, db())
    return jsonify(result.as_json()), 200


@device_bl.delete("/<uuid:device_id>")
def delete_device(account_id, device_id) -> tuple[Response, int]:
    """
    Delete a specific device by account and device ID.
    Args:
        account_id (UUID): The account's unique identifier.
        device_id (UUID): The device's unique identifier.
    Returns:
        tuple[Response, int]: The deleted device as JSON and HTTP status code 204.
    """
    result = device_service.delete_device(account_id, device_id, db())
    return jsonify(result.as_json()), 204


@device_bl.put("/<uuid:device_id>")
@parse_body
def update_device(account_id, device_id, dto: DeviceInfoDto) -> tuple[Response, int]:
    """
    Update a specific device by account and device ID.
    Args:
        account_id (UUID): The account's unique identifier.
        device_id (UUID): The device's unique identifier.
    Returns:
        tuple[Response, int]: The updated device as JSON and HTTP status code 202.
    """
    result = device_service.update_device(account_id, device_id, dto, db())
    return jsonify(result.as_json()), 202
