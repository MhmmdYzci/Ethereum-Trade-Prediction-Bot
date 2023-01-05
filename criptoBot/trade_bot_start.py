
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
import threading
import tradeBot



class Ui_bgwidget(object):
    def setupUi(self, bgwidget):
        bgwidget.setObjectName("bgwidget")
        bgwidget.setEnabled(True)
        bgwidget.resize(890, 534)
        bgwidget.setStyleSheet(
            "QWidget#bgwidget{background-color: qlineargradient(spread:pad, x1:0.084, y1:0.0514545, x2:0.979, y2:0.949, stop:0.0209424 rgba(0, 170, 255, 255), stop:0.994764 rgba(0, 255, 127, 255));}")
        self.pushButton_2 = QtWidgets.QPushButton(bgwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 360, 101, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(bgwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 561, 71))
        self.label.setStyleSheet("font: 36pt \"MS Shell Dlg 2\"; color:rgb(255, 255, 255)")
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(bgwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(600, 320, 101, 31))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(bgwidget)
        QtCore.QMetaObject.connectSlotsByName(bgwidget)
        self.pushButton_3.clicked.connect(self.buton_fonksiyon)
        self.pushButton_2.clicked.connect(self.close_bot)
        uygulama.aboutToQuit.connect(self.closeEvent)

    def retranslateUi(self, bgwidget):
        _translate = QtCore.QCoreApplication.translate
        bgwidget.setWindowTitle(_translate("bgwidget", "Trade Bot"))
        self.pushButton_2.setText(_translate("bgwidget", "Stop Bot"))
        self.label.setText(_translate("bgwidget", "Ethereum Trade Bot"))
        self.pushButton_3.setText(_translate("bgwidget", "Start Bot"))


    def start_bot(self):
        self.pushButton_3.hide()
        tradeBot.start()

    def buton_fonksiyon(self):
        th = threading.Thread(target=self.start_bot)
        th.start()
    def close_bot(self):
        tradeBot.on_close(tradeBot.ws)
        self.pushButton_3.show()
    def closeEvent(self):
        tradeBot.on_close(tradeBot.ws)

        sys.exit(0)
if __name__ == "__main__":

    uygulama = QApplication(sys.argv)
    pencere = QMainWindow()
    ui = Ui_bgwidget()
    ui.setupUi(pencere)
    pencere.show()
    sys.exit(uygulama.exec_())