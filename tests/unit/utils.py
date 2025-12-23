# utils.py

import os
import logging
from datetime import datetime

def get_current_timestamp():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def create_directory_if_not_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

def configure_logging(log_file):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.FileHandler(log_file), logging.StreamHandler()]
    )