from flask import Blueprint, Response, request, jsonify
from app.config.sqlmodel_config import db
from app.services import WatchHistoryService
from flask_jwt_extended import jwt_required

watch_bl = Blueprint("watch_history", __name__,
                     url_prefix="/<uuid:user_id>/watches")

watch_service = WatchHistoryService()


@watch_bl.post("/")
@jwt_required()
def create_watch_history(user_id) -> tuple[Response, int]:
    result = watch_service.create_watch_history(
        user_id,
        request.get_json(),
        db()
    )
    return jsonify(result.as_json()), 201


@watch_bl.get("/")
@jwt_required()
def get_watch_histories(user_id) -> tuple[Response, int]:
    result = watch_service.get_watch_histories(user_id, db())
    return jsonify(result.serialize()), 200


@watch_bl.get("/<uuid:watch_id>")
@jwt_required()
def get_watch_history(user_id, watch_id) -> tuple[Response, int]:
    result = watch_service.get_watch_history(
        user_id,
        watch_id,
        db()
    )
    return jsonify(result.as_json()), 200


@watch_bl.delete("/<uuid:watch_id>")
@jwt_required()
def delete_watch_history(user_id, watch_id) -> tuple[Response, int]:
    result = watch_service.delete_watch_history(
        user_id,
        watch_id,
        db()
    )
    return jsonify(result.as_json()), 204


@watch_bl.put("/<uuid:watch_id>")
@jwt_required()
def update_watch_history(user_id, watch_id) -> tuple[Response, int]:
    result = watch_service.update_watch_history(
        user_id,
        watch_id,
        request.get_json(),
        db()
    )
    return jsonify(result.as_json()), 202
