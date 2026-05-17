class Atlas:
    def __init__(self, path, type, tags=None, favorite=0):
        self.type = type
        self.path = path
        self.name = self.path.name
        self.tags = tags or []
        self.favorite = favorite

    def __repr__(self):
        return f'AtlasEntry:(Path: {self.name} | Type: {self.type})'

    def view_tags(self):
        return self.tags

    def add_tag(self, tag):
        self.tags.append(tag)

    def remove_tag(self, tag):
        self.tags.remove(tag)


class AtlasFolder(Atlas):
    def __init__(self, path, tags=None, favorite=0):
        super().__init__(path, 'folder', tags, favorite)


class AtlasFile(Atlas):
    def __init__(self, path, tags=None, favorite=0):
        super().__init__(path, 'file', tags, favorite)
        suffix = path.suffix
        self.extension = suffix
