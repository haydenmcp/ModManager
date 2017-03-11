###############################################################################
#   @description: Module containing mods for skyrim.
#   @author: Hayden McParlane
###############################################################################

from client import ModManagerClient
import skyrim_packages

def run_skyrim_install():

    client = ModManagerClient()
    client.install_mod_packages([
        skyrim_packages.FoundationPatchPack(),
        skyrim_packages.RealisticWorldWithTrueVisionENBVisionENB(),
        skyrim_packages.ActorModelAndTexturePack(),
        skyrim_packages.HarshSkyrimImmersionPack(),
        skyrim_packages.WeaponAndArmorPack(),
    ])
    # client.install_mod_packages([
    #     skyrim_packages.TestPackage(),
    # ])

if __name__ == '__main__':
    run_skyrim_install()
