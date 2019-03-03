# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sfz.ui',
# licensing of 'sfz.ui' applies.
#
# Created: Tue Jan 15 22:42:05 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(693, 424)
        self.lEditResult = QtWidgets.QLineEdit(Form)
        self.lEditResult.setGeometry(QtCore.QRect(190, 120, 331, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lEditResult.setFont(font)
        self.lEditResult.setReadOnly(True)
        self.lEditResult.setObjectName("lEditResult")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(110, 330, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.btnQuery = QtWidgets.QPushButton(Form)
        self.btnQuery.setGeometry(QtCore.QRect(560, 50, 93, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.btnQuery.setFont(font)
        self.btnQuery.setObjectName("btnQuery")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 120, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(110, 260, 71, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.btnClear = QtWidgets.QPushButton(Form)
        self.btnClear.setGeometry(QtCore.QRect(560, 120, 93, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.btnClear.setFont(font)
        self.btnClear.setObjectName("btnClear")
        self.label1 = QtWidgets.QLabel(Form)
        self.label1.setGeometry(QtCore.QRect(50, 50, 131, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.lEditBirth = QtWidgets.QLineEdit(Form)
        self.lEditBirth.setGeometry(QtCore.QRect(190, 261, 331, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lEditBirth.setFont(font)
        self.lEditBirth.setReadOnly(True)
        self.lEditBirth.setObjectName("lEditBirth")
        self.lEditRegion = QtWidgets.QLineEdit(Form)
        self.lEditRegion.setGeometry(QtCore.QRect(190, 190, 331, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lEditRegion.setFont(font)
        self.lEditRegion.setReadOnly(True)
        self.lEditRegion.setObjectName("lEditRegion")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(110, 190, 61, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lEditGender = QtWidgets.QLineEdit(Form)
        self.lEditGender.setGeometry(QtCore.QRect(190, 330, 331, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lEditGender.setFont(font)
        self.lEditGender.setReadOnly(True)
        self.lEditGender.setObjectName("lEditGender")
        self.lEditNum = QtWidgets.QLineEdit(Form)
        self.lEditNum.setGeometry(QtCore.QRect(190, 50, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.lEditNum.setFont(font)
        self.lEditNum.setReadOnly(False)
        self.lEditNum.setObjectName("lEditNum")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate(
            "Form", "身份证验证", None, -1))
        self.label_5.setText(
            QtWidgets.QApplication.translate("Form", "性别：", None, -1))
        self.btnQuery.setText(
            QtWidgets.QApplication.translate("Form", "查询", None, -1))
        self.label_2.setText(
            QtWidgets.QApplication.translate("Form", "查询结果：", None, -1))
        self.label_4.setText(
            QtWidgets.QApplication.translate("Form", "生日：", None, -1))
        self.btnClear.setText(
            QtWidgets.QApplication.translate("Form", "清除", None, -1))
        self.label1.setText(QtWidgets.QApplication.translate(
            "Form", "18位身份证：", None, -1))
        self.label_3.setText(
            QtWidgets.QApplication.translate("Form", "地区：", None, -1))
