import logging
import os
import datetime
import sys

logger = None  # 🔥 global logger


def setup_logger():
    global logger

    # ✅ If already created, reuse it
    if logger:
        return logger

    log_dir = "reports/logs"
    os.makedirs(log_dir, exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(log_dir, f"test_execution_{timestamp}.log")

    logger = logging.getLogger("payment_logger")
    logger.setLevel(logging.INFO)

    # Clear old handlers
    if logger.hasHandlers():
        logger.handlers.clear()

    file_handler = logging.FileHandler(log_file)
    console_handler = logging.StreamHandler(sys.stdout)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.info(f"Log file created: {log_file}")

    return logger