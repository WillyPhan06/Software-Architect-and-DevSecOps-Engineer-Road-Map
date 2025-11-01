import logging

logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Script started")

try:
    with open("data.csv", "r") as f:
        lines = f.readlines()
        logging.info(f"Read {len(lines)} lines successfully.")
except FileNotFoundError as e:
    logging.error(f"File not found: {e}")
except Exception as e:
    logging.exception("Unexpected error occurred")
finally:
    logging.info("Script finished.")
