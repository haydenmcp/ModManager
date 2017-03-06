###############################################################################
#   @description: Module containing mods for skyrim.
#   @author: Hayden McParlane
###############################################################################
import os

TEMP_DIRECTORY = os.path.abspath(r".\tmp")
APP_MOD_DIRECTORY = os.path.abspath(r".\games")
APP_CONFIG_DIRECTORY = os.path.abspath(r".\configurations")
SKYRIM_APP_MOD_DIRECTORY = r"{0}\{1}".format(APP_MOD_DIRECTORY, "skyrim")
# SKYRIM_APP_MOD_DIRECTORY = r"C:\dev\personal\mods" # for laptop

BASE_STEAM_GAME_DIRECTORY = r"C:\personal\programs\steam\steamapps\common"
STEAM_SKYRIM_DIRECTORY = r"{0}\{1}".format(BASE_STEAM_GAME_DIRECTORY, "skyrim")
# STEAM_SKYRIM_DIRECTORY = r"C:\Users\hayde\Documents\tmp\skyrim"

SKYRIM_DATA_DIRECTORY = r"{0}\{1}".format(STEAM_SKYRIM_DIRECTORY, "data")
# SKYRIM_DATA_DIRECTORY = os.path.abspath(r"C:\dev\personal\mods\tmp") # for laptop

INSTALLED_MODS_CONFIG_FILE = r"{0}\{1}".format(APP_CONFIG_DIRECTORY, r"installed_mods.json")
