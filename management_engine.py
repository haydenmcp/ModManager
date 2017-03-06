###############################################################################
#   @description: The mod management engine responsible for executing
#   mod installation, etc.
#
#   @author: Hayden McParlane
###############################################################################
from applogger import ModManagementLogger

log = ModManagementLogger()

from common import *
import configparser
import enum
import appconfig
import copy
import json
import modcore
import os
from zipfile import ZipFile, ZipInfo


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
        self._mod_installation_history = self._read_from_install_history()
        self._mod_installation_status = dict()
        self._registered_file_modifications = dict()
        self._game_mod_dir = appconfig.APP_MOD_DIR_SKYRIM
        self._config_modifications = dict()

    def install_mod_packages(self, mod_packages):
        if is_populated(mod_packages):
            self._map_package_relationships(mod_packages)
            for mod_package in mod_packages:
                if is_valid_package(mod_package):
                    self._install_mods(mod_package.mods())
                    self._update_game_configurations()
            self._record_activity_in_install_history()

    def install_is_pending(self, mod):
        if is_valid_mod(mod):
            mod_is_currently_pending = self._mod_installation_status[mod] == InstallStatus.PENDING
            mod_was_previously_installed = self.is_in_install_history(mod)
            return mod_is_currently_pending and not mod_was_previously_installed

    # TODO: Better name?
    def is_in_install_history(self, mod):
        mod_was_previously_installed = False
        if mod.__class__.__name__ in self._mod_installation_history:
            mod_was_previously_installed = True
        return mod_was_previously_installed

    def _install_mods(self, mods):
        if is_populated(mods):
            for mod in mods:
                if is_valid_mod(mod):
                    if self.install_is_pending(mod):
                        self._handle_dependencies(mod.dependencies())
                        self._handle_superiorities(mod.superiorities())
                        self._install_mod(mod)
                        self._handle_configurations(mod.configurations())
                        # TODO: *** Need to handle patches such that install of modA not requiring patch,
                        # TODO: followed by subsequent install of modB which suddenly requires that
                        # TODO: modA is patched, is possible. Currently, this would be recorded as
                        # TODO: installed and wouldn't execute if-statement resulting in patch
                        # TODO: not being added.
                        self._handle_patches(mod.patches())
                    else:
                        log.info("Mod Already Installed: {0}".format(mod.__class__.__name__))

    # TODO: This method cant be called directly. If done that way, dependency resolution
    # TODO: occurs out of order because dependency install is direct vs. going through
    # TODO: recursive dependency resolution on those dependencies. Modify?
    def _install_mod(self, mod):
        if is_valid_mod(mod):
            log.info("Installing mod: {0}".format(mod.__class__.__name__))
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
            log.info("Installation Successful: {0}".format(mod.__class__.__name__))

    def _handle_dependencies(self, dependencies):
        if is_populated(dependencies):
            for dependency in dependencies:
                if is_valid_dependency(dependency):
                    self._install_mods([dependency.target_mod])

    def _handle_configurations(self, configurations):
        if is_populated(configurations):
            for filename, config_updates in configurations.items():
                self._add_config_modification(filename, config_updates)

    def _handle_patches(self, patches):
        if is_populated(patches):
            for patch in patches:
                if is_valid_patch(patch):
                    mod_to_patch_if_found = patch.patch_dependency
                    if self._is_registered(mod_to_patch_if_found):
                        self._install_mods([patch.patch_mod])

    def _handle_superiorities(self, superiorities):
        if is_populated(superiorities):
            for superiority in superiorities:
                if is_valid_superiority(superiority):
                    superior_mod = superiority.target_mod
                    inferior_mod = superiority.source_mod
                    log.debug("Configuring superiority of mod: {0}".format(superior_mod.__class__.__name__))
                    files_to_avoid = self._registered_file_modifications[superior_mod]
                    log.debug("Superior files: {0}".format(files_to_avoid))
                    inferior_mod_files = self._registered_file_modifications[inferior_mod]
                    log.debug("Inferior files: {0}".format(inferior_mod_files))
                    updated_files_to_modify = set_difference_zipinfos(inferior_mod_files, files_to_avoid)
                    log.debug("Updated inferior files: {0}".format(updated_files_to_modify))
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
                    self._map_mod_relationships([dependency.target_mod])

    def _register_patches(self, mod):
        if is_valid_mod(mod):
            log.debug("Registering Patches: {0}".format(mod.patches()))
            for patch in mod.patches():
                if is_valid_patch(patch):
                    self._map_mod_relationships([patch.patch_mod])

    def _register_mod(self, mod):
        if is_valid_mod(mod):
            compressed_entities = compressed_members(self._game_mod_dir, mod)
            self._update_file_modifications(mod, isolate_files(compressed_entities))
            self._update_installation_status(mod, InstallStatus.PENDING)

    def _update_file_modifications(self, mod, zipinfos):
        if is_valid_mod(mod):  # Do NOT check zero case for zipinfos. Mods files "to add" can be empty list.
            self._registered_file_modifications[mod] = zipinfos

    def _is_registered(self, mod):
        return is_valid_mod(mod) and mod in self._registered_file_modifications

    def _update_installation_status(self, mod, status):
        if is_valid_mod(mod) and isinstance(status, InstallStatus):
            self._mod_installation_status[mod] = status

    def _record_activity_in_install_history(self):
        try:
            log.info(r"Writing installed mods to config file: {0}".format(appconfig.INSTALLED_MODS_CONFIG_FILE))
            self._update_installation_history()
            with open(appconfig.INSTALLED_MODS_CONFIG_FILE, 'w') as installed_mods_config_file:
                json.dump(self._mod_installation_history, installed_mods_config_file)
        except Exception:
            log.error("Failed to write installed mods to: {0}".format(appconfig.INSTALLED_MODS_CONFIG_FILE))

    def _read_from_install_history(self):
        configurations = dict()
        try:
            log.info(
                r"Reading currently installed mods from config file: {0}".format(appconfig.INSTALLED_MODS_CONFIG_FILE))
            with open(appconfig.INSTALLED_MODS_CONFIG_FILE, 'r') as installed_mods_config_file:
                # TODO: Refactor such that more readable.
                configurations = json.load(installed_mods_config_file)
                for mod_name, status_string in configurations.items():
                    configurations[mod_name] = InstallStatus[status_string]
        except Exception:
            log.warning(r"An error occurred while trying to access installed mods. Assuming fresh install.")
        return configurations

    def _update_installation_history(self):
        # TODO: Refactor such that more readable.
        string_keyed_mod_dict = dict()
        for mod_name, status_object in self._mod_installation_history.items():
            self._mod_installation_history[mod_name] = status_object.name
        for mod, status in self._mod_installation_status.items():
            # TODO: May be better to represent status as separate dicts and to transfer mods
            # TODO: from one to the other (i.e, pending -> complete dict). That way don't
            # TODO: need to iterate over all mods every time history is updated.
            if status is InstallStatus.COMPLETE:
                string_keyed_mod_dict[mod.__class__.__name__] = status.name
        for mod_name, status_name in string_keyed_mod_dict.items():
            if mod_name not in self._mod_installation_history:
                self._mod_installation_history[mod_name] = status_name

    def _add_config_modification(self, filename, config_updates):
        if is_populated(filename) and is_populated(config_updates):
            if not self._has_config_updates(filename):
                self._config_modifications[filename] = configparser.ConfigParser()
            self._config_modifications[filename].read_dict(config_updates)

    def _has_config_updates(self, filename):
        if is_populated(filename):
            return filename in self._config_modifications

    def _update_game_configurations(self):
        if is_populated(self._config_modifications):
            for config_filename, config_modifications in self._config_modifications.items():
                log.info(r"Updating configuration file: {0}".format(config_filename))
                if is_populated(config_filename):
                    config_file_contents = config_file(config_filename)
                    self._merge_config_files(config_file_contents, config_modifications)
                    with open(config_filename, 'w') as target_config_file:
                        config_file_contents.write(target_config_file)
                log.info(r"Configuration file update successful: {0}".format(config_filename))

    def _merge_config_files(self, current_config, config_updates):
        if isinstance(current_config, configparser.ConfigParser) and isinstance(config_updates, configparser.ConfigParser):
            updated_sections = config_updates.sections()
            for section in updated_sections:
                if is_populated(section):
                    if not current_config.has_section(section):
                        current_config.add_section(section)
                    for option, value in config_updates.items(section):
                        if is_populated(option) and is_populated(value):
                            log.info("\tOption: {0}, Value: {1}".format(option, value))
                            current_config.set(section, option, value)
        return current_config



###############################################################################
#   Helper functions
###############################################################################
class InstallStatus(enum.Enum):
    PENDING = "PENDING",
    COMPLETE = "COMPLETE"


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


def config_file(filename):
    config = configparser.ConfigParser()
    with open(filename) as file:
        config.read_file(file)
    return config
