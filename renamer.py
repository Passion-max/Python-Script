from openpyxl import load_workbook
import os
import shutil

def rename_files_based_on_cell(input_folder, cell_address):
    for file in os.listdir(input_folder):
        if file.endswith('.xlsx') or file.endswith('.xls'):
            file_path = os.path.join(input_folder, file)
            wb = load_workbook(filename = file_path)
            sheet = wb.active
            
            # Get value of cell
            cell_value = sheet[cell_address].value
            
            # Rename the file with cell value. Handle possible errors due to invalid characters for filenames
            try:
                new_file_path = os.path.join(input_folder, f'{cell_value}-KOKOOLA-UAAG.xlsx')
                os.rename(file_path, new_file_path)
                print(f"Renamae this {file} to this {e}")
            except Exception as e:
                print(f"Couldn't rename {file} due to an error: {new_file_path}")
input_folder = r'C:\Users\user\Documents\python output\Transfer Done'
cell_address = 'B10'  # change this to the cell address you want
rename_files_based_on_cell(input_folder, cell_address)