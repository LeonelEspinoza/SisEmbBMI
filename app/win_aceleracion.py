# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'grafico_aceleracion.ui'
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
        fig, self.axis = plt.subplots(figsize=(3,2),dpi=100)
        super().__init__(fig)
        self.setParent(parent)

        t = receiver.time_array

        print(receiver.ax)

        self.lineAx, = self.axis.plot(t,receiver.ax, color='r')
        self.lineAy, = self.axis.plot(t,receiver.ay, color='g')
        self.lineAz, = self.axis.plot(t,receiver.az, color='b')

        self.axis.set(xlabel='tiempo', ylabel='aceleración', title='Medias Acelerometro')
        self.axis.grid()


class Ui_GraphAcceleration(QWidget):
    def setupUi(self, GraphAcceleration):
        GraphAcceleration.setObjectName("GraphAcceleration")
        GraphAcceleration.resize(820, 600)
        self.centralwidget = QtWidgets.QWidget(GraphAcceleration)
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 820, 600))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.chart = Canvas(self)
        self.horizontalLayout.addWidget(self.chart)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.horizontalLayoutWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(743, 170, 77, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setBaseSize(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox.setChecked(True)
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox_2.setChecked(True)
        self.checkBox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox_3.setChecked(True)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        GraphAcceleration.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(GraphAcceleration)
        self.statusbar.setObjectName("statusbar")
        GraphAcceleration.setStatusBar(self.statusbar)

        self.retranslateUi(GraphAcceleration)
        QtCore.QMetaObject.connectSlotsByName(GraphAcceleration)

        self.pushButton.clicked.connect(self.volverMenu)
        self.pushButton.clicked.connect(GraphAcceleration.close)

        self.checkBox.stateChanged.connect(self.checkbox_ax)
        self.checkBox_2.stateChanged.connect(self.checkbox_ay)
        self.checkBox_3.stateChanged.connect(self.checkbox_az)

    def checkbox_ax(self, state):
        if state:
            print(receiver.ax)
            self.chart.lineAx, = self.chart.axis.plot(receiver.ax, color='r')
            self.chart.draw()
        else:
            self.chart.lineAx.remove()
            self.chart.draw()
    
    def checkbox_ay(self, state):
        if state:
            self.chart.lineAy, = self.chart.axis.plot(receiver.ax, color='g')
            self.chart.draw()
        else:
            self.chart.lineAy.remove()
            self.chart.draw()
            
    def checkbox_az(self, state):
        if state:
            self.chart.lineAz, = self.chart.axis.plot(receiver.ax, color='b')
            self.chart.draw()
        else:
            self.chart.lineAz.remove()
            self.chart.draw()
    
    def volverMenu(self):
        from main_app import Ui_MainWindow
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window2)
        self.window2.show()

    def retranslateUi(self, GraphAcceleration):
        _translate = QtCore.QCoreApplication.translate
        GraphAcceleration.setWindowTitle(_translate("GraphAcceleration", "Gráfico Aceleración"))
        self.checkBox.setText(_translate("GraphAcceleration", "eje X"))
        self.checkBox_2.setText(_translate("GraphAcceleration", "eje Y"))
        self.checkBox_3.setText(_translate("GraphAcceleration", "eje Z"))
        self.pushButton.setText(_translate("GraphAcceleration", "Volver"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GraphAcceleration = QtWidgets.QMainWindow()
    ui = Ui_GraphAcceleration()
    ui.setupUi(GraphAcceleration)
    GraphAcceleration.show()
    sys.exit(app.exec_())