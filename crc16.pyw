# -*- coding: utf-8 -*-
import sys
from PySide2.QtWidgets import QApplication, QDialog
from PySide2 import QtCore, QtGui, QtWidgets



class Ui_dlgMain(object):
    def setupUi(self, dlgMain):
        dlgMain.setObjectName("dlgMain")
        dlgMain.resize(709, 332)
        self.label = QtWidgets.QLabel(dlgMain)
        self.label.setGeometry(QtCore.QRect(40, 60, 51, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(dlgMain)
        self.pushButton.setGeometry(QtCore.QRect(590, 50, 93, 41))
        self.pushButton.setObjectName("pushButton")
        self.lEdit_2 = QtWidgets.QLineEdit(dlgMain)
        self.lEdit_2.setGeometry(QtCore.QRect(90, 220, 481, 31))
        self.lEdit_2.setObjectName("lEdit_2")
        self.label_2 = QtWidgets.QLabel(dlgMain)
        self.label_2.setGeometry(QtCore.QRect(40, 230, 51, 16))
        self.label_2.setObjectName("label_2")
        self.lEdit = QtWidgets.QLineEdit(dlgMain)
        self.lEdit.setGeometry(QtCore.QRect(80, 50, 491, 31))
        self.lEdit.setObjectName("lEdit")

        self.retranslateUi(dlgMain)
        QtCore.QMetaObject.connectSlotsByName(dlgMain)

    def retranslateUi(self, dlgMain):
        dlgMain.setWindowTitle(QtWidgets.QApplication.translate(
            "dlgMain", "CRC16计算", None, -1))
        self.label.setText(QtWidgets.QApplication.translate(
            "dlgMain", "输入:", None, -1))
        self.pushButton.setText(
            QtWidgets.QApplication.translate("dlgMain", "计算", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate(
            "dlgMain", "结果:", None, -1))


class Crc16_dlg(Ui_dlgMain, QDialog, object):
    def __init__(self, parent=None):
        super(Crc16_dlg, self).__init__()

    def calcCrc(self):
        toCalc = self.lEdit.text().strip()
        _crc16 = self.crc16(toCalc).upper()
        self.lEdit_2.setText(_crc16)

    def setupUi(self):
        super(Crc16_dlg, self).setupUi(self)
        self.pushButton.clicked.connect(self.calcCrc)
        self.lEdit.setValidator(QtGui.QRegExpValidator(
            QtCore.QRegExp('^[A-Fa-f0-9]*$'), self.lEdit))

    def crc16(self,string):
        data = bytearray.fromhex(string)
        crc = 0xFFFF
        for pos in data:
            crc ^= pos
            for i in range(8):
                if ((crc & 1) != 0):
                    crc >>= 1
                    crc ^= 0xA001
                else:
                    crc >>= 1
        return hex(((crc & 0xff) << 8) + (crc >> 8))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    newDlg = Crc16_dlg()
    newDlg.setupUi()
    newDlg.show()
    sys.exit(app.exec_())
