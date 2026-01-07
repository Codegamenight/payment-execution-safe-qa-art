REQUIRED_FIELDS = [
    "MessageId",
    "CreationDateTime",
    "Debtor",
    "Creditor",
    "Amount",
    "Currency"
]

def validate_payment_message(message: dict) -> list:
    errors = []
    for field in REQUIRED_FIELDS:
        if field not in message or not message[field]:
            errors.append(f"Missing field: {field}")

    if message.get("Amount", 0) <= 0:
        errors.append("Amount must be greater than zero")

    return errors

if __name__ == "__main__":
    payment = {
        "MessageId": "MSG001",
        "CreationDateTime": "2026-01-01T10:00:00",
        "Debtor": "Sender",
        "Creditor": "Receiver",
        "Amount": 250.00,
        "Currency": "SEK"
    }

    errors = validate_payment_message(payment)
    print("VALID" if not errors else errors)
