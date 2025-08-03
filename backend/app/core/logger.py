import os
import logging

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler(f"{log_dir}/app.log"),  
        logging.StreamHandler()                
    ]
)

logger = logging.getLogger("book_logger")
