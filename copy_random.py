import os
import shutil
import random

def copy_random_files(source_folder, target_folder, n):
    # Get all files from the source_folder
    files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

    # Randomly select n files
    random_files = random.sample(files, n)

    # Make sure the target folder exists
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # Copy the selected files to the target_folder
    for file in random_files:
        shutil.copy2(os.path.join(source_folder, file), target_folder)

# Usage
source_folder = r'C:\Users\user\Documents\python output\Brenda\ALL'
target_folder = r'C:\Users\user\Documents\python output\BRENDA COMMUNICATION'
copy_random_files(source_folder, target_folder, 1000)
