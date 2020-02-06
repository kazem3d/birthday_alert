import sqlite3
import xlrd


address="list.xls"
#address=input('Enter file path :')

excel_reader=xlrd.open_workbook(address) 
sheet = excel_reader.sheet_by_index(0) 
sheet.cell_value(0, 0) 

conn=sqlite3.connect("personel")
