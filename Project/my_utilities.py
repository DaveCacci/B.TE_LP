# DECLARE THE FUNCTION TO SAVE DATA TO EXCEL FILES
from openpyxl import load_workbook
from openpyxl import Workbook
from openpyxl.utils import get_column_letter

def flatten_list(nested_list):
    """Flatten a nested list."""
    flattened_list = []
    for sublist in nested_list:
        if isinstance(sublist, list):
            flattened_list.extend(flatten_list(sublist))
        else:
            flattened_list.append(sublist)
    return flattened_list

def save_list_to_excel(nested_list, file_path, sheet_name):

    # Flatten the nested list
    flattened_list = flatten_list(nested_list)

    # Load the existing workbook if it exists
    try:
        workbook = load_workbook(file_path)
    except FileNotFoundError:
        workbook = Workbook()

    # Check if the specified sheet exists in the workbook
    if sheet_name in workbook.sheetnames:
        # Get the existing sheet
        sheet = workbook[sheet_name]
        # Find the next available column
        next_column = len(list(sheet.columns)) + 1
    else:
        # Create a new sheet
        sheet = workbook.create_sheet(title=sheet_name)
        next_column = 1

    # Write data to the sheet
    for row_idx, item in enumerate(flattened_list, start=1):
        sheet.cell(row=row_idx, column=next_column, value=item)

    # Save the workbook back to the file
    workbook.save(file_path)

# DECLARE THE FUNCTION TO READ DATA FROM EXCEL FILES
import pandas as pd
def read_excel_file(file_path):
    # Read the Excel file and return a dictionary of DataFrames for each sheet
    xls = pd.ExcelFile(file_path)
    sheet_dict = {sheet_name: pd.read_excel(xls, sheet_name, skiprows=[1]) for sheet_name in xls.sheet_names}
    return sheet_dict