###############################################################################
#   @description: Client used to install mod packages.
#   @author: Hayden McParlane
###############################################################################

from common import *
from management_engine import SkyrimModInstallationManager

from applogger import ModiLogger
log = ModiLogger()

_mod_manager = SkyrimModInstallationManager()

class ModManagerClient(object):

    def install_mod_packages(self, mod_packages):
        if is_populated(mod_packages):
            _mod_manager.install_mod_packages(mod_packages)
