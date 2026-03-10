from flask import Blueprint
from flask_jwt_extended import jwt_required

from app.controllers.client_controller import create_client, delete_client, list_clients, update_client

client_bp = Blueprint("clients", __name__)

client_bp.get("/clients")(jwt_required()(list_clients))
client_bp.post("/clients")(jwt_required()(create_client))
client_bp.put("/clients/<int:client_id>")(jwt_required()(update_client))
client_bp.delete("/clients/<int:client_id>")(jwt_required()(delete_client))
