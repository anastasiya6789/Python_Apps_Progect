
from PyQt5.QtGui import QColor, QTextCharFormat
from PyQt5.QtCore import Qt, QDate, QDateTime
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1132, 732)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1132, 732))
        self.stackedWidget.setObjectName("stackedWidget")

        self.HOME_page_0 = QtWidgets.QWidget()
        self.HOME_page_0.setObjectName("HOME_page_0")

        self.label = QtWidgets.QLabel(self.HOME_page_0)
        self.label.setGeometry(QtCore.QRect(0, 0, 1132, 732))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("1.png"))
        self.label.setObjectName("label")

        self.HOME_REGISTRATION_pushButton = QtWidgets.QPushButton(self.HOME_page_0)
        self.HOME_REGISTRATION_pushButton.setGeometry(QtCore.QRect(460, 430, 211, 41))
        self.HOME_REGISTRATION_pushButton.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;")
        self.HOME_REGISTRATION_pushButton.setText("")
        self.HOME_REGISTRATION_pushButton.setObjectName("HOME_REGISTRATION_pushButton")
        self.HOME_REGISTRATION_pushButton.clicked.connect(self.switch_0_1)

        self.HOME_VXOD_pushButton = QtWidgets.QPushButton(self.HOME_page_0)
        self.HOME_VXOD_pushButton.setGeometry(QtCore.QRect(520, 490, 91, 51))
        self.HOME_VXOD_pushButton.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;")
        self.HOME_VXOD_pushButton.setText("")
        self.HOME_VXOD_pushButton.setObjectName("HOME_VXOD_pushButton")
        self.HOME_VXOD_pushButton.clicked.connect(self.switch_0_2)

        self.stackedWidget.addWidget(self.HOME_page_0)

        self.REGISTRATION_page_1 = QtWidgets.QWidget()
        self.REGISTRATION_page_1.setObjectName("REGISTRATION_page_1")

        self.label_2 = QtWidgets.QLabel(self.REGISTRATION_page_1)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1132, 732))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("2.png"))
        self.label_2.setObjectName("label_2")

        self.REGISTRATION_CALENDAR_pushButton = QtWidgets.QPushButton(self.REGISTRATION_page_1)
        self.REGISTRATION_CALENDAR_pushButton.setGeometry(QtCore.QRect(640, 500, 351, 91))
        self.REGISTRATION_CALENDAR_pushButton.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;")
        self.REGISTRATION_CALENDAR_pushButton.setText("")
        self.REGISTRATION_CALENDAR_pushButton.setObjectName("REGISTRATION_CALENDAR_pushButton")
        self.REGISTRATION_CALENDAR_pushButton.clicked.connect(self.registration)

        self.REGISTRATION_LOGIN_lineEdit = QtWidgets.QLineEdit(self.REGISTRATION_page_1)
        self.REGISTRATION_LOGIN_lineEdit.setGeometry(QtCore.QRect(760, 263, 281, 31))
        self.REGISTRATION_LOGIN_lineEdit.setObjectName("REGISTRATION_LOGIN_lineEdit")

        self.REGISTRATION_PASSWORD_lineEdit = QtWidgets.QLineEdit(self.REGISTRATION_page_1)
        self.REGISTRATION_PASSWORD_lineEdit.setGeometry(QtCore.QRect(800, 380, 241, 31))
        self.REGISTRATION_PASSWORD_lineEdit.setObjectName("REGISTRATION_PASSWORD_lineEdit")

        self.stackedWidget.addWidget(self.REGISTRATION_page_1)

        self.VXOD_page = QtWidgets.QWidget()
        self.VXOD_page.setObjectName("VXOD_page")

        self.label_3 = QtWidgets.QLabel(self.VXOD_page)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 1132, 732))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("3.png"))
        self.label_3.setObjectName("label_3")

        self.VXOD_CALENDAR_pushButton = QtWidgets.QPushButton(self.VXOD_page)
        self.VXOD_CALENDAR_pushButton.setGeometry(QtCore.QRect(640, 497, 351, 91))
        self.VXOD_CALENDAR_pushButton.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;")
        self.VXOD_CALENDAR_pushButton.setText("")
        self.VXOD_CALENDAR_pushButton.setObjectName("VXOD_CALENDAR_pushButton")
        self.VXOD_CALENDAR_pushButton.clicked.connect(self.vhod)

        self.VXOD_PASSWORD_lineEdit = QtWidgets.QLineEdit(self.VXOD_page)
        self.VXOD_PASSWORD_lineEdit.setGeometry(QtCore.QRect(800, 377, 241, 31))
        self.VXOD_PASSWORD_lineEdit.setObjectName("VXOD_PASSWORD_lineEdit")

        self.VXOD_LOGIN_lineEdit = QtWidgets.QLineEdit(self.VXOD_page)
        self.VXOD_LOGIN_lineEdit.setGeometry(QtCore.QRect(760, 260, 281, 31))
        self.VXOD_LOGIN_lineEdit.setObjectName("VXOD_LOGIN_lineEdit")

        self.stackedWidget.addWidget(self.VXOD_page)

        self.CALENDAR_page = QtWidgets.QWidget()
        self.CALENDAR_page.setObjectName("CALENDAR_page")

        self.label_4 = QtWidgets.QLabel(self.CALENDAR_page)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 1132, 732))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("4.png"))
        self.label_4.setObjectName("label_4")

        self.scrollArea = QtWidgets.QScrollArea(self.CALENDAR_page)
        self.scrollArea.setGeometry(QtCore.QRect(5, 115, 328, 499))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 326, 497))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.TEXT_FROM_BD_label = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.TEXT_FROM_BD_label.setGeometry(QtCore.QRect(0, 0, 321, 491))
        self.TEXT_FROM_BD_label.setText("")
        self.TEXT_FROM_BD_label.setObjectName("TEXT_FROM_BD_label")

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.ADD_EXERCIZE__pushButton = QtWidgets.QPushButton(self.CALENDAR_page)
        self.ADD_EXERCIZE__pushButton.setGeometry(QtCore.QRect(520, 170, 151, 41))
        self.ADD_EXERCIZE__pushButton.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;")
        self.ADD_EXERCIZE__pushButton.setText("")
        self.ADD_EXERCIZE__pushButton.setObjectName("ADD_EXERCIZE__pushButton")
        self.ADD_EXERCIZE__pushButton.clicked.connect(self.add_exercise)


        self.TIME_lineEdit = QtWidgets.QTextEdit(self.CALENDAR_page)
        self.TIME_lineEdit.setGeometry(QtCore.QRect(900, 165, 113, 27))
        self.TIME_lineEdit.setObjectName("TIME_lineEdit")

        self.EXERSIZE_lineEdit = QtWidgets.QTextEdit(self.CALENDAR_page)
        self.EXERSIZE_lineEdit.setGeometry(QtCore.QRect(840, 202, 171, 27))
        self.EXERSIZE_lineEdit.setObjectName("EXERSIZE_lineEdit")

        self.CALENDAR_calendarWidget = QtWidgets.QCalendarWidget(self.CALENDAR_page)
        self.CALENDAR_calendarWidget.setGeometry(QtCore.QRect(497, 290, 524, 321))
        self.CALENDAR_calendarWidget.setObjectName("CALENDAR_calendarWidget")
        self.CALENDAR_calendarWidget.clicked[QDate].connect(self.show_exercises)

        self.selected_date = QDate.currentDate()
        self.show_exercises(self.selected_date)

        self.CALENDAR_calendarWidget.setSelectedDate(self.selected_date)
        self.show_exercises(self.selected_date)

        self.stackedWidget.addWidget(self.CALENDAR_page)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    # функция перехода на страницу регистрации
    def switch_0_1(self, index):
        self.stackedWidget.setCurrentIndex(1)

    # функция перехода на страницу входа
    def switch_0_2(self, index):
        self.stackedWidget.setCurrentIndex(2)

    # регистрация пользователя.Вносим логин и пароль пользователя в таблицу user
    def registration(self):
            con = sqlite3.connect('Gumn.db')
            cur = con.cursor()
            a = self.REGISTRATION_LOGIN_lineEdit.text()
            b = self.REGISTRATION_PASSWORD_lineEdit.text()
            query1 = f" INSERT INTO users (login,password) VALUES('{a}','{b}')"
            cur.execute(query1)
            con.commit()
            cur.close()
            con.close()
            # переходим на страницу календаря
            self.stackedWidget.setCurrentIndex(3)  # регистрация пользователя
    # функция для добавления заметки в базу данных
    def add_exercise(self):
        time = self.TIME_lineEdit.toPlainText()
        name = self.EXERSIZE_lineEdit.toPlainText()
        login=self.REGISTRATION_LOGIN_lineEdit.text() or self.VXOD_LOGIN_lineEdit.text()
        password=self.REGISTRATION_PASSWORD_lineEdit.text() or self.VXOD_PASSWORD_lineEdit.text()
        con = sqlite3.connect('Gumn.db')
        cur = con.cursor()

        cur.execute("INSERT INTO exercise (date, time, name, login, password) VALUES (?, ?, ?, ?, ?)",
                       (self.selected_date.toString(Qt.ISODate), time, name, login, password))


        con.commit()
        self.show_exercises(self.selected_date)


    def show_exercises(self, date):
        self.selected_date = date

        con = sqlite3.connect('Gumn.db')
        cur = con.cursor()
        login=self.REGISTRATION_LOGIN_lineEdit.text() or self.VXOD_LOGIN_lineEdit.text()
        password=self.REGISTRATION_PASSWORD_lineEdit.text() or self.VXOD_PASSWORD_lineEdit.text()
        cur.execute("SELECT date, time, name FROM exercise WHERE date = ? AND login=? AND password=?", (self.selected_date.toString(Qt.ISODate), login, password))
        data = cur.fetchall()

        self.TEXT_FROM_BD_label.clear()
        for row in data:
            self.TEXT_FROM_BD_label.insertPlainText("Дата: " + row[0] + "\n")
            self.TEXT_FROM_BD_label.insertPlainText("Продолжительность тренировки: " + row[1] + "\n")
            self.TEXT_FROM_BD_label.insertPlainText("Упражнение: " + row[2] + "\n\n")

        # Устанавливаем фон дня зеленым, если есть заметки для дня
        if data:
            self.CALENDAR_calendarWidget.setDateTextFormat(self.selected_date, self.format_day(QColor(0, 255, 0)))
        else:
            self.CALENDAR_calendarWidget.setDateTextFormat(self.selected_date,
                                                           QTextCharFormat())  # Убираем форматирование, если заметок нет



    def format_day(self, color):
        format = QTextCharFormat()
        format.setBackground(color)
        return format


    def green_text_format(self):
        text_format = self.default_text_format()
        text_format.setBackground(QColor(0, 255, 0, 127))
        return text_format


    def default_text_format(self):
        text_format = self.CALENDAR_calendarWidget.dateTextFormat(QDate())
        text_format.setBackground(QColor(255, 255, 255, 0))
        return text_format

    def vhod(self):
        login = self.VXOD_LOGIN_lineEdit.text()
        password = self.VXOD_PASSWORD_lineEdit.text()

        # Подключиться к базе данных
        conn = sqlite3.connect('Gumn.db')
        cursor = conn.cursor()

        # Проверить, существует ли пользователь с таким логином и паролем в таблице users
        cursor.execute("SELECT * FROM users WHERE login=? AND password=?", (login, password))
        user = cursor.fetchone()

        if user:
            self.stackedWidget.setCurrentIndex(3)
            login = self.VXOD_LOGIN_lineEdit.text()
            password = self.VXOD_PASSWORD_lineEdit.text()

            # Подключиться к базе данных
            conn = sqlite3.connect('Gumn.db')
            cursor = conn.cursor()

            cursor.execute("SELECT date FROM exercise WHERE login=? AND password=?", (login, password))
            dates = cursor.fetchall()

            for date in dates:
                date = QDate.fromString(date[0], 'yyyy-MM-dd')
                self.CALENDAR_calendarWidget.setDateTextFormat(date, self.green_text_format())

        else:
            self.stackedWidget.setCurrentIndex(0)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


