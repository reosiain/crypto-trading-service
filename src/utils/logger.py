import os
from loguru import logger

format_string = "<green>{time:DD.MM.YY HH:mm:ss}</green> | <level>{level: <8}</level>|<cyan>{function}</cyan> - <level>{message}</level>"

logger.add(os.getenv('LOGGER_PATH'), format=format_string, rotation="50 MB")
log = logger
