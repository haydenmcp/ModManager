###############################################################################
#   @description: Module containing mods for skyrim.
#   @author: Hayden McParlane
###############################################################################
import configparser
import os

################################################################################
#   Application Config
################################################################################
APP_MOD_DIR = os.path.abspath(r".\games")
APP_CONFIG_DIR = os.path.abspath(r".\configurations")
INSTALLED_MODS_CONFIG_FILE = r"{0}\{1}".format(APP_CONFIG_DIR, r"installed_mods.json")

APP_MOD_DIR_SKYRIM = r"{0}\{1}".format(APP_MOD_DIR, "skyrim")

################################################################################
#   Steam Config
################################################################################
STEAM_BASE_GAME_DIRECTORY = r"C:\personal\programs\steam\steamapps\common"
STEAM_GAME_CONFIG_DIR = r"C:\Users\hayde\Documents\My Games"

################################################################################
#   Skyrim Config
################################################################################
SKYRIM_BASE_DIR = r"{0}\{1}".format(STEAM_BASE_GAME_DIRECTORY, "skyrim")
SKYRIM_DATA_DIR = r"{0}\{1}".format(SKYRIM_BASE_DIR, "data")
SKYRIM_GAME_CONFIG_DIR = r"{0}\{1}".format(STEAM_GAME_CONFIG_DIR, "skyrim")
SKYRIM_INI_FILE = r"{0}\{1}".format(SKYRIM_GAME_CONFIG_DIR, "Skyrim.ini")
SKYRIM_PREFS_INI_FILE = r"{0}\{1}".format(SKYRIM_GAME_CONFIG_DIR, "SkyrimPrefs.ini")
SKYRIM_ENBLOCAL_INI_FILE = r"{0}\{1}".format(SKYRIM_GAME_CONFIG_DIR, "enblocal.ini")
