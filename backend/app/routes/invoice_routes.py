from flask import Blueprint
from flask_jwt_extended import jwt_required

from app.controllers.invoice_controller import create_invoice, delete_invoice, get_invoice, list_invoices, update_invoice

invoice_bp = Blueprint("invoices", __name__)

invoice_bp.get("/invoices")(jwt_required()(list_invoices))
invoice_bp.post("/invoices")(jwt_required()(create_invoice))
invoice_bp.get("/invoices/<int:invoice_id>")(jwt_required()(get_invoice))
invoice_bp.put("/invoices/<int:invoice_id>")(jwt_required()(update_invoice))
invoice_bp.delete("/invoices/<int:invoice_id>")(jwt_required()(delete_invoice))
