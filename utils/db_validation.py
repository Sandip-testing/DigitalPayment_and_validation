from utils.db_connection import get_connection
from utils.logger import setup_logger

logger = setup_logger()


def insert_transaction(txn_id, amount, status):
    logger.info(f"Inserting transaction into DB | TXN_ID: {txn_id}")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO TRANSACTIONS (TXN_ID, AMOUNT, STATUS) VALUES (:1, :2, :3)",
        (txn_id, amount, status)
    )

    conn.commit()
    cursor.close()
    conn.close()

    logger.info(f"Transaction inserted successfully | TXN_ID: {txn_id}")


def validate_transaction(txn_id):
    logger.info(f"Validating transaction in DB | TXN_ID: {txn_id}")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT STATUS FROM TRANSACTIONS WHERE TXN_ID = :txn_id",
        txn_id=txn_id
    )

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        logger.info(f"DB Validation Success | Status: {result[0]}")
        return result[0]
    else:
        logger.error(f"Transaction not found in DB | TXN_ID: {txn_id}")
        return None