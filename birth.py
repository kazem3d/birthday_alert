
import jdatetime
import calendar
import sqlite3

#address=input('Enter file path :')
line_count=0
l=list()
d=dict()
l2=list()
address="list.xls"

conn=sqlite3.connect("personel")
curser=conn.cursor()
curser.execute('SELECT * FROM main')
rows=curser.fetchall()
for row in rows:
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
print('______________________________________')
print("In this week we have birthday of :")    

for i in d:
    name=i   
    date_list=d[i].split('/')            
    if int(date_list[1]) == int(today_list[1]):
        for i in this_week:
            if  int(date_list[2]) == i:   
                print(name,d[name])  