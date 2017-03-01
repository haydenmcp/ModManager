from modcore import SkyrimModInstallationManager

from applogger import ModiLogger
log = ModiLogger()

_mod_install_manager = SkyrimModInstallationManager()

class ModInstallerClient(object):

    def install(self, mods):
        if mods is not None and len(mods) > 0:
            for mod in mods:
                _mod_install_manager.add(mod)
            _mod_install_manager.install_mods()
