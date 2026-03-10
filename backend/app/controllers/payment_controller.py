from datetime import datetime

from flask import jsonify, request

from app import db
from app.models.models import Invoice, Payment


def create_payment():
    payload = request.get_json() or {}
    payment = Payment(
        invoice_id=payload["invoice_id"],
        company_id=payload["company_id"],
        amount=payload["amount"],
        payment_date=datetime.fromisoformat(payload["payment_date"]).date(),
        method=payload["method"],
        gateway_reference=payload.get("gateway_reference"),
    )
    db.session.add(payment)

    invoice = Invoice.query.get_or_404(payload["invoice_id"])
    invoice.amount_paid = float(invoice.amount_paid) + float(payload["amount"])
    invoice.status = "Paid" if invoice.amount_paid >= invoice.total_amount else invoice.status

    db.session.commit()
    return jsonify({"id": payment.id, "message": "Payment recorded"}), 201


def list_payments():
    company_id = request.args.get("company_id", type=int)
    payments = Payment.query.filter_by(company_id=company_id).all() if company_id else []
    return jsonify([
        {"id": p.id, "invoice_id": p.invoice_id, "amount": float(p.amount), "method": p.method}
        for p in payments
    ])
