import os
from ast import Index
import enum
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from cffi.setuptools_ext import execfile
from trade_bot_designer import *
import requests
import pandas as pd
from ta.trend import EMAIndicator
import websocket, json, pprint, numpy, talib
import threading
import subprocess
import pid
import signal


uygulama = QApplication(sys.argv)
pencere = QMainWindow()
ui = Ui_bgwidget()
ui.setupUi(pencere)
pencere.show()


def start_bot():
    ui.pushButton_3.hide()

    os.system('python main.py')


def buton_fonksiyon():
    th = threading.Thread(target=start_bot)
    th.start()


def stop_bot():
    b = pid.Pid()
    c = b.id_goruntule()
    os.kill(c, signal.SIGTERM)


ui.pushButton_3.clicked.connect(buton_fonksiyon)
ui.pushButton_2.clicked.connect(stop_bot)


sys.exit(uygulama.exec_())
