class ModBase(object):

    def relationships(self):
        '''Should return relationships to other mods (i.e, Dependencies, Superiority, etc)'''
        return list()

    def run_post_processing(self):
        '''Processing that needs to occur after installation should be placed here'''
        pass


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
