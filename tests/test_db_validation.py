from utils.db_validation import validate_transaction

def test_transaction_exists():
    txn_id = "TXN12345"

    status = validate_transaction(txn_id)

    assert status is not None