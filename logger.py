import logging
from datetime import datetime

def __get_logger():

    __logger = logging.getLogger('logger')
    formatter = logging.Formatter('[%(asctime)s]\t [%(levelname)s]\t : %(message)s)')

    stream_handler = logging.StreamHandler()
    file_handler = logging.FileHandler('./logger.log')

    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    return __logger

def loggingSerial(_text):
    msgForm = str('[serial]\t >> {text}').format(text=_text)
    logging.info(msgForm)

def loggingWebSocket(_text):
    msgForm = str('[webSocket]\t >> {text}').format(text=_text)
    logging.info(msgForm)

def loggingDetect(_text):
    msgForm = str('[detect]\t >> {text}').format(text=_text)
    logging.info(msgForm)

def loggingActive(_text):
    msgForm = str('[active]\t >> {text}').format(text=_text)
    logging.info(msgForm)