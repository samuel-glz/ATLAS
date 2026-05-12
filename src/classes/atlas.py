class Atlas:
    def __init__(self, path, type, tags=None, group='none', favorite=0):
        self.name = path.name
        self.type = type
        self.path = path
        self.tags = tags or []
        self.group = group
        self.favorite = favorite


class AtlasFolder(Atlas):
    def __init__(self, path, tags=None, group='none', favorite=0):
        super().__init__(path, 'folder', tags, group, favorite)


class AtlasFile(Atlas):
    def __init__(self, path, extension, tags=None, group='none', favorite=0):
        super().__init__(path, 'file', tags, group, favorite)
        self.extension = extension
