from utils.payment_utils import pay_by_card
from utils.db_validation import validate_transaction
from utils.logger import setup_logger

logger = setup_logger()


def test_card_payment():
    logger.info("Starting test: test_card_payment")

    res = pay_by_card("4111111111111111", "12/28", "123", 500)

    # 🔥 Step 1: Validate API response first
    assert res["status"] == "SUCCESS", "Payment API failed"

    txn_id = res["txn_id"]
    assert txn_id is not None, "Transaction ID is None"

    # 🔥 Step 2: Validate DB only if API success
    db_status = validate_transaction(txn_id)

    assert db_status == "SUCCESS", "DB validation failed"

    logger.info("Test Passed: test_card_payment")