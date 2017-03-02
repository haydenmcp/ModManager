###############################################################################
#   @description: Module containing mods for skyrim.
#   @author: Hayden McParlane
###############################################################################

from common import *
from management_engine import SkyrimModInstallationManager

from applogger import ModiLogger
log = ModiLogger()

_mod_manager = SkyrimModInstallationManager()

class ModManagerClient(object):

    def install_mods(self, mod_packages):
        if is_populated(mod_packages):
            _mod_manager.install_mod_packages(mod_packages)

    def install(self, mods):
        if is_populated(mods):
            _mod_manager.install_mods(mods)
