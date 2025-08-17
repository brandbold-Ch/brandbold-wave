from flask import Blueprint, Response, request, jsonify
from app.config.sqlmodel_config import db
from app.services import DeviceService
from flask_jwt_extended import jwt_required

device_bl = Blueprint("device", __name__,
                      url_prefix="/<uuid:user_id>/devices")

device_service = DeviceService()


@device_bl.post("/")
@jwt_required()
def create_device(user_id) -> tuple[Response, int]:
    result = device_service.create_device(
        user_id,
        request.get_json(),
        db()
    )
    return jsonify(result.as_json()), 201


@device_bl.get("/")
@jwt_required()
def get_devices(user_id) -> tuple[Response, int]:
    result = device_service.get_devices(
        user_id,
        db()
    )
    return jsonify(result.serialize()), 200


@device_bl.get("/<uuid:device_id>")
@jwt_required()
def get_device(user_id, device_id) -> tuple[Response, int]:
    result = device_service.get_device(
        user_id,
        device_id,
        db()
    )
    return jsonify(result.as_json()), 200


@device_bl.delete("/<uuid:device_id>")
@jwt_required()
def delete_device(user_id, device_id) -> tuple[Response, int]:
    result = device_service.delete_device(
        user_id,
        device_id,
        db()
    )
    return jsonify(result.as_json()), 204


@device_bl.put("/<uuid:device_id>")
@jwt_required()
def update_device(user_id, device_id) -> tuple[Response, int]:
    result = device_service.update_device(
        user_id,
        device_id,
        request.get_json(),
        db()
    )
    return jsonify(result.as_json()), 202
