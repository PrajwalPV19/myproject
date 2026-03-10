from flask import Blueprint
from flask_jwt_extended import jwt_required

from app.controllers.report_controller import outstanding_report, revenue_report

report_bp = Blueprint("reports", __name__)

report_bp.get("/reports/revenue")(jwt_required()(revenue_report))
report_bp.get("/reports/outstanding")(jwt_required()(outstanding_report))
