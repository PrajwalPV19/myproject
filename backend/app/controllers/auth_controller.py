from flask import jsonify, request

from app import db
from app.models.models import User
from app.services.security_service import generate_token, hash_password, verify_password


def register():
    payload = request.get_json() or {}
    required = ["email", "password", "full_name"]
    if not all(payload.get(field) for field in required):
        return jsonify({"message": "Missing required fields"}), 400

    if User.query.filter_by(email=payload["email"]).first():
        return jsonify({"message": "Email already registered"}), 409

    user = User(
        email=payload["email"],
        full_name=payload["full_name"],
        password_hash=hash_password(payload["password"]),
        role="owner",
    )
    db.session.add(user)
    db.session.commit()
    token = generate_token(f"{user.id}:{user.role}")
    return jsonify({"token": token, "user": {"id": user.id, "email": user.email}}), 201


def login():
    payload = request.get_json() or {}
    user = User.query.filter_by(email=payload.get("email", "")).first()
    if not user or not verify_password(payload.get("password", ""), user.password_hash):
        return jsonify({"message": "Invalid credentials"}), 401

    token = generate_token(f"{user.id}:{user.role}")
    return jsonify({"token": token, "user": {"id": user.id, "email": user.email}}), 200


def logout():
    return jsonify({"message": "Logout successful on client token discard"}), 200
