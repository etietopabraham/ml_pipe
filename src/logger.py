import logging, os
from datetime import datetime

FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
file_path = os.path.join(os.getcwd(), "log", FILE_NAME)
os.makedirs(file_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(file_path, FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='%(asctime)s %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


# Test
# if __name__ == "__main__":
#     logging.info("Logging has started")
