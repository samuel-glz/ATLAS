
from pathlib import Path
from file_navigation import *
from classes.atlas import AtlasFile, AtlasFolder

atlas_path = Path.home() / "documents" / "atlas storage"

# TODO: Later this will be replaced with persistent storage (Local then Cloud).
atlas_entry = {}


def view_atlas_entries():
    return atlas_entry


def createAtlasEntry(atlas_path=atlas_path):
    ''' Converts filesystem items into ATLAS entry objects. '''

    all_files = get_all_files(atlas_path)

    for item in all_files:
        if item.name != 'desktop.ini':
            if item.is_file():
                atlas_entry[str(item)] = AtlasFile(item, item.suffix)
            if item.is_dir():
                atlas_entry[str(item)] = AtlasFolder(item)


def printAtlasEntries():
    for f in atlas_entry:
        extension = f.extension if hasattr(f, 'extension') else 'n/a'
        print(
            f'Entry name: {f.path.stem} | Type: {f.type} | Extension: {extension}')
