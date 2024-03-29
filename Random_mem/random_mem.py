# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sqlite3 as sql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class Ui_Random_mem(object):
    def setupUi(self, Random_mem):
        Random_mem.setObjectName("Random_mem")
        Random_mem.resize(1603, 900)
        self.centralwidget = QtWidgets.QWidget(Random_mem)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1603, 900))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label = QtWidgets.QLabel(self.page_2)
        self.label.setGeometry(QtCore.QRect(0, 0, 1603, 900))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setItalic(True)
        font.setStrikeOut(True)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("registration.png"))
        self.label.setObjectName("label")
        self.PushButton_Sign_in = QtWidgets.QPushButton(self.page_2)
        self.PushButton_Sign_in.setGeometry(QtCore.QRect(660, 690, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.PushButton_Sign_in.setFont(font)
        self.PushButton_Sign_in.setStatusTip("")
        self.PushButton_Sign_in.setWhatsThis("")
        self.PushButton_Sign_in.setAccessibleName("")
        self.PushButton_Sign_in.setStyleSheet("background:rgb(170, 170, 255);")
        self.PushButton_Sign_in.setObjectName("PushButton_Sign_in")
        self.PushButton_Sign_in.clicked.connect(self.switch) #подключаем функцию перехода на следующую страницу


        self.stackedWidget.addWidget(self.page_2)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1603, 900))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("reg.png"))
        self.label_2.setObjectName("label_2")
        self.lineEdit_Login = QtWidgets.QLineEdit(self.page)
        self.lineEdit_Login.setGeometry(QtCore.QRect(1140, 430, 281, 30))
        self.lineEdit_Login.setObjectName("lineEdit_Login")
        self.lineEdit_Password = QtWidgets.QLineEdit(self.page)
        self.lineEdit_Password.setGeometry(QtCore.QRect(1180, 553, 251, 30))
        self.lineEdit_Password.setObjectName("lineEdit_Password")
        self.pushButton_reg_bd = QtWidgets.QPushButton(self.page)
        self.pushButton_reg_bd.setGeometry(QtCore.QRect(1030, 752, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_reg_bd.setFont(font)
        self.pushButton_reg_bd.setStyleSheet("background:rgb(170, 170, 255);")
        self.pushButton_reg_bd.setObjectName("pushButton_reg_bd")
        self.pushButton_reg_bd.clicked.connect(self.registration)


        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_3 = QtWidgets.QLabel(self.page_3)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 1603, 900))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("mem.png"))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.page_3)
        self.label_4.setGeometry(QtCore.QRect(270, 80, 1031, 721))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("default.jpg"))
        self.label_4.setObjectName("label_4")

        self.pushButton_random = QtWidgets.QPushButton(self.page_3)
        self.pushButton_random.setGeometry(QtCore.QRect(640, 820, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_random.setFont(font)
        self.pushButton_random.setStyleSheet("background:rgb(170, 170, 255);")
        self.pushButton_random.setObjectName("pushButton_random")
        self.pushButton_random.clicked.connect(self.mem)
        self.stackedWidget.addWidget(self.page_3)
        Random_mem.setCentralWidget(self.centralwidget)

        self.retranslateUi(Random_mem)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Random_mem)



    def retranslateUi(self, Random_mem):
        _translate = QtCore.QCoreApplication.translate
        Random_mem.setWindowTitle(_translate("Random_mem", "Random_mem"))
        self.PushButton_Sign_in.setText(_translate("Random_mem", "Регистрация"))
        self.pushButton_reg_bd.setText(_translate("Random_mem", "Зарегистрироваться"))
        self.pushButton_random.setText(_translate("Random_mem", "Сгенерировать"))


    def switch(self, index):
            self.stackedWidget.setCurrentIndex(1) #функция перехода на следующую страницу

    def registration(self):
            con = sql.connect('memes_database.db')
            cur = con.cursor()
            a = self.lineEdit_Login.text()
            b = self.lineEdit_Password.text()
            query1 = f" INSERT INTO registration (login,password) VALUES('{a}','{b}')"
            cur.execute(query1)
            con.commit()
            cur.close()
            con.close()
            self.stackedWidget.setCurrentIndex(2) #регистрация пользователя

    def mem(self):
        self.conn = sql.connect('memes_database.db')
        self.cursor = self.conn.cursor()
        # Получаем номер фотографии
        self.cursor.execute('SELECT id FROM photos ORDER BY RANDOM() LIMIT 1')
        row = self.cursor.fetchone()
        photo_id = row[0]

        # Получаем фотографию из базы данных
        self.cursor.execute('SELECT photo FROM photos WHERE id = ?', (photo_id,))
        row = self.cursor.fetchone()

        # Отображаем фотографию на экране
        pixmap = QPixmap()
        pixmap.loadFromData(row[0])
        self.label_4.setPixmap(pixmap)
        self.label_4.setGeometry(QtCore.QRect(270, 80, 1031, 721))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.conn.close()





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Random_mem = QtWidgets.QMainWindow()
    ui = Ui_Random_mem()
    ui.setupUi(Random_mem)
    Random_mem.show()
    sys.exit(app.exec_())
