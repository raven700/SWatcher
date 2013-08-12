# -*- coding: utf-8 -*-

# #############################################################################
# Copyright (C) 2013  raven700
#
# https://github.com/raven700/SWatcher
#
# This file is part of SWatcher.
#
# SWatcher is a tool for watching and managing Windows certain services.
#
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# #############################################################################

import sys
from PyQt4 import QtGui
import win32serviceutil
import threading
import time


sTitle = "SWatcher"
sStart = "Uruchom"
sStop = "Zatrzymaj"
sStartAll = "Uruchom wszystkie"
sStopAll = "Zatrzymaj wszystkie"
sStarted = "Uruchomiona"
sStopped = "Zatrzymana"
sService1 = "Spooler"
sService2 = "uvnc_service"
sComputer = "localhost"

cStyleGreen = 'QCheckBox {color: green}'
cStyleRed = 'QCheckBox {color: red}'


class Services(QtGui.QWidget):
    def __init__(self):
        super(Services, self).__init__()

        self.initUI()

    def initUI(self):
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        # --Wiersz 1--
        self.l1 = QtGui.QLabel(sService1, self)
        self.gridLayout.addWidget(self.l1, 0, 0, 1, 1)

        self.bRun1 = QtGui.QPushButton(self)
        self.gridLayout.addWidget(self.bRun1, 0, 1, 1, 1)
        self.bRun1.clicked.connect(self.bRun1Click)

        self.cStatus1 = QtGui.QCheckBox(self)
        self.cStatus1.setEnabled(False)
        self.gridLayout.addWidget(self.cStatus1, 0, 2, 1, 1)
        # --Wiersz 2--
        self.l2 = QtGui.QLabel(sService2, self)
        self.gridLayout.addWidget(self.l2, 1, 0, 1, 1)

        self.bRun2 = QtGui.QPushButton(self)
        self.gridLayout.addWidget(self.bRun2, 1, 1, 1, 1)
        self.bRun2.clicked.connect(self.bRun2Click)

        self.cStatus2 = QtGui.QCheckBox(self)
        self.cStatus2.setEnabled(False)
        self.gridLayout.addWidget(self.cStatus2, 1, 2, 1, 1)
        # --Wiersz 3--
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        # --Wiersz 4--
        self.bOnAll = QtGui.QPushButton(sStartAll, self)
        self.gridLayout.addWidget(self.bOnAll, 4, 0, 1, 1)
        self.bOnAll.clicked.connect(self.bOnAllClick)

        self.bOffAll = QtGui.QPushButton(sStopAll, self)
        self.gridLayout.addWidget(self.bOffAll, 4, 1, 1, 1)
        self.bOffAll.clicked.connect(self.bOffAllClick)    

        self.horizontalLayout_2.addLayout(self.gridLayout)


        self.setGeometry(300, 100, 0, 0)
        self.setWindowTitle(sTitle)
        self.show()


    def bRun1Click(self):
        if win32serviceutil.QueryServiceStatus(sService1, sComputer)[1] == 4:
            win32serviceutil.StopService(sService1, sComputer)
        else:
            win32serviceutil.StartService(sService1, sComputer)

    def bRun2Click(self):
        if win32serviceutil.QueryServiceStatus(sService2, sComputer)[1] == 4:
            win32serviceutil.StopService(sService2, sComputer)
        else:
            win32serviceutil.StartService(sService2, sComputer)

    def bOnAllClick(self):
        if win32serviceutil.QueryServiceStatus(sService1, sComputer)[1] != 4:
            win32serviceutil.StartService(sService1, sComputer)

        if win32serviceutil.QueryServiceStatus(sService2, sComputer)[1] != 4:
            win32serviceutil.StartService(sService2, sComputer)

    def bOffAllClick(self):
        if win32serviceutil.QueryServiceStatus(sService1, sComputer)[1] == 4:
            win32serviceutil.StopService(sService1, sComputer)

        if win32serviceutil.QueryServiceStatus(sService2, sComputer)[1] == 4:
            win32serviceutil.StopService(sService2, sComputer)

    def serviceTest(self):
        while True:
            if win32serviceutil.QueryServiceStatus(sService1, sComputer)[1] == 4:
                self.bRun1.setText(sStop)
                self.cStatus1.setText(sStarted)
                self.cStatus1.setChecked(True)
                self.cStatus1.setStyleSheet(cStyleGreen)
            else:
                self.bRun1.setText(sStart)
                self.cStatus1.setText(sStopped)
                self.cStatus1.setChecked(False)
                self.cStatus1.setStyleSheet(cStyleRed)

            if win32serviceutil.QueryServiceStatus(sService2, sComputer)[1] == 4:
                self.bRun2.setText(sStop)
                self.cStatus2.setText(sStarted)
                self.cStatus2.setChecked(True)
                self.cStatus2.setStyleSheet(cStyleGreen)
            else:
                self.bRun2.setText(sStart)
                self.cStatus2.setText(sStopped)
                self.cStatus2.setChecked(False)
                self.cStatus2.setStyleSheet(cStyleRed)

            time.sleep(1)

    def watek(self):
        t = threading.Thread(target=self.serviceTest)
        t.daemon = True
        t.start()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Services()
    ex.watek()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
