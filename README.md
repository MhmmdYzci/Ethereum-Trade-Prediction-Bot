# Ethereum-Trade-Prediction-Bot
This bot predicts buy or sell for ethereum, a virtual currency.
In order to use this bot, you must contact the developers and be taken to the telegram channel.
After importing the necessary libraries, you can run the trade_bot_start_py file and use the bot.

Required Libraries:
from PyQt5 import QtCore, QtWidgets
import sys
from PyQt5.QtWidgets import *
import threading
import os
import requests
import pandas as pd
from ta.trend import EMAIndicator
import websocket, json, numpy, talib

If you get an error in the talib installation, follow this directive:
https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib
From this site, download the appropriate file for your python version and computer and put it in the folder where the project is.
You can find out the python version you are using by typing python --version into the terminal of the IDE you are using.
After you put the downloaded file in the project folder, you need to type 'pip install -the name of the downloaded file with its extension-' in the terminal.
If you get errors from other libraries, simply uninstall and reinstall.
