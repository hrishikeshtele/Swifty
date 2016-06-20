# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_pg.ui'
#
# Created: Fri Aug 28 01:31:55 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1554, 929)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(_fromUtf8("\n"
"background-color: rgb(44, 44,44);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setStyleSheet(_fromUtf8("background-image: url(:/ht/letters3.png);"))
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout_3.addWidget(self.textBrowser)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 2, 4, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setText(_fromUtf8(""))
        self.label_7.setPixmap(QtGui.QPixmap(_fromUtf8("credenz.png")))
        self.label_7.setScaledContents(False)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.gridLayout_3.addLayout(self.verticalLayout, 1, 0, 4, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier 10 Pitch"))
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label.setStyleSheet(_fromUtf8("font: 75 italic 36pt \"Courier 10 Pitch\";\n"
"\n"
"color: rgb(255, 255, 255)"))
        self.label.setText(_fromUtf8(""))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 1, 1, 1, 4)
        self.login = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Eras Medium ITC"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.login.setFont(font)
        self.login.setStyleSheet(_fromUtf8("font: 18pt \"Eras Medium ITC\";\n"
"background-image: url(:/ht/butt3.png);\n"
"color: rgb(255, 255, 255)"))
        self.login.setObjectName(_fromUtf8("login"))
        self.gridLayout_3.addWidget(self.login, 4, 2, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setStyleSheet(_fromUtf8("\n"
"font: 22pt \"Eras Medium ITC\";\n"
"color: rgb(255, 255, 255)"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setStyleSheet(_fromUtf8("font: 22pt \"Eras Medium ITC\";\n"
"color: rgb(255, 255, 255)"))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_2.addWidget(self.label_5)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setStyleSheet(_fromUtf8("font: 22pt \"Eras Medium ITC\";\n"
"color: rgb(255, 255, 255)"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_2.addWidget(self.label_4)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setStyleSheet(_fromUtf8("font: 22pt \"Eras Medium ITC\";\n"
"color: rgb(255, 255, 255)"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 2, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 75 italic 36pt \"Courier 10 Pitch\";"))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_3.addWidget(self.label_9)
        self.horizontalLayout.addLayout(self.horizontalLayout_3)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8(":/ht/ieee.png")))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout.addWidget(self.label_6)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 5)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setStyleSheet(_fromUtf8("color: rgb(44, 44, 44);"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 3, 1, 1)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShadow(QtGui.QFrame.Plain)
        self.line.setLineWidth(20)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_3.addWidget(self.line, 5, 0, 1, 5)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 3, 2, 1, 1)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setSpacing(7)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem6)
        self.nam = QtGui.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Eras Medium ITC"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.nam.setFont(font)
        self.nam.setStyleSheet(_fromUtf8("font: 16pt \"Eras Medium ITC\";\n"
"background-image: url(:/ht/backi1.png);\n"
"color: rgb(66, 66, 66)"))
        self.nam.setInputMethodHints(QtCore.Qt.ImhPreferLowercase|QtCore.Qt.ImhPreferUppercase)
        self.nam.setText(_fromUtf8(""))
        self.nam.setObjectName(_fromUtf8("nam"))
        self.verticalLayout_4.addWidget(self.nam)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem7)
        self.rec = QtGui.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Eras Medium ITC"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.rec.setFont(font)
        self.rec.setStyleSheet(_fromUtf8("font: 16pt \"Eras Medium ITC\";\n"
"background-image: url(:/ht/backi1.png);\n"
"color: rgb(66, 66, 66)"))
        self.rec.setObjectName(_fromUtf8("rec"))
        self.verticalLayout_4.addWidget(self.rec)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem8)
        self.col = QtGui.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Eras Medium ITC"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.col.setFont(font)
        self.col.setStyleSheet(_fromUtf8("font: 16pt \"Eras Medium ITC\";\n"
"background-image: url(:/ht/backi1.png);\n"
"color: rgb(66, 66, 66)"))
        self.col.setObjectName(_fromUtf8("col"))
        self.verticalLayout_4.addWidget(self.col)
        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem9)
        self.mob = QtGui.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Eras Medium ITC"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.mob.setFont(font)
        self.mob.setAutoFillBackground(False)
        self.mob.setStyleSheet(_fromUtf8("font: 16pt \"Eras Medium ITC\";\n"
"background-image: url(:/ht/backi1.png);\n"
"color: rgb(66, 66, 66)"))
        self.mob.setObjectName(_fromUtf8("mob"))
        self.verticalLayout_4.addWidget(self.mob)
        spacerItem10 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem10)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 2, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Swift-Typer", None))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600; text-decoration: underline; color:#c3c3c3;\">INSTRUCTIONS</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">1)ROUND WILL  BE OF 1:30 MINUTES.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">2)ACCURACY WILL BE CALCULATED ACCORDING TO </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">WORDS PER MINUTE &amp; CORRECTNESS.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">3)CORRECT LETTERS WILL BE HIGHLIGHTED IN</span> <span style=\" color:#49dc00;\">GREEN</span><span style=\" color:#ffffff;\">.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">4)WRONG LETTERS  WILL BE HIGHLIGHTED IN </span><span style=\" color:#f00000;\">RED</span><span style=\" color:#ffffff;\">.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">5) CORRECTNESS CALCULATED AS :</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\"> FIVE CORRECT LETTERS WILL BE CONSIDERED AS ONE CORRECT WORD.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">eg:</span><span style=\" color:#000000;\"> </span><span style=\" color:#ffffff;\">HRISHIKESH </span><span style=\" color:#000000;\"> </span><span style=\" color:#ffffff;\">10 CORRECT LETTERS  WILL BE</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">CONSIDERED AS</span><span style=\" color:#000000;\"> </span><span style=\" text-decoration: underline; color:#aa0000;\">TWO</span><span style=\" color:#000000;\"> </span><span style=\" color:#ffffff;\">CORRECT WORD.</span></p></body></html>", None))
        self.login.setText(_translate("MainWindow", "LOGIN", None))
        self.label_2.setText(_translate("MainWindow", "NAME", None))
        self.label_5.setText(_translate("MainWindow", "RECEIPT NO.", None))
        self.label_4.setText(_translate("MainWindow", "COLLEGE", None))
        self.label_3.setText(_translate("MainWindow", "MOBILE NO.", None))
        self.label_9.setText(_translate("MainWindow", "SWIFT TYPER \'15_", None))
        self.label_8.setText(_translate("MainWindow", "Swifttyper", None))

import ht1_rc
