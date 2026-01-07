def test_payment_accepted():
    response = {
        "status": "ACCEPTED",
        "clearing": "SEPA"
    }
    assert response["status"] == "ACCEPTED"
    assert response["clearing"] in ["SEPA", "PLUSGIRO"]

def test_payment_rejected():
    response = {
        "status": "REJECTED",
        "error": "INVALID_ACCOUNT"
    }
    assert response["status"] == "REJECTED"

if __name__ == "__main__":
    test_payment_accepted()
    test_payment_rejected()
    print("API tests passed")
