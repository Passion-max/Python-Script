import os
import shutil


# Define the source and destination folders
src_folder = r'C:\Users\user\Downloads\Bundles\FILES T0 MOVE'
dst_folder = r'C:\Users\user\OneDrive\GRANT\MADAM NKECHI WORK\UAAG\GRACIOUS PEOPLE'

# Get the list of files in the source folder
files = os.listdir(src_folder)
count = 718
# Loop through each file in the source folder
for file in files:
    # Check if the file is an Excel file (has a .xlsx extension)
    if file.endswith('.xlsx'):
        # Generate a timestamp to use as the new filename
        
        new_filename = f'GRACIOUS-PEOPLE-{count}-UAAG.xlsx'

        # Construct the full paths to the source and destination files
        src_file = os.path.join(src_folder, file)
        dst_file = os.path.join(dst_folder, new_filename)

        # Move the file to the destination folder and rename it
        shutil.copy(src_file, dst_file)
        print(f'Moved {file} to {dst_file}')
        count += 1
