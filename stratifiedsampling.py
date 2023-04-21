import os
import random
import shutil

# Set the path to the source folder containing the files to transfer
source_folder = 'raw/c_covid'

# Set the path to the destination folder to transfer the files to
destination_folder = 'data/validation'

# Get the file paths for all the files in the source folder
file_paths = [os.path.join(source_folder, f) for f in os.listdir(source_folder)]

# Determine the number of files to transfer
num_files = int(1 * len(file_paths))

# Randomly shuffle the file paths
random.shuffle(file_paths)

# Transfer the specified number of files to the destination folder
for i in range(num_files):
    # Get the current file path
    file_path = file_paths[i]
    
    # Get the filename and extension
    file_name, file_extension = os.path.splitext(os.path.basename(file_path))
    
    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # Copy the file to the destination folder with a new filename
    new_file_name = f'{file_name}_{i}{file_extension}'
    destination_path = os.path.join(destination_folder, new_file_name)
    #shutil.copy(file_path, destination_path)
    os.rename(file_path, destination_path)
