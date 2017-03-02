###############################################################################
#   @description: The mod management engine responsible for executing
#   mod installation, etc.
#
#   @author: Hayden McParlane
###############################################################################
from common import *
import enum
from zipfile import ZipFile, ZipInfo
import appconfig
import copy
import modcore
import os

# TODO: Add traceback to logging module. Shouldn't need to include this in every module with logging.
import traceback
from applogger import ModiLogger

log = ModiLogger()


class ModManager(object):
    def install_mod_packages(self, mod_packages):
        raise NotImplementedError()

    def install_mods(self, mods):
        raise NotImplementedError()


###############################################################################
#   Skyrim
###############################################################################
class SkyrimModManager(ModManager):
    def __init__(self):
        self._mod_installation_status = dict()
        self._registered_file_modifications = dict()
        self._game_mod_dir = appconfig.SKYRIM_APP_MOD_DIRECTORY

    def install_mod_packages(self, mod_packages):
        if is_populated(mod_packages):
            self._map_package_relationships(mod_packages)
            for mod_package in mod_packages:
                if is_valid_package(mod_package):
                    self._install_mods(mod_package.mods())

    def _install_mods(self, mods):
        if is_populated(mods):
            for mod in mods:
                if is_valid_mod(mod):
                    if self.is_install_pending(mod):
                        log.info("Installing mod: {0}".format(mod.__class__.__name__))
                        self._handle_dependencies(mod.dependencies())
                        self._handle_superiorities(mod.superiorities())
                        self._install_mod(mod)
                        self._handle_patches(mod.patches())
                        log.info("Installation Successful: {0}".format(mod.__class__.__name__))
                    else:
                        log.debug("Mod Already Installed: {0}".format(mod.__class__.__name__))

    def _install_mod(self, mod):
        if is_valid_mod(mod):
            install_dir = mod.install_directory()
            log.info("Extracting files to: {0}".format(install_dir))
            with ZipFile(compressed_filename(self._game_mod_dir, mod.__class__.__name__)) as archive:
                files_to_install = self._registered_file_modifications[mod]
                if is_populated(files_to_install):
                    for file in files_to_install:
                        log.debug("\t{0}".format(file.filename))
                        archive.extract(file, install_dir)
            mod.run_post_processing()
            self._update_installation_status(mod, InstallStatus.COMPLETE)

    def _handle_dependencies(self, dependencies):
        if is_populated(dependencies):
            for dependency in dependencies:
                if is_valid_dependency(dependency):
                    self._install_mod(dependency.target_mod)

    def _handle_patches(self, patches):
        if is_populated(patches):
            for patch in patches:
                if is_valid_patch(patch):
                    mod_to_patch_if_found = patch.patch_dependency
                    if self._is_registered(mod_to_patch_if_found):
                        self._install_mod(patch.patch_mod)

    def _handle_superiorities(self, superiorities):
        if is_populated(superiorities):
            for superiority in superiorities:
                if is_valid_superiority(superiority):
                    superior_mod = superiority.target_mod
                    inferior_mod = superiority.source_mod
                    log.info("Configuring superiority of mod: {0}".format(superior_mod.__class__.__name__))
                    files_to_avoid = self._registered_file_modifications[superior_mod]
                    inferior_mod_files = self._registered_file_modifications[inferior_mod]
                    updated_files_to_modify = set_difference_zipinfos(inferior_mod_files, files_to_avoid)
                    self._update_file_modifications(inferior_mod, updated_files_to_modify)

    def _map_package_relationships(self, mod_packages):
        if is_populated(mod_packages):
            for mod_package in mod_packages:
                if is_valid_package(mod_package):
                    self._map_mod_relationships(mod_package.mods())

    def _map_mod_relationships(self, mods):
        if is_populated(mods):
            for mod in mods:
                if is_valid_mod(mod) and not self._is_registered(mod):
                    log.debug("Registering mod: {0}".format(mod.__class__.__name__))
                    self._register_dependencies(mod)
                    self._register_mod(mod)
                    self._register_patches(mod)

    def _register_dependencies(self, mod):
        if is_valid_mod(mod):
            for dependency in mod.dependencies():
                if is_valid_dependency(dependency):
                    self._map_mod_relationships(dependency.target_mod)

    def _register_patches(self, mod):
        if is_valid_mod(mod):
            for patch in mod.patches():
                if is_valid_patch(patch):
                    self._map_mod_relationships(patch.patch_mod)

    def _register_mod(self, mod):
        if is_valid_mod(mod):
            compressed_entities = compressed_members(self._game_mod_dir, mod)
            self._update_file_modifications(mod, isolate_files(compressed_entities))
            self._update_installation_status(mod, InstallStatus.PENDING)

    def _update_file_modifications(self, mod, zipinfos):
        if is_valid_mod(mod) and is_populated(zipinfos) and isinstance(zipinfos[0], ZipInfo):
            self._registered_file_modifications[mod] = zipinfos

    def _is_registered(self, mod):
        return is_valid_mod(mod) and self._registered_file_modifications[mod] is not None

    def _update_installation_status(self, mod, status):
        if is_valid_mod(mod) and isinstance(status, InstallStatus):
            self._mod_installation_status[mod] = status

    def is_install_pending(self, mod):
        if is_valid_mod(mod):
            return self._mod_installation_status[mod] == InstallStatus.PENDING


###############################################################################
#   Helper functions
###############################################################################
class InstallStatus(enum.Enum):
    PENDING = 1,
    COMPLETE = 2


###############################################################################
#   Helper functions
###############################################################################
def is_valid_package(mod_package):
    return mod_package is not None and isinstance(mod_package, modcore.ModPackage)


def is_valid_mod(mod):
    return mod is not None and isinstance(mod, modcore.ModBase)


# TODO: Should these be moved to modebase?
def is_valid_patch(patch):
    return (patch is not None and isinstance(patch, modcore.Patch)
            and is_valid_mod(patch.subject_mod)
            and is_valid_mod(patch.patch_mod)
            and is_valid_mod(patch.patch_dependency))


def is_valid_dependency(dependency):
    return (dependency is not None and isinstance(dependency, modcore.Dependency)
            and is_valid_mod(dependency.source_mod)
            and is_valid_mod(dependency.target_mod))


def is_valid_superiority(superiority):
    return superiority is not None and isinstance(superiority, modcore.Superiority)


def set_difference_zipinfos(zipinfos1, zipinfos2):
    new1 = copy.deepcopy(zipinfos1)
    new2 = copy.deepcopy(zipinfos2)
    for info2 in new2:
        for info1 in new1:
            if info1.filename == info2.filename:
                new1.remove(info1)
    return new1


def compressed_members(game_archive_directory, mod):
    if is_populated(game_archive_directory) and is_valid_mod(mod):
        with ZipFile(compressed_filename(game_archive_directory, mod.__class__.__name__)) as archive:
            return archive.infolist()
    else:
        raise ValueError()


def compressed_filename(game_mod_directory, mod_name):
    return r"{0}\{1}.zip".format(game_mod_directory, mod_name)


def isolate_files(zipinfos):
    files_containing_extensions = list()
    if is_populated(zipinfos):
        files_containing_extensions = [info for info in zipinfos if has_extension(info.filename)]
    return files_containing_extensions


def has_extension(filename):
    result = False
    if filename is not None:
        split_filename = os.path.splitext(filename)
        result = split_filename[1] not in ""
    return result
