from app.config.sqlmodel_config import db
from app.services import GenreService
from flask import Blueprint, jsonify, Response

genre_bl = Blueprint("genre", __name__,
                     url_prefix="/genres")

genre_services = GenreService()


@genre_bl.get("/")
def get_genders() -> tuple[Response, int]:
    result = genre_services.get_genres(db())
    return jsonify(result.serialize()), 200
