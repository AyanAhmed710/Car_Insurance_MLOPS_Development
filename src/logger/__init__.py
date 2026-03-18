import logging
import os
from from_root import from_root
from logging.handlers import RotatingFileHandler
from datetime import datetime



LOG_DIR="./logs"
MAX_LOG_SIZE=5*1024*1024
BACKUP_COUNT=3
LOG_FILE=f"{datetime.now().strftime('%m-%d-%Y-%H-%M-%S')}.log"


os.makedirs(LOG_DIR , exist_ok=True)
log_file_path=os.path.join(LOG_DIR,LOG_FILE)

def configure_logger():

    logger=logging.getLogger()
    logger.setLevel(logging.DEBUG)

    formatter=logging.Formatter("[ %(asctime)s] - %(name)s - %(levelname)s -%(message)s")

    file_handler=RotatingFileHandler(log_file_path , maxBytes=MAX_LOG_SIZE ,backupCount=BACKUP_COUNT)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    console_handler=logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.DEBUG)

    if not logger.handlers:
      logger.addHandler(file_handler)
      logger.addHandler(console_handler)


configure_logger()




