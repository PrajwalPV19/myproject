def compute_invoice_totals(items: list[dict], intra_state: bool = True) -> dict:
    subtotal = sum(item["quantity"] * item["unit_price"] for item in items)
    total_gst = sum((item["quantity"] * item["unit_price"] * item.get("gst_rate", 18) / 100) for item in items)

    cgst_amount = total_gst / 2 if intra_state else 0
    sgst_amount = total_gst / 2 if intra_state else 0
    igst_amount = total_gst if not intra_state else 0
    total_amount = subtotal + total_gst

    return {
        "subtotal": round(subtotal, 2),
        "cgst_amount": round(cgst_amount, 2),
        "sgst_amount": round(sgst_amount, 2),
        "igst_amount": round(igst_amount, 2),
        "total_amount": round(total_amount, 2),
    }
