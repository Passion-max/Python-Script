import openpyxl

def convert_excel_to_dict(file_path, sheet_name, start_row, end_row, header_row):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb[sheet_name]
    
    header_cells = sheet[header_row]
    header = [cell.value for cell in header_cells]
    
    data = []
    for row in range(start_row, end_row + 1):
        row_data = {}
        for col, header_cell in enumerate(header_cells):
            row_data[header_cell.value] = sheet.cell(row=row, column=col + 1).value
        data.append(row_data)
    return data

file_path = r'C:\Users\user\Downloads\format\data.xlsx'
sheet_name = 'Sheet2'
start_row = 2
end_row = 501
header_row = 1

data = convert_excel_to_dict(file_path, sheet_name, start_row, end_row, header_row)
print(data)