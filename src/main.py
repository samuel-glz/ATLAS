from handlers.atlas_manager import AtlasManager
from database.db_access import atlas_entries

AM = AtlasManager()

AM.create_atlas_entries()

print(f"Curernt Folder: '{AM.current_view.name}'")
print('Files:')

AM.view_current_dir()

# # ***** This is the file system version. The goal is to do this with AtLas Entries dict. *****
# for item in AM.current_view.iterdir():
#     if item.name != 'desktop.ini':
#         print(item.name)

# # print the starting folder
# user_input = input('Change dir to: ')

# AM.change_dir(user_input, 'f')

# for item in AM.current_view.iterdir():
#     if item.name != 'desktop.ini':
#         print(item.name)
