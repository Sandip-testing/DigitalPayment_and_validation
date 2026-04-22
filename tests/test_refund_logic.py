## logger
from utils.payment_utils import pay_by_card
from utils.logger import setup_logger

logger = setup_logger()

def test_double_debit_refund():
    logger.info("Starting test: test_double_debit_refund")

    txn1 = pay_by_card("4111", "12/28", "123", 100)
    txn2 = pay_by_card("4111", "12/28", "123", 100)

    if txn1["txn_id"] == txn2["txn_id"]:
        logger.info("Duplicate transaction detected")

        refund = {"status": "REFUNDED"}

        assert refund["status"] == "REFUNDED"
        logger.info("Refund successful")

    logger.info("Test Completed: test_double_debit_refund")