# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
import myLabel
from PyQt5.QtGui import QPixmap, QMovie


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1160, 865)
        Form.setStyleSheet("background-color: rgb(198, 255, 202);")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(640, 800, 150, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet('QPushButton{background:#9AFF9A;border-radius:5px;}QPushButton:hover{background:orange;}')
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 80, 1111, 151))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.groupBox.setFont(font)
        self.groupBox.setToolTipDuration(-3)
        self.groupBox.setStyleSheet("background-color: rgb(139, 253, 255);\n"
"color: rgb(48, 48, 48);\n"
"font: 75 9pt \"Arial\";\n"
"border-color: rgb(0, 170, 0);")
        self.groupBox.setObjectName("groupBox")
        font_doubleSpinBox = QtGui.QFont()
        font_doubleSpinBox.setFamily("Arial")
        font_doubleSpinBox.setPointSize(20)
        font_doubleSpinBox.setBold(True)
        font_doubleSpinBox.setWeight(9)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox.setGeometry(QtCore.QRect(710, 30, 71, 41))
        self.doubleSpinBox.setStyleSheet("background-color: rgb(255, 251, 228);")
        self.doubleSpinBox.setRange(14, 17)
        self.doubleSpinBox.setSingleStep(0.1)
        self.doubleSpinBox.setDecimals(1)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox.setFont(font_doubleSpinBox)
        self.doubleSpinBox.setStyleSheet("background-color: rgb(255, 251, 228);\n"
                                           "font: 90 18pt \"Arial\";")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(630, 30, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(450, 30, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(530, 30, 71, 41))
        self.doubleSpinBox_3.setStyleSheet("background-color: rgb(255, 251, 228);")
        self.doubleSpinBox_3.setSingleStep(0.1)
        self.doubleSpinBox_3.setDecimals(1)
        self.doubleSpinBox_3.setRange(5, 7)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.doubleSpinBox_3.setFont(font_doubleSpinBox)
        self.doubleSpinBox_3.setStyleSheet("background-color: rgb(255, 251, 228);\n"
                                         "font: 90 18pt \"Arial\";")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(800, 30, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setReadOnly(True)
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_4.setGeometry(QtCore.QRect(900, 30, 91, 41))
        self.doubleSpinBox_4.setStyleSheet("background-color: rgb(255, 251, 228);")
        self.doubleSpinBox_4.setRange(1.10, 1.30)
        self.doubleSpinBox_4.setSingleStep(0.01)
        self.doubleSpinBox_4.setLineEdit(self.lineEdit_3)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.doubleSpinBox_4.setFont(font_doubleSpinBox)
        self.doubleSpinBox_4.setStyleSheet("background-color: rgb(255, 251, 228);\n"
                                         "font: 90 18pt \"Arial\";")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(220, 100, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_5.setGeometry(QtCore.QRect(280, 100, 91, 41))
        self.doubleSpinBox_5.setStyleSheet("background-color: rgb(255, 251, 228);")
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.doubleSpinBox_5.setRange(0.25, 0.35)
        self.doubleSpinBox_5.setSingleStep(0.01)
        self.doubleSpinBox_5.setDecimals(3)
        self.doubleSpinBox_5.setFont(font_doubleSpinBox)
        self.doubleSpinBox_5.setStyleSheet("background-color: rgb(255, 251, 228);\n"
                                         "font: 90 18pt \"Arial\";")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(400, 100, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.doubleSpinBox_6 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_6.setGeometry(QtCore.QRect(530, 100, 81, 41))
        self.doubleSpinBox_6.setStyleSheet("background-color: rgb(255, 251, 228);")
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.doubleSpinBox_6.setDecimals(2)
        self.doubleSpinBox_6.setSingleStep(0.1)
        self.doubleSpinBox_6.setRange(2.5, 4.5)
        self.doubleSpinBox_6.setFont(font_doubleSpinBox)
        self.doubleSpinBox_6.setStyleSheet("background-color: rgb(255, 251, 228);\n"
                                         "font: 90 18pt \"Arial\";")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(640, 100, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.doubleSpinBox_7 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_7.setGeometry(QtCore.QRect(730, 100, 91, 41))
        self.doubleSpinBox_7.setStyleSheet("background-color: rgb(255, 251, 228);")
        self.doubleSpinBox_7.setObjectName("doubleSpinBox_7")
        self.doubleSpinBox_7.setRange(1400, 1560)
        self.doubleSpinBox_7.setValue(1500)
        self.doubleSpinBox_7.setSingleStep(1)
        self.doubleSpinBox_7.setDecimals(0)
        self.doubleSpinBox_7.setFont(font_doubleSpinBox)
        self.doubleSpinBox_7.setStyleSheet("background-color: rgb(255, 251, 228);\n"
                                         "font: 90 18pt \"Arial\";")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(90, 30, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(280, 30, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(650, 70, 121, 21))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("font: 9pt \"宋体\";")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(470, 70, 121, 21))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("font: 9pt \"宋体\";")
        self.label_15.setObjectName("label_15")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(170, 30, 91, 41))
        self.textEdit.setStyleSheet("background-color: rgb(255, 251, 228);")
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setText('40.85')
        self.textEdit.setDisabled(True)
        self.textEdit.setStyleSheet("background-color: rgb(255, 251, 228);\n"
                                           "font: 90 18pt \"Arial\";")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_2.setGeometry(QtCore.QRect(350, 30, 81, 41))
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 251, 228);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setText('37.14')
        self.textEdit_2.setDisabled(True)
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 251, 228);\n"
                                    "font: 90 18pt \"Arial\";")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(50, 250, 551, 341))
        self.groupBox_2.setStyleSheet("font: 9pt \"宋体\";\n"
                                      "background-color: rgb(179, 231, 255);\n"
                                      )
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("font: 9pt \"宋体\";\n"
"background-color: rgb(179, 231, 255);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 50, 50))
        self.label_2.setObjectName("label_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(10, 150, 50, 50))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(10, 260, 50, 50))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(70, 40, 221, 20))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(70, 150, 191, 20))
        self.label_11.setObjectName("label_11")
        self.label_16 = QtWidgets.QLabel(self.groupBox_2)
        self.label_16.setGeometry(QtCore.QRect(70, 260, 201, 20))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        self.label_17.setGeometry(QtCore.QRect(70, 70, 301, 41))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox_2)
        self.label_18.setGeometry(QtCore.QRect(70, 180, 310, 41))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.groupBox_2)
        self.label_19.setGeometry(QtCore.QRect(70, 280, 301, 41))
        self.label_19.setObjectName("label_19")
        self.label_20 = myLabel.MyQLabel(self.groupBox_2)
        self.label_20.setGeometry(QtCore.QRect(470, 260, 50, 50))
        self.label_20.setObjectName("label_20")
        self.label_21 = myLabel.MyQLabel(self.groupBox_2)
        self.label_21.setGeometry(QtCore.QRect(470, 150, 50, 50))
        self.label_21.setObjectName("label_21")
        self.label_22 = myLabel.MyQLabel(self.groupBox_2)
        self.label_22.setGeometry(QtCore.QRect(470, 40, 50, 50))
        self.label_22.setObjectName("label_22")
        self.label_37 = QtWidgets.QLabel(self.groupBox_2)
        self.label_37.setGeometry(QtCore.QRect(420, 80, 51, 16))
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.groupBox_2)
        self.label_38.setGeometry(QtCore.QRect(420, 190, 31, 16))
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.groupBox_2)
        self.label_39.setGeometry(QtCore.QRect(420, 290, 51, 16))
        self.label_39.setObjectName("label_39")
        self.label_43 = QtWidgets.QLabel(self.groupBox_2)
        self.label_43.setVisible(False)
        self.label_43.setGeometry(QtCore.QRect(220, 110, 311, 31))
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.groupBox_2)
        self.label_44.setGeometry(QtCore.QRect(220, 210, 311, 31))
        self.label_44.setObjectName("label_44")
        self.label_44.setVisible(False)
        self.label_45 = QtWidgets.QLabel(self.groupBox_2)
        self.label_45.setGeometry(QtCore.QRect(220, 310, 311, 31))
        self.label_45.setObjectName("label_45")
        self.label_45.setVisible(False)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 800, 150, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(
                'QPushButton{background:#9AFF9A;border-radius:5px;}QPushButton:hover{background:orange;}')
        self.pushButton_2.setObjectName("pushButton_2")
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        font.setWeight(50)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setFont(font)
        self.textBrowser.setGeometry(QtCore.QRect(30, 620, 1071, 161))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.label_24 = myLabel.MyQLabel(Form)
        self.label_24.setGeometry(QtCore.QRect(10, 10, 126, 41))
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.label_26 = QtWidgets.QLabel(Form)
        self.label_26.setGeometry(QtCore.QRect(300, 10, 781, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(23)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(650, 250, 441, 341))
        self.groupBox_3.setStyleSheet("font: 9pt \"宋体\";\n"
"background-color: rgb(179, 231, 255);")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_29 = QtWidgets.QLabel(self.groupBox_3)
        self.label_29.setGeometry(QtCore.QRect(20, 40, 50, 50))
        self.label_29.setObjectName("label_29")
        self.label_27 = QtWidgets.QLabel(self.groupBox_3)
        self.label_27.setGeometry(QtCore.QRect(20, 260, 50, 50))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.groupBox_3)
        self.label_28.setGeometry(QtCore.QRect(20, 150, 50, 50))
        self.label_28.setObjectName("label_28")
        self.label_35 = QtWidgets.QLabel(self.groupBox_3)
        self.label_35.setGeometry(QtCore.QRect(90, 150, 221, 20))
        self.label_35.setObjectName("label_35")
        self.label_32 = QtWidgets.QLabel(self.groupBox_3)
        self.label_32.setGeometry(QtCore.QRect(90, 40, 221, 20))
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.groupBox_3)
        self.label_33.setGeometry(QtCore.QRect(90, 180, 310, 41))
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.groupBox_3)
        self.label_34.setGeometry(QtCore.QRect(90, 70, 310, 41))
        self.label_34.setObjectName("label_34")
        self.label_31 = QtWidgets.QLabel(self.groupBox_3)
        self.label_31.setGeometry(QtCore.QRect(90, 290, 310, 41))
        self.label_31.setObjectName("label_31")
        self.label_30 = QtWidgets.QLabel(self.groupBox_3)
        self.label_30.setGeometry(QtCore.QRect(90, 260, 221, 20))
        self.label_30.setObjectName("label_30")
        self.label_42 = QtWidgets.QLabel(self.groupBox_3)
        self.label_42.setGeometry(QtCore.QRect(400, 70, 51, 16))
        self.label_42.setObjectName("label_42")
        self.label_40 = QtWidgets.QLabel(self.groupBox_3)
        self.label_40.setGeometry(QtCore.QRect(400, 180, 31, 16))
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.groupBox_3)
        self.label_41.setGeometry(QtCore.QRect(390, 290, 51, 16))
        self.label_41.setObjectName("label_41")
        self.label_25 = myLabel.MyQLabel(Form)
        self.label_25.setGeometry(QtCore.QRect(1060, 820, 85, 41))
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.label_23 = QtWidgets.QLabel(Form)
        self.label_23.setGeometry(QtCore.QRect(10, 790, 470, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_36 = QtWidgets.QLabel(Form)
        self.label_36.setFont(font)
        self.label_36.setGeometry(QtCore.QRect(30, 590, 221, 31))
        self.label_36.setObjectName("label_36")
        self.label_46 = QtWidgets.QLabel(self.groupBox)
        self.label_46.setGeometry(QtCore.QRect(870, 70, 201, 16))
        self.label_46.setObjectName("label_46")
        self.label_31.setStyleSheet("font: 18pt \"Arial\";")
        self.label_33.setStyleSheet("font: 18pt \"Arial\";")
        self.label_34.setStyleSheet("font: 18pt \"Arial\";")
        self.label_17.setStyleSheet("font: 18pt \"Arial\";")
        self.label_18.setStyleSheet("font: 18pt \"Arial\";")
        self.label_19.setStyleSheet("font: 18pt \"Arial\";")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(800, 800, 181, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(
                'QPushButton{background:#9AFF9A;border-radius:5px;}QPushButton:hover{background:orange;}')
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(990, 800, 150, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet('QPushButton{background:#9AFF9A;border-radius:5px;}QPushButton:hover{background:orange;}')
        self.pushButton_4.setObjectName("pushButton_4")

        # self.doubleSpinBox_8 = QtWidgets.QDoubleSpinBox(self.groupBox)
        # self.doubleSpinBox_8.setGeometry(QtCore.QRect(820, 100, 91, 41))
        # self.doubleSpinBox_8.setRange(0, 2)
        # self.doubleSpinBox_8.setValue(1)
        # self.doubleSpinBox_8.setSingleStep(0.01)
        # self.doubleSpinBox_8.setDecimals(2)
        # self.doubleSpinBox_8.setObjectName("doubleSpinBox_8")
        # self.doubleSpinBox_8.setStyleSheet("background-color: rgb(255, 251, 228);\n"
        #                                    "font: 90 18pt \"Arial\";")
        # self.label_47 = QtWidgets.QLabel(self.groupBox)
        # self.label_47.setGeometry(QtCore.QRect(750, 100, 61, 41))
        # font = QtGui.QFont()
        # font.setFamily("Arial")
        # font.setPointSize(9)
        # font.setBold(False)
        # font.setItalic(False)
        # font.setWeight(9)
        # self.label_47.setFont(font)
        # self.label_47.setObjectName("label_47")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.on_pushButton2_clicked)
        self.pushButton_3.clicked.connect(Form.on_pushButton3_clicked)
        self.doubleSpinBox.valueChanged.connect(Form.on_doubleSpinBox_valueChanged)
        self.doubleSpinBox_3.valueChanged.connect(Form.on_doubleSpinBox_valueChanged)
        self.doubleSpinBox_4.valueChanged.connect(Form.on_doubleSpinBox_valueChanged)
        self.pushButton_2.clicked.connect(Form.on_pushButton_clicked)
        self.pushButton_4.clicked.connect(Form.on_pushButton4_clicked)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Software for predicting slag performance"))
        self.pushButton.setText(_translate("Form", "Numerical results"))
        self.groupBox.setTitle(_translate("Form", "Input"))
        self.label.setText(_translate("Form", "Al2O3 (wt%):"))
        self.label_3.setText(_translate("Form", "MgO (wt%)："))
        self.label_4.setText(_translate("Form", "R："))
        self.label_5.setText(_translate("Form", "slag ratio:"))
        self.label_6.setText(_translate("Form", "sulfur partition ratio:"))
        self.label_7.setText(_translate("Form", "T (℃):"))
        self.label_12.setText(_translate("Form", "CaO (wt%):"))
        self.label_13.setText(_translate("Form", "SiO2 (wt%):"))
        self.label_14.setText(_translate("Form", "range from 14 to 7"))
        self.label_15.setText(_translate("Form", "range from 5 to 7"))
        self.textEdit.setHtml(_translate("Form",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'Arial\'; font-size:9pt; font-weight:72; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">11111</p></body></html>"))
        self.label_46.setText(_translate("Form", "Note：CaO+SiO2+MgO+Al2O3=100"))
        self.groupBox_2.setTitle(_translate("Form", "Output"))
        self.label_2.setText(_translate("Form", "image1"))
        self.label_8.setText(_translate("Form", "image1"))
        self.label_9.setText(_translate("Form", "image1"))
        self.label_10.setText(_translate("Form", "Desulfurization of slag"))
        self.label_11.setText(_translate("Form", "Melting performance of slag"))
        self.label_16.setText(_translate("Form", "Viscosity of slag"))
        self.label_17.setText(_translate("Form", "123"))
        self.label_18.setText(_translate("Form", "None"))
        self.label_19.setText(_translate("Form", "None"))
        self.label_20.setText(_translate("Form", "image1"))
        self.label_21.setText(_translate("Form", "image1"))
        self.label_22.setText(_translate("Form", "image1"))
        self.label_29.setPixmap(QPixmap(r'.\image3.png'))
        self.label_27.setPixmap(QPixmap(r'.\image3.png'))
        self.label_28.setPixmap(QPixmap(r'.\image3.png'))
        self.label_37.setText(_translate("Form", "(wt%)"))
        self.label_38.setText(_translate("Form", "(℃)"))
        self.label_39.setText(_translate("Form", "(Pa·s)"))
        self.label_43.setText(_translate("Form",
                                         "↑ indicates an increase from the previous period, \n↓ indicates a decrease from the previous period"))
        self.label_44.setText(_translate("Form",
                                         "↑ indicates an increase from the previous period, \n↓ indicates a decrease from the previous period"))
        self.label_45.setText(_translate("Form",
                                         "↑ indicates an increase from the previous period, \n↓ indicates a decrease from the previous period"))
        self.pushButton_2.setText(_translate("Form", "Image Results"))
        self.label_20.setPixmap(QPixmap(r'.\image2.png'))
        self.label_21.setPixmap(QPixmap(r'.\image2.png'))
        self.label_22.setPixmap(QPixmap(r'.\image2.png'))
        self.label_2.setPixmap(QPixmap(r'.\image1.png'))
        self.label_8.setPixmap(QPixmap(r'.\image1.png'))
        self.label_9.setPixmap(QPixmap(r'.\image1.png'))
        self.textBrowser.setHtml(_translate("Form",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_26.setText(_translate("Form", "Predicting slag performance v1.0"))
        self.groupBox_3.setTitle(_translate("Form", "Last Output"))
        self.label_29.setPixmap(QPixmap(r'.\image3.png'))
        self.label_27.setPixmap(QPixmap(r'.\image3.png'))
        self.label_28.setPixmap(QPixmap(r'.\image3.png'))
        self.label_35.setText(_translate("Form", "Melting performance of slag"))
        self.label_32.setText(_translate("Form", "Desulfurization of slag"))
        self.label_33.setText(_translate("Form", "None"))
        self.label_34.setText(_translate("Form", "None"))
        self.label_31.setText(_translate("Form", "None"))
        self.label_30.setText(_translate("Form", "Viscosity of slag"))
        self.label_42.setText(_translate("Form", "(wt%)"))
        self.label_40.setText(_translate("Form", "(℃)"))
        self.label_41.setText(_translate("Form", "(Pa·s)"))
        self.label_23.setText(_translate("Form", "Notes: \n"
                                                 "[s] sulfur content in iron; \n"
                                                 "T20%: start melting temperature, T80%: end melting temperature. \n"
                                                 " ↑ indicates an increase from the previous one, ↓ indicates a decrease from the previous one."))
        self.label_36.setText(_translate("Form", "History Information"))
        self.pushButton_3.setText(_translate("Form", "Visualization History"))
        self.pushButton_4.setText(_translate("Form", "Clear records"))

