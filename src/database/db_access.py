from pathlib import Path

# Identifies and stores the Atlas Storage Folder path.
atlas_path = Path.home() / "documents" / "atlas storage"

# TODO: Later this will be replaced with persistent storage (Local SQL Server then a cloud database).
atlas_entries = {}


# used to put an item into datbase that doesn't matter if its a dict or database that holds it. Interchangable. This handles the storing
# needs to be abstracted so that you can use this no matter what is the storage source.


def add_to_db(atlas_entry):
    atlas_entries[str(atlas_entry.path)] = atlas_entry


def remove_from_db(atlas_entry):
    try:
        del atlas_entries[str(atlas_entry.path)]
    except:
        print(
            f'ISSUE: Atlas Entry does not exist at path: {atlas_entry['path']}')


def get_entries():
    return atlas_entries


def get_entries_values():
    return atlas_entries.values()
