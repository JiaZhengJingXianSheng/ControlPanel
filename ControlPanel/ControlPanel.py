#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/21 13:47
# @Author : LYZ

from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QDateTime, QTimer, SIGNAL
import sys
import Adafruit_DHT

import threading
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
channel = 38
GPIO.setup(channel,GPIO.OUT,initial=0)
channel2 = 36
GPIO.setup(channel2,GPIO.OUT,initial=0)
        
class Stats:

    def __init__(self):

        self.ui = QUiLoader().load('ui/control.ui')
        
        self.timer = QTimer()
        self.humidity, self.temperature = Adafruit_DHT.read_retry(11,21)
        self.timer.connect(self.timer, SIGNAL("timeout()"), self.showInfo)
        self.ui.temLcd.display(self.temperature)
        self.ui.humLcd.display(self.humidity)
        self.timer.start(1000)

        #self.t1 = threading.Thread(target=self.getInfo)
        #self.t1.start()
        self.ui.openFanButton.clicked.connect(self.openFan)
        self.ui.closeFanButton.clicked.connect(self.closeFan)
    
        self.ui.openLightButton.clicked.connect(self.openLight)
        self.ui.closeLightButton.clicked.connect(self.closeLight)
        
    def openLight(self):
        GPIO.output(channel2,1)

    def closeLight(self):
        GPIO.output(channel2,0)

    def openFan(self):
        GPIO.output(channel,1)

    def closeFan(slef):
        GPIO.output(channel,0)

    def showInfo(self):
        self.humidity, self.temperature = Adafruit_DHT.read_retry(11,21)
        self.ui.temLcd.display(self.temperature)
        self.ui.humLcd.display(self.humidity)


    def getInfo(self):
        while(True):
            self.humidity, self.temperature = Adafruit_DHT.read_retry(11,21)
            self.timer = QTimer(self)
            self.connect(timer, SIGNAL("timeout()"), self.updtTime)
            self.ui.temLcd.display(self.temperature)
            self.ui.humLcd.display(self.humidity)
            self.timer.start(1000)


if __name__=='__main__':
    app = QApplication([])
    stats = Stats()
    stats.ui.show()
    app.exec_()
    GPIO.cleanup()
