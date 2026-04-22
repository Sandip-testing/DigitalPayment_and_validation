from utils.logger import setup_logger
from utils.db_validation import insert_transaction
import random

logger = setup_logger()


def generate_txn_id():
    return f"TXN{random.randint(10000, 99999)}"


def pay_by_card(card_number, expiry, cvv, amount):
    logger.info(f"Initiating card payment | Amount: {amount}")

    # 🔥 generate dynamic txn_id
    txn_id = generate_txn_id()

    # 🔥 insert into DB (IMPORTANT CHANGE)
    insert_transaction(txn_id, amount, "SUCCESS")

    response = {
        "status": "SUCCESS",
        "txn_id": txn_id
    }

    logger.info(f"Payment Success | TXN_ID: {txn_id}")

    return response