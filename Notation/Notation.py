from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_Notation():
    def setupUi(self, Notation):
        Notation.setObjectName("Notation")
        Notation.resize(550, 796)
        self.centralwidget = QtWidgets.QWidget(Notation)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 550, 800))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(0, 0, 550, 800))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Слой 1.png"))
        self.label.setObjectName("label")
        self.pushButton_1_1 = QtWidgets.QPushButton(self.page)
        self.pushButton_1_1.setGeometry(QtCore.QRect(235, 740, 21, 21))
        self.pushButton_1_1.setStyleSheet("background-color:#F0F2F6;\n"
"border-radius: 5px;")
        self.pushButton_1_1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Слой 2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_1_1.setIcon(icon)
        self.pushButton_1_1.setObjectName("pushButton_1_1")

        self.pushButton_1_2 = QtWidgets.QPushButton(self.page)
        self.pushButton_1_2.setGeometry(QtCore.QRect(265, 740, 21, 21))
        self.pushButton_1_2.setStyleSheet("background-color:#F0F2F6;\n"
"border-radius: 5px;")
        self.pushButton_1_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Слой 3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_1_2.setIcon(icon1)
        self.pushButton_1_2.setObjectName("pushButton_1_2")
        self.pushButton_1_2.clicked.connect(self.switch_1_2)
        self.pushButton_1_3 = QtWidgets.QPushButton(self.page)
        self.pushButton_1_3.setGeometry(QtCore.QRect(295, 740, 21, 21))
        self.pushButton_1_3.setStyleSheet("background-color:#F0F2F6;\n"
"border-radius: 5px;")
        self.pushButton_1_3.setText("")
        self.pushButton_1_3.setIcon(icon1)
        self.pushButton_1_3.setObjectName("pushButton_1_3")
        self.pushButton_1_3.clicked.connect(self.switch_1_3)
        self.pushButton_1_4 = QtWidgets.QPushButton(self.page)
        self.pushButton_1_4.setGeometry(QtCore.QRect(325, 740, 21, 21))
        self.pushButton_1_4.setStyleSheet("background-color:#F0F2F6;\n"
"border-radius: 5px;")
        self.pushButton_1_4.setText("")
        self.pushButton_1_4.setIcon(icon1)
        self.pushButton_1_4.setObjectName("pushButton_1_4")
        self.pushButton_1_4.clicked.connect(self.switch_1_4)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 550, 1921))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Слой 5.png"))
        self.label_2.setObjectName("label_2")


        self.lineEdit_original_number_system = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_original_number_system.setGeometry(QtCore.QRect(340, 410, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_original_number_system.setFont(font)
        self.lineEdit_original_number_system.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_original_number_system.setObjectName("lineEdit_original_number_system")


        self.lineEdit_number = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_number.setGeometry(QtCore.QRect(60, 410, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_number.setFont(font)
        self.lineEdit_number.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_number.setStyleSheet("")
        self.lineEdit_number.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_number.setObjectName("lineEdit_number")


        self.lineEdit_number_system_is_finite = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_number_system_is_finite.setGeometry(QtCore.QRect(200, 570, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_number_system_is_finite.setFont(font)
        self.lineEdit_number_system_is_finite.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_number_system_is_finite.setObjectName("lineEdit_number_system_is_finite")


        self.pushButton_2_2 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_2_2.setGeometry(QtCore.QRect(265, 740, 21, 21))
        self.pushButton_2_2.setStyleSheet("background-color:#F0F2F6;\n"
"border-radius: 5px;")
        self.pushButton_2_2.setText("")
        self.pushButton_2_2.setIcon(icon)
        self.pushButton_2_2.setObjectName("pushButton_2_2")

        self.pushButton_2_1 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_2_1.setGeometry(QtCore.QRect(235, 740, 21, 21))
        self.pushButton_2_1.setStyleSheet("background-color:#F0F2F6;\n"
"border-radius: 5px;")
        self.pushButton_2_1.setText("")
        self.pushButton_2_1.setIcon(icon1)
        self.pushButton_2_1.setObjectName("pushButton_2_1")
        self.pushButton_2_1.clicked.connect(self.switch_2_1)
        self.pushButton_2_3 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_2_3.setGeometry(QtCore.QRect(295, 740, 21, 21))
        self.pushButton_2_3.setStyleSheet("background-color:#F0F2F6;\n"
"border-radius: 5px;")
        self.pushButton_2_3.setText("")
        self.pushButton_2_3.setIcon(icon1)
        self.pushButton_2_3.setObjectName("pushButton_2_3")
        self.pushButton_2_3.clicked.connect(self.switch_2_3)
        self.pushButton_2_4 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_2_4.setGeometry(QtCore.QRect(325, 740, 21, 21))
        self.pushButton_2_4.setStyleSheet("background-color:#F0F2F6;\n"
"border-radius: 5px;")
        self.pushButton_2_4.setText("")
        self.pushButton_2_4.setIcon(icon1)
        self.pushButton_2_4.setObjectName("pushButton_2_4")
        self.pushButton_2_4.clicked.connect(self.switch_2_4)


        self.pushButton_count = QtWidgets.QPushButton(self.page_2)
        self.pushButton_count.setGeometry(QtCore.QRect(0, 620, 551, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_count.setFont(font)
        self.pushButton_count.setStyleSheet("background-color:#787CD1;\n"
"color:white;\n"
"border-radius: 2px;")
        self.pushButton_count.setObjectName("pushButton_count")
        self.pushButton_count.clicked.connect(self.count)


        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_3 = QtWidgets.QLabel(self.page_3)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 550, 800))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Слой 4.png"))
        self.label_3.setObjectName("label_3")
        self.label_conclusion = QtWidgets.QLabel(self.page_3)
        self.label_conclusion.setGeometry(QtCore.QRect(0, 130, 550, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_conclusion.setFont(font)
        self.label_conclusion.setStyleSheet("color: white;")
        self.label_conclusion.setAlignment(QtCore.Qt.AlignCenter)
        self.label_conclusion.setObjectName("label_conclusion")
        self.pushButton_3_1 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_3_1.setGeometry(QtCore.QRect(235, 740, 21, 21))
        self.pushButton_3_1.setStyleSheet("background-color:#F0F2F6;\n"
"border-radius: 5px;")
        self.pushButton_3_1.setText("")
        self.pushButton_3_1.setIcon(icon1)
        self.pushButton_3_1.setObjectName("pushButton_3_1")
        self.pushButton_3_1.clicked.connect(self.switch_3_1)
        self.pushButton_3_2 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_3_2.setGeometry(QtCore.QRect(265, 740, 21, 21))
        self.pushButton_3_2.setStyleSheet("background-color:#F0F2F6;\n"
"border-radius: 5px;")
        self.pushButton_3_2.setText("")
        self.pushButton_3_2.setIcon(icon1)
        self.pushButton_3_2.setObjectName("pushButton_3_2")
        self.pushButton_3_2.clicked.connect(self.switch_3_2)
        self.pushButton_3_4 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_3_4.setGeometry(QtCore.QRect(325, 740, 21, 21))
        self.pushButton_3_4.setStyleSheet("background-color:#F0F2F6;\n"
"border-radius: 5px;")
        self.pushButton_3_4.setText("")
        self.pushButton_3_4.setIcon(icon1)
        self.pushButton_3_4.setObjectName("pushButton_3_4")
        self.pushButton_3_4.clicked.connect(self.switch_3_4)
        self.pushButton_3_3 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_3_3.setGeometry(QtCore.QRect(295, 740, 21, 21))
        self.pushButton_3_3.setStyleSheet("background-color:#F0F2F6;\n"
"border-radius: 5px;")
        self.pushButton_3_3.setText("")
        self.pushButton_3_3.setIcon(icon)
        self.pushButton_3_3.setObjectName("pushButton_3_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_5 = QtWidgets.QLabel(self.page_4)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 550, 800))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("Слой 6.png"))
        self.label_5.setObjectName("label_5")
        self.pushButton_4_1 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_4_1.setGeometry(QtCore.QRect(235, 740, 21, 21))
        self.pushButton_4_1.setStyleSheet("background-color:#302B70;\n"
"border-radius: 5px;")
        self.pushButton_4_1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Слой 7.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4_1.setIcon(icon2)
        self.pushButton_4_1.setObjectName("pushButton_4_1")
        self.pushButton_4_1.clicked.connect(self.switch_4_1)
        self.pushButton_4_2 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_4_2.setGeometry(QtCore.QRect(265, 740, 21, 21))
        self.pushButton_4_2.setStyleSheet("background-color:#302B70;\n"
"border-radius: 5px;")
        self.pushButton_4_2.setText("")
        self.pushButton_4_2.setIcon(icon2)
        self.pushButton_4_2.setObjectName("pushButton_4_2")
        self.pushButton_4_2.clicked.connect(self.switch_4_2)
        self.pushButton_4_3 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_4_3.setGeometry(QtCore.QRect(295, 740, 21, 21))
        self.pushButton_4_3.setStyleSheet("background-color:#302B70;\n"
"border-radius: 5px;")
        self.pushButton_4_3.setText("")
        self.pushButton_4_3.setIcon(icon2)
        self.pushButton_4_3.setObjectName("pushButton_4_3")
        self.pushButton_4_3.clicked.connect(self.switch_4_3)
        self.pushButton_4_4 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_4_4.setGeometry(QtCore.QRect(325, 740, 21, 21))
        self.pushButton_4_4.setStyleSheet("background-color:#302B70;\n"
"border-radius: 5px;")
        self.pushButton_4_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Слой 8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4_4.setIcon(icon3)
        self.pushButton_4_4.setObjectName("pushButton_4_4")
        self.stackedWidget.addWidget(self.page_4)
        Notation.setCentralWidget(self.centralwidget)

        self.retranslateUi(Notation)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Notation)



    def retranslateUi(self, Notation):
        _translate = QtCore.QCoreApplication.translate
        Notation.setWindowTitle(_translate("Notation", "MainWindow"))
        self.pushButton_count.setText(_translate("Notation", "Посчитать"))
        self.label_conclusion.setText(_translate("Notation", "Вывод"))


    def switch_1_2(self,index):
             self.stackedWidget.setCurrentIndex(1)
    def switch_1_3(self,index):
             self.stackedWidget.setCurrentIndex(2)
    def switch_1_4(self,index):
             self.stackedWidget.setCurrentIndex(3)
    def switch_2_1(self,index):
             self.stackedWidget.setCurrentIndex(0)
    def switch_2_3(self,index):
             self.stackedWidget.setCurrentIndex(2)
    def switch_2_4(self,index):
             self.stackedWidget.setCurrentIndex(3)
    def switch_3_1(self,index):
             self.stackedWidget.setCurrentIndex(0)
    def switch_3_2(self,index):
             self.stackedWidget.setCurrentIndex(1)
    def switch_3_4(self,index):
             self.stackedWidget.setCurrentIndex(3)
    def switch_4_1(self,index):
             self.stackedWidget.setCurrentIndex(0)
    def switch_4_2(self,index):
             self.stackedWidget.setCurrentIndex(1)
    def switch_4_3(self,index):
             self.stackedWidget.setCurrentIndex(2)


    def count(self):
        number = self.lineEdit_number.text()
        original_system=self.lineEdit_original_number_system.text()
        finite_system=self.lineEdit_number_system_is_finite.text()
        finite_system = int(finite_system)
        original_system = int(original_system)
        if original_system>10:

            number = [i.replace('A', '10', ) for i in number]
            number = [i.replace('a', '10', ) for i in number]
            number = [i.replace('B', '11', ) for i in number]
            number = [i.replace('b', '11', ) for i in number]
            number = [i.replace('C', '12', ) for i in number]
            number = [i.replace('c', '12', ) for i in number]
            number = [i.replace('D', '13', ) for i in number]
            number = [i.replace('d', '13', ) for i in number]
            number = [i.replace('E', '14', ) for i in number]
            number = [i.replace('e', '14', ) for i in number]
            number = [i.replace('F', '15', ) for i in number]
            number = [i.replace('f', '15', ) for i in number]
            if finite_system == 10:
                res = 0
                result = [int(item) for item in number]
                result_rev = list(reversed(result))
                for i in range(len(result_rev)):
                    res += result_rev[i] * (original_system ** i)  # вывод из 16-ой в 10-ую

            if finite_system < 10:
                resa = 0
                result = [int(item) for item in number]
                result_rev = list(reversed(result))
                for i in range(len(result_rev)):
                    resa += result_rev[i] * (original_system ** i)
                res = ''
                while resa > 0:
                    res = res + str(resa % finite_system)  # перевод из любой в любую?
                    resa = resa // finite_system
                res=(''.join(reversed(res)))



            if finite_system>10:
                res = []
                while number_10 > 0:
                    res.append(number_10 % finite_system)
                    number_10 = number_10 // finite_system
                    for i in range(len(res)):
                        if res[i] == 10:
                            res[i] = 'A'
                        if res[i] == 11:
                            res[i] = 'B'
                        if res[i] == 12:
                            res[i] = 'C'
                        if res[i] == 13:
                            res[i] = 'D'
                        if res[i] == 14:
                            res[i] = 'E'
                        if res[i] == 15:
                            res[i] = 'F'
                res = ("".join(map(str, res)))
                res = (''.join(reversed(res)))




        if  original_system<=10:
            if finite_system <= 10:
                number = int(number)
                number = (str(number))
                resu = int(number, original_system)
                res = ''
                while resu > 0:
                    res = res + str(resu % finite_system)  # перевод из любой в любую?
                    resu = resu // finite_system
                res=(''.join(reversed(res)))
            if finite_system>10:
                number = str(number)
                number_10 = int(number, original_system)
                res = []
                while number_10 > 0:
                    res.append(number_10 % finite_system)
                    number_10 = number_10 // finite_system
                    for i in range(len(res)):
                        if res[i] == 10:
                            res[i] = 'A'
                        if res[i] == 11:
                            res[i] = 'B'
                        if res[i] == 12:
                            res[i] = 'C'
                        if res[i] == 13:
                            res[i] = 'D'
                        if res[i] == 14:
                            res[i] = 'E'
                        if res[i] == 15:
                            res[i] = 'F'
                res = ("".join(map(str, res)))
                res = (''.join(reversed(res)))



        res = str(res)
        if len(res)>23:
            error=QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Слишком большое число")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()
        else:
            self.stackedWidget.setCurrentIndex(2)
            self.label_conclusion.setText(res)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Notation = QtWidgets.QMainWindow()
    ui = Ui_Notation()
    ui.setupUi(Notation)
    Notation.show()
    sys.exit(app.exec_())