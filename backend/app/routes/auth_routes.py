from flask import Blueprint

from app.controllers.auth_controller import login, logout, register

auth_bp = Blueprint("auth", __name__)

auth_bp.post("/register")(register)
auth_bp.post("/login")(login)
auth_bp.post("/logout")(logout)
