class AtlasFile:
    def __init__(self, path, extension, tags=[], group='none', favorite=0):
        self.name = path.name
        self.path = path
        self.extension = extension
        self.tags = tags
        self.group = group
        self.favorite = favorite
