# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI3.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Optimus(object):
    def setupUi(self, Optimus):
        Optimus.setObjectName("Optimus")
        Optimus.resize(893, 597)
        Optimus.setMaximumSize(QtCore.QSize(893, 597))
        Optimus.setWindowIcon(QtGui.QIcon(
            r"Images\logo1.png"))
        self.centralwidget = QtWidgets.QWidget(Optimus)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 891, 561))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(
            r"Images\7LP8.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(710, 520, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setMouseTracking(False)
        self.pushButton.setStyleSheet("background: transparent;\n"
                                      "color: #9FD3E9;\n"
                                      "border: 1px solid #9FD3E9;"
                                      )
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(780, 520, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setMouseTracking(False)
        self.pushButton_2.setStyleSheet("background: transparent;\n"
                                        "color: #9FD3E9;\n"
                                        "border: 1px solid #9FD3E9;\n"
                                        )
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 371, 81))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(
            r"Images\T8bahf.gif"))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(530, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background: transparent;\n"
                                       "color: #9FD3E9;\n"
                                       "border: none;\n"
                                       "letter-spacing: 3px;\n"
                                       "font-size: 15px;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(700, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("background: transparent;\n"
                                         "color: #9FD3E9;\n"
                                         "border: none;\n"
                                         "letter-spacing: 3px;\n"
                                         "font-size: 15px;\n"
                                         )
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(590, 320, 281, 171))
        self.label_3.setText(
            "")
        self.label_3.setObjectName("label_3")
        self.label_3.setWordWrap(True)
        # self.label_3 = ScrollLabel(self)
        self.label_3.setStyleSheet("background: transparent;\n"
                                   "color: #9FD3E9;\n"
                                   "border: 1px dotted #9FD3E9;\n"
                                   "letter-spacing: 3px;\n"
                                   "font-size: 15px;\n"
                                   )

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 320, 150, 140))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(
            r"Images\7LP8.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("background: transparent;\n"
                                   "color: #9FD3E9;\n"
                                   "border: none;\n"
                                   "letter-spacing: 3px;\n"
                                   "font-size: 15px;\n"
                                   )
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 320, 150, 150))
        self.label_5.setText("OPTIMUS")
        self.label_5.setStyleSheet("background: transparent;\n"
                                   "color: #9FD3E9;\n"
                                   "border: none;\n"
                                   "letter-spacing: 5px;\n"
                                   "font-size: 25px;\n"
                                   "font-weight: bold;\n"
                                   )
        Optimus.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Optimus)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 893, 21))
        self.menubar.setObjectName("menubar")
        Optimus.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Optimus)
        self.statusbar.setObjectName("statusbar")
        Optimus.setStatusBar(self.statusbar)

        self.retranslateUi(Optimus)
        QtCore.QMetaObject.connectSlotsByName(Optimus)

    def retranslateUi(self, Optimus):
        _translate = QtCore.QCoreApplication.translate
        Optimus.setWindowTitle(_translate("Optimus", "Optimus"))
        self.pushButton.setText(_translate("Optimus", "RUN"))
        self.pushButton_2.setText(_translate("Optimus", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Optimus = QtWidgets.QMainWindow()
    ui = Ui_Optimus()
    ui.setupUi(Optimus)
    Optimus.show()
    sys.exit(app.exec_())
