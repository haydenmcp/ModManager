class ModBase(object):

    def install(self):
        self.setup()
        self.apply()
        self.cleanup()

    def setup(self):
        pass

    def apply(self):
        raise NotImplementedError()

    def cleanup(self):
        pass

    def relationships(self):
        return list()

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