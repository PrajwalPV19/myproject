import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "postgresql://smartinvoice:smartinvoice@db:5432/smartinvoice"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "change-me-in-production")
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*")
    STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "")
    APP_URL = os.getenv("APP_URL", "http://localhost:5173")
