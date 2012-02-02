import replicates

class Recipe(object):

    def __init__(self, buildout, name, options):
        self.buildout = buildout
        self.name = name
        self.options = options

    def install(self):
        staging = self.options['staging']
        replicates.main(staging)
        
    def update(self):
        return self.install()