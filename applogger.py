import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class ModiLogger(object):

    def debug(self, msg):
        logging.debug(msg)

    def info(self, msg):
        logging.info(msg)

    def warning(self, msg):
        logging.warning(msg)

    def error(self, msg):
        logging.error(msg)

    def critical(self, msg):
        logging.critical(msg)