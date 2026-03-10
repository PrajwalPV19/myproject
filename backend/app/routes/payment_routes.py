from flask import Blueprint
from flask_jwt_extended import jwt_required

from app.controllers.payment_controller import create_payment, list_payments

payment_bp = Blueprint("payments", __name__)

payment_bp.post("/payments")(jwt_required()(create_payment))
payment_bp.get("/payments")(jwt_required()(list_payments))
