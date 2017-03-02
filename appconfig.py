import os

TEMP_DIRECTORY = os.path.abspath(r".\tmp")
APP_MOD_DIRECTORY = os.path.abspath(r".\games")
SKYRIM_APP_MOD_DIRECTORY = r"{0}\{1}".format(APP_MOD_DIRECTORY, "skyrim")
# SKYRIM_APP_MOD_DIRECTORY = r"C:\dev\personal\mods" # for laptop

BASE_STEAM_GAME_DIRECTORY = r"C:\personal\programs\steam\steamapps\common"
STEAM_SKYRIM_DIRECTORY = r"{0}\{1}".format(BASE_STEAM_GAME_DIRECTORY, "skyrim")

# SKYRIM_DATA_DIRECTORY = r"{0}\{1}".format(STEAM_SKYRIM_DIRECTORY, "data")
SKYRIM_DATA_DIRECTORY = os.path.abspath(r"C:\personal\gaming\nmm\mods\tmp")
# SKYRIM_DATA_DIRECTORY = os.path.abspath(r"C:\dev\personal\mods\tmp") # for laptop
