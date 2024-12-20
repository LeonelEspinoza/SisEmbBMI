# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rms.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget
import numpy as np
import receiver

class Canvas(FigureCanvas):
    def __init__(self,parent):
        fig, self.axis = plt.subplots(ncols=2, figsize=(3,2),dpi=100)
        super().__init__(fig)
        self.setParent(parent)

        rms = ["rms_gx","rms_gy","rms_gz","rms_ax","rms_ay","rms_az"]
        rmsg = ["rms_gx","rms_gy","rms_gz"]
        rmsa = ["rms_ax","rms_ay","rms_az"]
        count = receiver.rms_a_g   

        bar_labelg = ["giroscopio","_giroscopio","_giroscopio"]
        bar_labela = ["aceleracion","_aceleracion","_aceleracion"]
        
        self.axis[0].scatter(x=rmsg,y=count[0:3],label=bar_labelg)
        self.axis[1].scatter(x=rmsa,y=count[3:6],label=bar_labela)

        self.axis[0].set(xlabel='RMS_G', ylabel='valores', title='Medicion de RMS Giroscopio')
        self.axis[1].set(xlabel='RMS_A', ylabel='valores', title='Medicion de RMS Aceleración')

        #self.axis.plot(t,s)
        #self.axis.set(xlabel='time (s)', ylabel='voltage (mv)', title='nada')
        #self.axis.grid()


class Ui_RMS(QWidget):
    def setupUi(self, MainWindow):
        self.array = []

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(820, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 820, 600))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        chart = Canvas(self)
        self.horizontalLayout.addWidget(chart)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        #original
        #self.verticalLayoutWidget.setGeometry(QtCore.QRect(743, 170, 77, 151))
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(379, 495, 77, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)

        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.volverMenu)
        self.pushButton.clicked.connect(MainWindow.close)

    
    def volverMenu(self):
        from main_app import Ui_MainWindow
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window2)
        self.window2.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gráfico Giroscopio"))
        self.pushButton.setText(_translate("MainWindow", "Volver"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_RMS()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

