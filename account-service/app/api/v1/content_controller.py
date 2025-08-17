from app.config.sqlmodel_config import db
from app.services import ContentService
from flask import Blueprint, jsonify, Response
from flask_jwt_extended import jwt_required

content_bl = Blueprint("content", __name__,
                       url_prefix="/media")

content_service = ContentService()


@content_bl.get("/")
@jwt_required()
def get_contents() -> tuple[Response, int]:
    result = content_service.get_contents(db())
    return jsonify(result.serialize()), 200
 