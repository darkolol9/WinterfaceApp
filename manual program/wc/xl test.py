from openpyxl import Workbook
from openpyxl import load_workbook

wb = load_workbook('testxls.xlsx')
ws = wb.get_sheet_by_name('Sheet')
ws.append((1,2,3))
wb.save('testxls.xlsx')