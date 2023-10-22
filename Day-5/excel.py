# read excel file in python

import xlrd

# to extract data from spreadsheet 

loc  = ("e:\\python\\Day-5\\demo.xlsx")

wb = xlrd.open_workbook(loc)
sheet= wb.sheet_by_index(0)

print(sheet.cell_value(3,3))

print(sheet.ncols) # print count of cols

print(sheet.nrows) # prints count of rows