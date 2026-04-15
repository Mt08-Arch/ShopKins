import logging
from logging.handlers import RotatingFileHandler

def setup_logger():
    handler = RotatingFileHandler('logs/bot.log', maxBytes=10**6, backupCount=5)
    logging.basicConfig(handlers=[handler], level=logging.INFO)
