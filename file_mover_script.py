import shutil
import os

# Define source and destination directories
source_dir = 'source_folder/'
destination_dir = 'destination_folder/'

# List all files in the source directory
files = os.listdir(source_dir)

# Move each file to the destination directory
for file_name in files:
    full_file_name = os.path.join(source_dir, file_name)
    if os.path.isfile(full_file_name):
        shutil.move(full_file_name, destination_dir)
        print(f'Moved: {file_name}')
    else:
        print(f'Not a file: {file_name}')