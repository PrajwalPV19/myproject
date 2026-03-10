from datetime import datetime

from sqlalchemy import UniqueConstraint

from app import db


class TimestampMixin:
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)


class User(db.Model, TimestampMixin):
    __tablename__ = "users"

    id = db.Column(db.BigInteger, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.Text, nullable=False)
    full_name = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), nullable=False, default="owner")
    is_active = db.Column(db.Boolean, nullable=False, default=True)


class Company(db.Model, TimestampMixin):
    __tablename__ = "companies"

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    gstin = db.Column(db.String(15), index=True)
    currency_code = db.Column(db.String(3), nullable=False, default="INR")
    timezone = db.Column(db.String(50), nullable=False, default="Asia/Kolkata")


class CompanyUser(db.Model, TimestampMixin):
    __tablename__ = "company_users"
    __table_args__ = (UniqueConstraint("company_id", "user_id", name="uq_company_user"),)

    id = db.Column(db.BigInteger, primary_key=True)
    company_id = db.Column(db.BigInteger, db.ForeignKey("companies.id", ondelete="CASCADE"), nullable=False)
    user_id = db.Column(db.BigInteger, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    role = db.Column(db.String(20), nullable=False, default="member")


class Client(db.Model, TimestampMixin):
    __tablename__ = "clients"

    id = db.Column(db.BigInteger, primary_key=True)
    company_id = db.Column(db.BigInteger, db.ForeignKey("companies.id", ondelete="CASCADE"), nullable=False, index=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(30))
    billing_address = db.Column(db.Text)


class Invoice(db.Model, TimestampMixin):
    __tablename__ = "invoices"

    id = db.Column(db.BigInteger, primary_key=True)
    company_id = db.Column(db.BigInteger, db.ForeignKey("companies.id", ondelete="CASCADE"), nullable=False, index=True)
    client_id = db.Column(db.BigInteger, db.ForeignKey("clients.id", ondelete="RESTRICT"), nullable=False, index=True)
    invoice_number = db.Column(db.String(50), nullable=False)
    issue_date = db.Column(db.Date, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), nullable=False, default="Draft", index=True)
    subtotal = db.Column(db.Numeric(12, 2), nullable=False, default=0)
    cgst_amount = db.Column(db.Numeric(12, 2), nullable=False, default=0)
    sgst_amount = db.Column(db.Numeric(12, 2), nullable=False, default=0)
    igst_amount = db.Column(db.Numeric(12, 2), nullable=False, default=0)
    total_amount = db.Column(db.Numeric(12, 2), nullable=False, default=0)
    amount_paid = db.Column(db.Numeric(12, 2), nullable=False, default=0)
    notes = db.Column(db.Text)
    is_recurring = db.Column(db.Boolean, nullable=False, default=False)
    recurring_frequency = db.Column(db.String(20))


class InvoiceItem(db.Model, TimestampMixin):
    __tablename__ = "invoice_items"

    id = db.Column(db.BigInteger, primary_key=True)
    invoice_id = db.Column(db.BigInteger, db.ForeignKey("invoices.id", ondelete="CASCADE"), nullable=False, index=True)
    description = db.Column(db.Text, nullable=False)
    quantity = db.Column(db.Numeric(10, 2), nullable=False, default=1)
    unit_price = db.Column(db.Numeric(12, 2), nullable=False)
    gst_rate = db.Column(db.Numeric(5, 2), nullable=False, default=18)
    line_total = db.Column(db.Numeric(12, 2), nullable=False)


class Payment(db.Model, TimestampMixin):
    __tablename__ = "payments"

    id = db.Column(db.BigInteger, primary_key=True)
    invoice_id = db.Column(db.BigInteger, db.ForeignKey("invoices.id", ondelete="CASCADE"), nullable=False, index=True)
    company_id = db.Column(db.BigInteger, db.ForeignKey("companies.id", ondelete="CASCADE"), nullable=False, index=True)
    amount = db.Column(db.Numeric(12, 2), nullable=False)
    payment_date = db.Column(db.Date, nullable=False)
    method = db.Column(db.String(30), nullable=False)
    gateway_reference = db.Column(db.String(120))


class Subscription(db.Model, TimestampMixin):
    __tablename__ = "subscriptions"

    id = db.Column(db.BigInteger, primary_key=True)
    company_id = db.Column(db.BigInteger, db.ForeignKey("companies.id", ondelete="CASCADE"), nullable=False, index=True)
    plan_name = db.Column(db.String(50), nullable=False)
    billing_cycle = db.Column(db.String(20), nullable=False, default="monthly")
    amount = db.Column(db.Numeric(12, 2), nullable=False)
    status = db.Column(db.String(20), nullable=False, default="active")


class Notification(db.Model, TimestampMixin):
    __tablename__ = "notifications"

    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    company_id = db.Column(db.BigInteger, db.ForeignKey("companies.id", ondelete="CASCADE"), nullable=False, index=True)
    type = db.Column(db.String(30), nullable=False)
    payload = db.Column(db.JSON, nullable=False)
    status = db.Column(db.String(20), nullable=False, default="queued")
