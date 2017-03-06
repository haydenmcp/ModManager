###############################################################################
#   @description: Client used to install mod packages.
#   @author: Hayden McParlane
###############################################################################

from common import *
from management_engine import SkyrimModManager

from applogger import ModManagementLogger
log = ModManagementLogger()

_mod_manager = SkyrimModManager()

class ModManagerClient(object):

    def install_mod_packages(self, mod_packages):
        if is_populated(mod_packages):
            _mod_manager.install_mod_packages(mod_packages)
