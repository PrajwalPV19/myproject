from flask import jsonify, request

from app import db
from app.models.models import Client


def list_clients():
    company_id = request.args.get("company_id", type=int)
    clients = Client.query.filter_by(company_id=company_id).all() if company_id else []
    return jsonify([
        {"id": c.id, "name": c.name, "email": c.email, "phone": c.phone} for c in clients
    ])


def create_client():
    payload = request.get_json() or {}
    client = Client(**payload)
    db.session.add(client)
    db.session.commit()
    return jsonify({"id": client.id, "message": "Client created"}), 201


def update_client(client_id: int):
    client = Client.query.get_or_404(client_id)
    payload = request.get_json() or {}
    for key in ["name", "email", "phone", "billing_address"]:
        if key in payload:
            setattr(client, key, payload[key])
    db.session.commit()
    return jsonify({"message": "Client updated"}), 200


def delete_client(client_id: int):
    client = Client.query.get_or_404(client_id)
    db.session.delete(client)
    db.session.commit()
    return jsonify({"message": "Client deleted"}), 200
