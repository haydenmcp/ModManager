from zipfile import ZipFile
import appconfig
import modbase
import os

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
class SkyrimModInstallationManager(ModInstallationManager):

    def __init__(self):
        self._installation_modifications = dict()

    def add(self, mod):
        if mod is not None:
            compressed_files = compressed_members(appconfig.SKYRIM_APP_MOD_DIRECTORY, mod.__class__.__name__)
            files_to_install = remove_directories(compressed_files)
            self._installation_modifications[mod] = frozenset(files_to_install)

    def install_mods(self):
        for mod in self._installation_modifications.keys():
            self._install(mod)

    def _install(self, mod):
        if mod is not None and isinstance(mod, modbase.ModBase):
            try:
                mod_name = mod.__class__.__name__
                log.info("Installing mod: {0}".format(mod_name))
                for relationship in mod.relationships():
                    self._handle(relationship)
                with ZipFile(compressed_filename(appconfig.SKYRIM_APP_MOD_DIRECTORY, mod_name)) as archive:
                    files_to_install = self._installation_modifications[mod]
                    for file in files_to_install:
                        log.info("File: {0}".format(file))
                        archive.extract(file, appconfig.SKYRIM_DATA_DIRECTORY)
                log.info("Installation Successful: {0}".format(mod_name))
            except Exception as e:
                log.error("Installation Failed: {0}\n\n{1}".format(mod_name, e))


    def _handle(self, relationship):
        if relationship is not None and isinstance(relationship, modbase.Relationship):
            # TODO: handle Incompatibility relationship
            if isinstance(relationship, modbase.Dependency):
                dependency = relationship.target_mod
                log.info("Resolving dependency on mod: {0}".format(dependency.__class__.__name__))
                self._install(dependency)
            elif isinstance(relationship, modbase.Superiority):
                superior_mod = relationship.target_mod
                inferior_mod = relationship.source_mod
                log.info("Resolving superiority of mod: {0}".format(superior_mod.__class__.__name__))
                files_to_avoid = self._installation_modifications[superior_mod]
                log.info("Superior files for {0}: {1}".format(superior_mod.__class__.__name__, files_to_avoid))
                inferior_mod_files = self._installation_modifications[inferior_mod]
                log.info("Inferior files for {0}: {1}".format(inferior_mod.__class__.__name__, inferior_mod_files))
                updated_files_to_modify = inferior_mod_files - files_to_avoid
                log.info("Updated {0} files: {1}".format(inferior_mod.__class__.__name__, inferior_mod_files))
                self._installation_modifications[inferior_mod] = updated_files_to_modify

###############################################################################
#   Helper functions
###############################################################################
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


