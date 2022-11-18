# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_jarvisui(object):
    def setupUi(self, jarvisui):
        jarvisui.setObjectName("jarvisui")
        jarvisui.resize(814, 599)
        jarvisui.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(jarvisui)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 400, 161, 141))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("2RNb.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.run_btn = QtWidgets.QPushButton(self.centralwidget)
        self.run_btn.setGeometry(QtCore.QRect(650, 500, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(14)
        self.run_btn.setFont(font)
        self.run_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.run_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 0);")
        self.run_btn.setObjectName("run_btn")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 0, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.run_btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.run_btn_2.setGeometry(QtCore.QRect(730, 500, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(14)
        self.run_btn_2.setFont(font)
        self.run_btn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.run_btn_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(236, 0, 0);")
        self.run_btn_2.setObjectName("run_btn_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 530, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 801, 391))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 401, 81))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("T8bahf.gif"))
        self.label_4.setObjectName("label_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(430, 20, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background:transparent;\n"
"border-radius: none;\n"
"color: #fff;\n"
"font-size: 20px\n;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(610, 20, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("background:transparent;\n"
"border-radius: none;\n"
"color: #fff;\n"
"font-size: 20px\n;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 100, 771, 281))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("frame.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(140, 140, 551, 201))
        self.textBrowser_3.setObjectName("textBrowser_3")
        jarvisui.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(jarvisui)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 814, 21))
        self.menubar.setObjectName("menubar")
        jarvisui.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(jarvisui)
        self.statusbar.setObjectName("statusbar")
        jarvisui.setStatusBar(self.statusbar)

        self.retranslateUi(jarvisui)
        QtCore.QMetaObject.connectSlotsByName(jarvisui)

    def retranslateUi(self, jarvisui):
        _translate = QtCore.QCoreApplication.translate
        jarvisui.setWindowTitle(_translate("jarvisui", "MainWindow"))
        self.run_btn.setText(_translate("jarvisui", "RUN"))
        self.pushButton_2.setText(_translate("jarvisui", "PushButton"))
        self.run_btn_2.setText(_translate("jarvisui", "STOP"))
        self.label_2.setText(_translate("jarvisui", "Listening..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    jarvisui = QtWidgets.QMainWindow()
    ui = Ui_jarvisui()
    ui.setupUi(jarvisui)
    jarvisui.show()
    sys.exit(app.exec_())
