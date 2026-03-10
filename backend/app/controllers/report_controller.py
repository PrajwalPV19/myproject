from flask import jsonify, request
from sqlalchemy import func

from app import db
from app.models.models import Invoice


def revenue_report():
    company_id = request.args.get("company_id", type=int)
    revenue = (
        db.session.query(func.coalesce(func.sum(Invoice.amount_paid), 0))
        .filter(Invoice.company_id == company_id)
        .scalar()
    )
    return jsonify({"company_id": company_id, "revenue": float(revenue)})


def outstanding_report():
    company_id = request.args.get("company_id", type=int)
    outstanding = (
        db.session.query(func.coalesce(func.sum(Invoice.total_amount - Invoice.amount_paid), 0))
        .filter(Invoice.company_id == company_id)
        .filter(Invoice.status.in_(["Sent", "Viewed", "Overdue"]))
        .scalar()
    )
    return jsonify({"company_id": company_id, "outstanding": float(outstanding)})
