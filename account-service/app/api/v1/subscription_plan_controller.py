from flask import Blueprint, request, jsonify, Response
from app.config.sqlmodel_config import db
from app.services import SubscriptionPlanService

subscription_plan_bl = Blueprint("subscription", __name__,
                                 url_prefix="/subscription-plans")

subscription_plan_service = SubscriptionPlanService()


@subscription_plan_bl.post("/")
def create_subscription_plan() -> tuple[Response, int]:
    result = subscription_plan_service.create_plan(
        request.get_json(),
        db()
    )
    return jsonify(result.as_json()), 201


@subscription_plan_bl.get("/")
def get_subscription_plans() -> tuple[Response, int]:
    result = subscription_plan_service.get_plans(db())
    return jsonify(result.serialize()), 200


@subscription_plan_bl.get("/<string:plan_name>")
def get_subscription_plan(plan_name) -> tuple[Response, int]:
    result = subscription_plan_service.get_one_plan(
        plan_name,
        db()
    )
    return jsonify(result.as_json()), 200


@subscription_plan_bl.put("/<string:plan_id>")
def update_subscription_plan(plan_id) -> tuple[Response, int]:
    result = subscription_plan_service.update_plan(
        plan_id,
        request.get_json(),
        db()
    )
    return jsonify(result.as_json()), 202


@subscription_plan_bl.delete("/<string:plan_id>")
def delete_subscription_plan(plan_id) -> tuple[Response, int]:
    result = subscription_plan_service.delete_plan(
        plan_id,
        db()
    )
    return jsonify(result.as_json()), 204
