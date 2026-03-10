from flask_jwt_extended import create_access_token

from app import bcrypt


def hash_password(raw_password: str) -> str:
    return bcrypt.generate_password_hash(raw_password).decode("utf-8")


def verify_password(raw_password: str, hashed: str) -> bool:
    return bcrypt.check_password_hash(hashed, raw_password)


def generate_token(identity: str) -> str:
    return create_access_token(identity=identity)
