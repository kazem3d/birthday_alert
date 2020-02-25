# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\kazem\Desktop\project\birthday.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


import jdatetime
import calendar
import sqlite3



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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(328, 321)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 10, 256, 261))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 328, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
        
        
        self.textBrowser.append("              ")
        self.textBrowser.append('                    تاریخ امروز : %s' %today)
        self.textBrowser.append("              ")

        self.printer()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "birthdayAlert"))
        

    def printer(self):
        self.textBrowser.append("                  *************************")
        for i in d:
            name=i

            date_list=d[i].split('/')
            
            if int(date_list[1]) == int(today_list[1]):
                if int(date_list[2]) == int(today_list[2])+1:
                    
                    print("It's %s birthday" %name)
                    self.textBrowser.append("فردا تولد %s است" %name)
                    
                    age=int(today_list[0])-int(date_list[0])
                    print("he/she is %s years old" % (age))
                    self.textBrowser.append("او  %d ساله شده است" % age)
                    print("===============================")
                    self.textBrowser.append("         ========================")

        #self.textBrowser.append('                ^^^^^^^^^^^^^^^^^^^^^^^^^^')
        self.textBrowser.append("لیست متولدین این هفته :")
        self.textBrowser.append('  ')
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^')
        print("In this week we have birthday of :")    
        no_birthday=False
        for i in d:
            name=i   
            date_list=d[i].split('/')            
            if int(date_list[1]) == int(today_list[1]):
                for i in this_week:
                    if  int(date_list[2]) == i: 
                        self.textBrowser.append('%s  متولد : %s'  %(name , d[name]) )  
                        print(name,d[name])  
                        no_birthday=True
        if no_birthday == False:
            print('there is no one') 
            self.textBrowser.append('کسی وجود ندارد')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
