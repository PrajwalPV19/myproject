from datetime import datetime

from flask import jsonify, request

from app import db
from app.models.models import Invoice
from app.services.invoice_service import compute_invoice_totals


def list_invoices():
    company_id = request.args.get("company_id", type=int)
    invoices = Invoice.query.filter_by(company_id=company_id).all() if company_id else []
    return jsonify([
        {
            "id": i.id,
            "invoice_number": i.invoice_number,
            "status": i.status,
            "total_amount": float(i.total_amount),
            "due_date": i.due_date.isoformat(),
        }
        for i in invoices
    ])


def create_invoice():
    payload = request.get_json() or {}
    items = payload.get("items", [])
    totals = compute_invoice_totals(items, payload.get("intra_state", True))
    invoice = Invoice(
        company_id=payload["company_id"],
        client_id=payload["client_id"],
        invoice_number=payload["invoice_number"],
        issue_date=datetime.fromisoformat(payload["issue_date"]).date(),
        due_date=datetime.fromisoformat(payload["due_date"]).date(),
        status=payload.get("status", "Draft"),
        notes=payload.get("notes"),
        is_recurring=payload.get("is_recurring", False),
        recurring_frequency=payload.get("recurring_frequency"),
        **totals,
    )
    db.session.add(invoice)
    db.session.commit()
    return jsonify({"id": invoice.id, "message": "Invoice created"}), 201


def get_invoice(invoice_id: int):
    invoice = Invoice.query.get_or_404(invoice_id)
    return jsonify(
        {
            "id": invoice.id,
            "invoice_number": invoice.invoice_number,
            "status": invoice.status,
            "subtotal": float(invoice.subtotal),
            "total_amount": float(invoice.total_amount),
            "amount_paid": float(invoice.amount_paid),
        }
    )


def update_invoice(invoice_id: int):
    invoice = Invoice.query.get_or_404(invoice_id)
    payload = request.get_json() or {}
    for key in ["status", "notes", "due_date"]:
        if key in payload:
            setattr(invoice, key, payload[key])
    db.session.commit()
    return jsonify({"message": "Invoice updated"})


def delete_invoice(invoice_id: int):
    invoice = Invoice.query.get_or_404(invoice_id)
    db.session.delete(invoice)
    db.session.commit()
    return jsonify({"message": "Invoice deleted"})
