
def view_folder_contents(path):
    ''' View the files and folders within a folder.'''

    file_paths = [f for f in path.iterdir() if f.name != 'desktop.ini']

    files = []
    for f in file_paths:
        files.append(f.name)

    return files


def add_folder(path, folder_name):
    new_folder = path / folder_name

    try:
        new_folder.mkdir()
    except:
        print("A folder with that name already exists.")


def remove_folder(path, folder_name):
    f = path / folder_name
    user_confirmation = input(
        f'Are you sure you want to remove this folder?: ({folder_name}) This will remove ALL files and folders within this folder!')

    if f and user_confirmation.lower() == 'y':
        f.rmdir()
        print('Folder removed successfully.')
    else:
        print('Folder was not removed.')


def get_all_files(atlas_root):
    return atlas_root.rglob("*")
