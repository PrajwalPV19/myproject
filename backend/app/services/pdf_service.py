from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def generate_invoice_pdf(invoice_data: dict, path: str) -> str:
    c = canvas.Canvas(path, pagesize=A4)
    c.setFont("Helvetica", 12)
    c.drawString(50, 800, f"Invoice: {invoice_data['invoice_number']}")
    c.drawString(50, 780, f"Client: {invoice_data['client_name']}")
    c.drawString(50, 760, f"Total: {invoice_data['total_amount']}")
    c.save()
    return path
