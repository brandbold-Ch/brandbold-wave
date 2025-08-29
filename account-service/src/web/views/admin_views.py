
"""
This module defines the admin blueprint and its routes for the admin dashboard and account management views.
It provides endpoints for viewing, updating, and deleting user accounts, as well as rendering the admin dashboard.
"""
from src.api.v1.services import AuthService, AccountService
from flask import request, render_template, Blueprint, redirect, url_for, Response
from src.config.sqlmodel_config import db

admin_bl = Blueprint(
    "admin", __name__, url_prefix="/admin", template_folder="../templates/admin"
)

user_services = AccountService()
auth_service = AuthService()

"""
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


@admin_bl.route("/content-streaming", methods=["GET"])
def content_streaming_view() -> str:
    return render_template(
        "content_streaming.html",
        url=request.args.get("url")
    )
"""


@admin_bl.route("/", methods=["GET"])
def dashboard_view() -> str:
    """
    Render the admin dashboard view.

    Returns:
        str: Rendered HTML for the dashboard.
    """
    return render_template("dashboard_view.html")


@admin_bl.route("/accounts", methods=["GET"])
def accounts_view() -> str:
    """
    Render the accounts view with a list of user accounts.

    Returns:
        str: Rendered HTML for the accounts list.
    """
    accounts = user_services.get_accounts(db())
    return render_template(
        "accounts_view.html",
        accounts=accounts.serialize(deep=False)
    )


@admin_bl.route("/accounts/<uuid:account_id>", methods=["PUT"])
def update_account(account_id) -> Response:
    """
    Update the authentication information for a specific account.

    Args:
        account_id (UUID): The unique identifier of the account to update.

    Returns:
        Response: Redirects to the accounts view after update.
    """
    auth_service.update_auth(account_id, request.get_json(), db())
    return redirect(url_for("admin.accounts_view"))


@admin_bl.route("/accounts/<uuid:account_id>", methods=["DELETE"])
def delete_account(account_id) -> Response:
    """
    Delete a specific user account.

    Args:
        account_id (UUID): The unique identifier of the account to delete.

    Returns:
        Response: Redirects to the accounts view after deletion.
    """
    user_services.delete_account(account_id, db())
    return redirect(url_for("admin.accounts_view"))
