from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from .config import Config

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
bcrypt = Bcrypt()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)
    CORS(app, resources={r"/api/*": {"origins": app.config["CORS_ORIGINS"]}})

    from .routes.auth_routes import auth_bp
    from .routes.client_routes import client_bp
    from .routes.invoice_routes import invoice_bp
    from .routes.payment_routes import payment_bp
    from .routes.report_routes import report_bp

    app.register_blueprint(auth_bp, url_prefix="/api")
    app.register_blueprint(client_bp, url_prefix="/api")
    app.register_blueprint(invoice_bp, url_prefix="/api")
    app.register_blueprint(payment_bp, url_prefix="/api")
    app.register_blueprint(report_bp, url_prefix="/api")

    @app.get("/health")
    def health_check():
        return {"status": "ok", "service": "smartinvoice-api"}, 200

    return app
