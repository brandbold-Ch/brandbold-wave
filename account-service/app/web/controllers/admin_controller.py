from app.config.sqlmodel_config import db
from app.utils.builders import build_spring_url
from flask import (
    Blueprint, 
    request, 
    render_template, 
    redirect, 
    url_for, 
    Response
)
from app.services import (
    AuthService, 
    UserService, 
    FranchiseService, 
    GenreService, 
    ContentService
)

admin_bl = Blueprint("admin", __name__,
                     url_prefix="/admin", template_folder="../templates/admin")
  
content_service = ContentService()
genre_service = GenreService()
franchise_service = FranchiseService()
user_services = UserService()
auth_service = AuthService()


@admin_bl.route("/", methods=["GET"])
def dashboard_view() -> str:
    return render_template("dashboard_view.html")


@admin_bl.route("/franchises", methods=["GET"])
def franchises_view() -> str:
    franchises = franchise_service.get_franchises(db())    
    return render_template(
        "franchises_view.html",
        data=franchises.serialize()
    )


@admin_bl.route("/franchises", methods=["POST"])
def create_franchise() -> Response:
    data = request.form.to_dict()
    franchise_service.create_franchise(data, db())
    return redirect(url_for("admin.franchises_view"))

    
@admin_bl.route("/franchises/<uuid:franchise_id>", methods=["PUT"])
def update_franchise(franchise_id) -> Response:
    data = request.form.to_dict()
    franchise_service.update_franchise(franchise_id, data, db())
    return redirect(url_for("admin.franchises_view"))


@admin_bl.route("/franchises/<uuid:franchise_id>", methods=["DELETE"])
def delete_franchise(franchise_id) -> Response:
    franchise_service.delete_franchise(franchise_id, db())
    return redirect(url_for("admin.franchises_view"))


@admin_bl.route("/media", methods=["GET"])
def media_view() -> str:
    contents = content_service.get_contents(db())
    return render_template(
        "content_view.html", 
        data=contents.serialize()
    )


@admin_bl.route("/media/upload", methods=["GET"])
def create_media_view() -> str:
    genres = genre_service.get_genres(db())
    franchises = franchise_service.get_franchises(db())
    
    return render_template(
        "upload_content.html",
        data={
            "genres": genres.serialize(),
            "franchises": franchises.serialize(),
            "url": build_spring_url("upload", proxy=True)
        }
    )


@admin_bl.route("/media/<uuid:content_id>", methods=["PUT"])
def update_media(content_id) -> Response:
    content_service.update_content(content_id, request.get_json(), db())
    return redirect(url_for("admin.media_view"))


@admin_bl.route("/media/<uuid:content_id>", methods=["DELETE"])
def delete_media(content_id) -> Response:
    #content_service.delete_content(content_id, get_session())
    return redirect(url_for("admin.media_view"))


@admin_bl.route("/users", methods=["GET"])
def users_view() -> str:
    users = user_services.get_users(db())
    return render_template(
        "users_view.html",
        data=users.serialize(deep=False)
    )


@admin_bl.route("/users/<uuid:user_id>", methods=["PUT"])
def update_user(user_id) -> Response:
    auth_service.update_auth(user_id, request.get_json(), db())
    return redirect(url_for("admin.users_view"))
    

@admin_bl.route("/users/<uuid:user_id>", methods=["DELETE"])
def delete_user(user_id) -> Response:
    user_services.delete_user(user_id, db())
    return redirect(url_for("admin.users_view"))


@admin_bl.route("/content-streaming", methods=["GET"])
def content_streaming_view() -> str:
    return render_template(
        "content_streaming.html",
        url=request.args.get("url")
    )


@admin_bl.route("/genres", methods=["GET"])
def genres_view() -> str:
    genres = genre_service.get_genres(db())
    return render_template(
        "genres_view.html",
        data=genres.serialize()
    )


@admin_bl.route("/genres", methods=["POST"])
def create_genre() -> Response:
    data = request.form.to_dict()
    genre_service.create_genre(data, db())
    return redirect(url_for("admin.genres_view"))


@admin_bl.route("/genres/<uuid:genre_id>", methods=["DELETE"])
def delete_genre(genre_id) -> Response:
    genre_service.delete_genre(genre_id, db())
    return redirect(url_for("admin.genres_view")) 
