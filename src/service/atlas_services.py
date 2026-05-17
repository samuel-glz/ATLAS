
from pathlib import Path
import pickle
from file_navigation import *
from classes.atlas import AtlasFile, AtlasFolder

atlas_path = Path.home() / "documents" / "atlas storage"

atlas_store_path = atlas_path / ".atlas_entries.pkl"


def load_atlas_entries():
    if not atlas_store_path.exists():
        return {}

    with atlas_store_path.open("rb") as storage_file:
        return pickle.load(storage_file)


def save_atlas_entries():
    atlas_store_path.parent.mkdir(parents=True, exist_ok=True)
    with atlas_store_path.open("wb") as storage_file:
        pickle.dump(atlas_entry, storage_file, protocol=pickle.HIGHEST_PROTOCOL)


atlas_entry = load_atlas_entries()


def view_atlas_entries():
    return atlas_entry


def createAtlasEntries(atlas_path=atlas_path):
    ''' Converts filesystem items into ATLAS entry objects. '''

    all_files = get_all_files(atlas_path)
    atlas_entry.clear()

    for item in all_files:
        if item.name != 'desktop.ini':
            if item.is_file():
                atlas_entry[item] = AtlasFile(item, item.suffix)
            if item.is_dir():
                atlas_entry[item] = AtlasFolder(item)
    save_atlas_entries()


def printAtlasEntries():
    for f in atlas_entry:
        extension = f.extension if hasattr(f, 'extension') else 'n/a'
        print(
            f'Entry name: {f.path.stem} | Type: {f.type} | Extension: {extension}')
