from pathlib import Path
from file_navigation import *
from classes.atlas_file import AtlasFile

atlas_path = Path.home() / "documents" / "atlas storage"

all_files = get_all_files(atlas_path)

atlas_files = []

for file in all_files:
    if file.name != 'desktop.ini':
        atlas_files.append(AtlasFile(file, file.suffix))

for f in atlas_files:
    print(f.name)

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
