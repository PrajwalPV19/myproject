def send_invoice_email(to_email: str, subject: str, body: str) -> dict:
    return {"status": "queued", "to": to_email, "subject": subject, "body": body}
