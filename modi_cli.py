###############################################################################
#   @description: Module containing mods for skyrim.
#   @author: Hayden McParlane
###############################################################################

from client import ModManagerClient
import skyrim_packages

def run_skyrim_install():

    client = ModManagerClient()
    # client.install_mod_packages([
    #     skyrim_packages.FoundationPatchPack(),
    #     skyrim_packages.RealisticWorldWithRealVisionENB(),
    #     skyrim_packages.HarshSkyrimImmersionPack()
    # ])
    client.install_mod_packages([
        skyrim_packages.TemporaryPackage()
    ])

if __name__ == '__main__':
    run_skyrim_install()
