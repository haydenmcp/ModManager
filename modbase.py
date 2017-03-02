###############################################################################
#   @description: Module containing mods for skyrim.
#   @author: Hayden McParlane
###############################################################################

class ModBase(object):

    def install_directory(self):
        raise NotImplementedError()

    def dependencies(self):
        '''Mods declared in this collection represent dependencies which must be installed for
        this mod to be included.'''
        return list()

    def superiorities(self):
        '''Mods declared in this collection are viewed as superior meaning that superior mod
        files will not be overwritten by this mods files.'''
        return frozenset()

    def patches(self):
        '''Patch dependencies are declared in this collection.'''
        return frozenset()

    def run_post_processing(self):
        '''Processing that needs to occur after installation should be placed here'''
        pass


class Patch(object):
    def __init__(self, subject_mod, patch_mod, patch_dependency):
        self.subject_mod = subject_mod
        self.patch_mod = patch_mod
        self.patch_dependency = patch_dependency

###################################################################################
#   Graph Definitions
###################################################################################
class Relationship(object):

    def __init__(self, source_mod, target_mod):
        self.source_mod = source_mod
        self.target_mod = target_mod

class Superiority(Relationship):

    def __init__(self, source_mod, target_mod):
        Relationship.__init__(self, source_mod, target_mod)

class Dependency(Relationship):

    def __init__(self, source_mod, target_mod):
        Relationship.__init__(self, source_mod, target_mod)

