from zipfile import ZipFile
import appconfig
import copy
import modbase
import os

# TODO: Add traceback to logging module. Shouldn't need to include this in every module with logging.
import traceback
from applogger import ModiLogger
log = ModiLogger()

class ModInstallationManager(object):

    def add(self, mod_name):
        '''Add a mod to be installed'''
        raise NotImplementedError()

    def install_mods(self):
        '''Run installation of all added mods.'''
        raise NotImplementedError()

###############################################################################
#   Skyrim
###############################################################################

INSTALLED = True
PENDING = False
class SkyrimModInstallationManager(ModInstallationManager):

    # TODO: Make mods singletons because mod should be used for mappings. Otherwise, map
    # TODO: thinks mod is different even if same.
    def __init__(self):
        self._installation_modifications = dict()
        self._installation_progress = dict()
        self._mods_to_install = dict()

    def add(self, mod):
        if mod is not None:
            mod_name = mod.__class__.__name__
            compressed_files = compressed_members(appconfig.SKYRIM_APP_MOD_DIRECTORY, mod_name)
            files_to_install = remove_directories(compressed_files)
            self._set_required_file_modifications(mod, files_to_install)
            self._add_mod_for_install(mod)
            self._set_mod_progress(mod, PENDING)

    def install_mods(self):
        for mod in self._get_mods_to_install():
            self._install(mod)

    def _install(self, mod):
        if mod is not None and isinstance(mod, modbase.ModBase):
            mod_name = mod.__class__.__name__
            if not self._is_installed(mod):
                try:
                    log.info("Installing mod: {0}".format(mod_name))
                    for relationship in mod.relationships():
                        self._handle(relationship)
                    with ZipFile(compressed_filename(appconfig.SKYRIM_APP_MOD_DIRECTORY, mod_name)) as archive:
                        files_to_install = self._get_required_file_modifications(mod)
                        for file in files_to_install:
                            log.debug("File: {0}".format(file))
                            archive.extract(file, appconfig.SKYRIM_DATA_DIRECTORY)
                    log.info("Installation Successful: {0}".format(mod_name))
                    self._set_mod_progress(mod, INSTALLED)
                except Exception as e:
                    log.error("Installation Failed: {0}\n\t{1}\n".format(mod_name, traceback.format_exc()))
            else:
                log.debug("Mod already installed: {0}".format(mod_name))

    def _handle(self, relationship):
        if relationship is not None and isinstance(relationship, modbase.Relationship):
            # TODO: handle Incompatibility relationship
            if isinstance(relationship, modbase.Dependency):
                dependency = relationship.target_mod
                log.info("Resolving dependency on mod: {0}".format(dependency.__class__.__name__))
                if self._is_installed(dependency):
                    log.info("Dependency already installed: {0}".format(dependency.__class__.__name__))
                else:
                    self._install(dependency)
            elif isinstance(relationship, modbase.Superiority):
                superior_mod = relationship.target_mod
                inferior_mod = relationship.source_mod
                log.info("Resolving superiority of mod: {0}".format(superior_mod.__class__.__name__))
                files_to_avoid = self._get_required_file_modifications(superior_mod)
                log.debug("Superior files for {0}: {1}".format(superior_mod.__class__.__name__, files_to_avoid))
                inferior_mod_files = self._get_required_file_modifications(inferior_mod)
                log.debug("Inferior files for {0}: {1}".format(inferior_mod.__class__.__name__, inferior_mod_files))
                updated_files_to_modify = set_difference_zipinfos(inferior_mod_files, files_to_avoid)
                log.debug("Updated {0} files: {1}".format(inferior_mod.__class__.__name__, inferior_mod_files))
                self._set_required_file_modifications(inferior_mod, updated_files_to_modify)

    def _is_installed(self, mod):
        # TODO: Refactor to use enums. True/False is misleading. What if mod doesn't exist in dict? Returns None which evals to false.
        # TODO: This will result in system assuming that mod is pending install.
        return self._installation_progress[mod.__class__.__name__]

    def _set_mod_progress(self, mod, progress_value):
        self._installation_progress[mod.__class__.__name__] = progress_value

    def _set_required_file_modifications(self, mod, zipinfos):
        self._installation_modifications[mod.__class__.__name__] = zipinfos

    def _get_required_file_modifications(self, mod):
        return self._installation_modifications[mod.__class__.__name__]

    def _add_mod_for_install(self, mod):
        self._mods_to_install[mod.__class__.__name__] = mod

    def _get_mod_for_install(self, mod):
        return self._mods_to_install[mod.__class__.__name__]

    def _get_mods_to_install(self):
        return self._mods_to_install.values()

###############################################################################
#   Helper functions
###############################################################################
def set_difference_zipinfos(zipinfos1, zipinfos2):
    # TODO: Better naming
    new1 = copy.deepcopy(zipinfos1)
    new2 = copy.deepcopy(zipinfos2)
    for info2 in new2:
        for info1 in new1:
            if info1.filename == info2.filename:
                new1.remove(info1)
    return new1

def compressed_members(game_archive_directory, mod_name):
    if (game_archive_directory is not None and len(game_archive_directory) > 0) and (mod_name is not None and len(mod_name) > 0):
        compressed_files = list()
        with ZipFile(compressed_filename(game_archive_directory, mod_name)) as archive:
            return archive.infolist()
    else:
        raise ValueError()

def compressed_filename(game_mod_directory, mod_name):
    return r"{0}\{1}.zip".format(game_mod_directory, mod_name)

def remove_directories(zipinfos):
    files_containing_extensions = list()
    if zipinfos is not None and len(zipinfos) > 0:
        files_containing_extensions = [info for info in zipinfos if has_extension(info.filename)]
    return files_containing_extensions

def has_extension(filename):
    result = False
    if filename is not None:
        split_filename = os.path.splitext(filename)
        result = split_filename[1] not in ""
    return result


