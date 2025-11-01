import logging
import os
from datetime import datetime

def get_my_logger():
    
    # Create logs directory if it doesn't exist
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    
    # Create log filename with just the date (not time)
    log_filename = f"{log_dir}/pipeline_{datetime.now().strftime('%Y%m%d')}.log"
    
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(),  # Console output
            logging.FileHandler(log_filename)  # File output - appends to existing file
        ]
    )
    logger = logging.getLogger()
    return logger