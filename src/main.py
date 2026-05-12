from pathlib import Path
from file_navigation import *
from classes.atlas import AtlasFile, AtlasFolder

atlas_path = Path.home() / "documents" / "atlas storage"

all_files = get_all_files(atlas_path)

atlas_entry = []

# Create AtlasFiles for each file and folder.
for item in all_files:
    if item.name != 'desktop.ini':
        if item.is_file():
            atlas_entry.append(AtlasFile(item, item.suffix))
        if item.is_dir():
            atlas_entry.append(AtlasFolder(item))

for f in atlas_entry:
    extension = f.extension if hasattr(f, 'extension') else 'n/a'
    print(
        f'Entry name: {f.path.stem} | Type: {f.type} | Extension: {extension}')

# This is only used for testing purposes
testing_true = False
while testing_true:
    user_selection = input(
        '\n1. Add folder\n2. Remove folder\n3. Exit\nSelection: ')

    match user_selection.lower():
        case '1':
            new_folder = input("New Folder Name: ")
            add_folder(atlas_path, new_folder)
            break
        case '2':
            folder_name = input("New Folder Name: ")
            remove_folder(atlas_path, folder_name)
            break
        case '3':
            break
        case _:
            print('Incorrect option selected. Try again.')
