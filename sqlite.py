import sqlite3
import xlrd


address="list.xls"
#address=input('Enter file path :')


line_count=0
l=list()
d=dict()
l2=list()

excel_reader=xlrd.open_workbook(address) 
sheet = excel_reader.sheet_by_index(0) 
sheet.cell_value(0,0) 

for i in range(2,sheet.nrows):
    
    row=sheet.row_values(i)     
    d[row[2]]=[row[3],row[5]]

    

conn=sqlite3.connect("personel")
curser=conn.cursor()

curser.execute('''CREATE TABLE IF NOT EXISTS main (
    
    id integer PRIMARY KEY,
    name TEXT  NULL ,
    full_name TEXT NOT NULL,
    birth_date TEXT NOT NULL,
    code TEXT NULL,
    city TEXT NULL,
    job TEXT NULL,
    contract_type TEXT NULL,
    FOREIGN  KEY (job) REFERENCES jobs (id)
    FOREIGN  KEY (city) REFERENCES cities (id)
    FOREIGN  KEY (contract_type) REFERENCES contracts (id)

)''')

curser.execute('''CREATE TABLE IF NOT EXISTS jobs (
    id integer PRIMARY KEY,
    name TEXT NOT NULL

    )''')

curser.execute('''CREATE TABLE IF NOT EXISTS cities (
    id integer PRIMARY KEY,
    name TEXT NOT NULL

    )''')

curser.execute('''CREATE TABLE IF NOT EXISTS contracts (
    id integer PRIMARY KEY,
    name TEXT NOT NULL

    )''')

# curser.execute('''INSERT INTO jobs (id,name) 
# VALUES  
#     (1,\'نگهبان\'),
#     (2,\'کارمند\')
#     '''
#     )


        
for i in d:
    name=i 
    curser.execute('INSERT INTO main (full_name,birth_date,job)  VALUES (?,?,?)' 
    ,(name,d[name][0],d[name][1])
    )



conn.commit()