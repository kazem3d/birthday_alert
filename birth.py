
import xlrd
import jdatetime
import calendar

#address=input('Enter file path :')
line_count=0
l=list()
d=dict()
l2=list()
address="list.xls"

excel_reader=xlrd.open_workbook(address) 
sheet = excel_reader.sheet_by_index(0) 
sheet.cell_value(0, 0) 

for i in range(2,sheet.nrows):
    
    row=sheet.row_values(i)
    
    d[row[2]]=row[3]
   

today=str(jdatetime.date.today()) 
today_list=today.split('-')

taqv=calendar.Calendar()
month_list=taqv.monthdayscalendar(int(today_list[0]), int(today_list[1])) 
for i in range(0,len(month_list)):
    
    if int(today_list[2]) in month_list[i]:
        this_week=month_list[i]

print('^^^^^^^^^^^^^^^^^^^^^^^^^^')        
print('Today date:',today) 
print('^^^^^^^^^^^^^^^^^^^^^^^^^^')

for i in d:
    name=i

    date_list=d[i].split('/')
    
    if int(date_list[1]) == int(today_list[1]):
        if int(date_list[2]) == int(today_list[2])+1:
            
            print("It's %s birthday" %name)
            age=int(today_list[0])-int(date_list[0])
            print("he/she is %s years old" % (age))
            print("*************************************")
print('^^^^^^^^^^^^^^^^^^^^^^^^^^')
print("In this week we have birthday of :")    

for i in d:
    name=i   
    date_list=d[i].split('/')            
    if int(date_list[1]) == int(today_list[1]):
        for i in this_week:
            if  int(date_list[2]) == i:   
                print(name,d[name])  