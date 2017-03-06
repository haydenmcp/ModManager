###############################################################################
#   @description: The application logger with standard configurations.
#   @author: Hayden McParlane
###############################################################################

import logging
import traceback

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class ModManagementLogger(object):

    def debug(self, msg):
        logging.debug(msg)

    def info(self, msg):
        logging.info(msg)

    def warning(self, msg):
        logging.warning(msg)

    def error(self, msg):
        msg = "{0}\n\t{1}".format(msg, traceback.format_exc())
        logging.error(msg)

    def critical(self, msg):
        logging.critical(msg)