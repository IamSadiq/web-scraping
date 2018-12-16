from xlsxwriter import Workbook
import xlrd

# create workbook
workbook = Workbook('./worksheets/first-workbook.xlsx')

# add worksheet
worksheet = workbook.add_worksheet()

# add data to sheet
for row in range(100):
    worksheet.write(row, 0, 'row number')
    worksheet.write(row, 1,  row)
    
# open worksheet
saved_wb = xlrd.open_workbook('./worksheets/first-workbook.xlsx')

# get sheet - method- sheet_by_index(index_parameter)
ws = saved_wb.sheet_by_index(0)

# get total number of rows
rows = ws.nrows

# show rows
for row in range(rows):
    first_col, second_col = ws.row_values(row)
    print(first_col,'  ',second_col)

# close workbook
workbook.close()