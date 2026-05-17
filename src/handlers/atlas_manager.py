

from pathlib import Path
from classes.atlas import AtlasFile, AtlasFolder
from database.db_access import add_to_db, get_entries_values


class AtlasManager:
    ''' Controls the Atlas System Processes including the creation of Atlas Entries (files/folders) and navigation.'''
    atlas_root = Path.home() / "documents" / "atlas storage"

    def __init__(self, directory=atlas_root):
        self.directory = directory
        self.current_view = directory

    def get_all_files(self):
        return self.atlas_root.rglob("*")

    def create_atlas_entries(self):
        ''' Converts filesystem within Atlas Storage into ATLAS entry objects. '''

        all_files = self.get_all_files()

        for f in all_files:
            if f.name != 'desktop.ini':
                if f.is_file():
                    # turn f into an AtlasFile class instance
                    atlas_entry = AtlasFile(f)
                if f.is_dir():
                    # turn f into an AtlasFolder class instance
                    atlas_entry = AtlasFolder(f)
                # add entry to the 'entry save location'
                add_to_db(atlas_entry)

    def change_dir(self, new_dir, direction):
        if direction == 'f':
            self.current_view = self.current_view / new_dir
        elif direction == 'b':
            self.current_view = self.current_view.parent

    def view_current_dir(self):
        for entry in get_entries_values():
            if entry.path.parent == self.current_view:
                print(entry)
