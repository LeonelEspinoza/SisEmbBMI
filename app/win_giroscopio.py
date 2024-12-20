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

        self.lineGx, = self.axis.plot(t,receiver.gx, color='r')
        self.lineGy, = self.axis.plot(t,receiver.gy, color='g')
        self.lineGz, = self.axis.plot(t,receiver.gz, color='b')

        self.axis.set(xlabel='tiempo (s)', ylabel='angulo', title='Medidas Giroscopio')
        self.axis.grid()

class Ui_GraphGyroscope(QWidget):
    def setupUi(self, GraphGyroscope):
        GraphGyroscope.setObjectName("GraphGyroscope")
        GraphGyroscope.resize(820, 600)
        self.centralwidget = QtWidgets.QWidget(GraphGyroscope)
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 820, 600))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.chart = Canvas(self)
        self.horizontalLayout.addWidget(self.chart)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
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
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout.addWidget(self.checkBox_3)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        GraphGyroscope.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(GraphGyroscope)
        self.statusbar.setObjectName("statusbar")
        GraphGyroscope.setStatusBar(self.statusbar)

        self.retranslateUi(GraphGyroscope)
        QtCore.QMetaObject.connectSlotsByName(GraphGyroscope)

        self.pushButton.clicked.connect(self.volverMenu)
        self.pushButton.clicked.connect(GraphGyroscope.close)

        self.checkBox.setChecked(True)
        self.checkBox_2.setChecked(True)
        self.checkBox_3.setChecked(True)

        self.checkBox.stateChanged.connect(self.checkbox_gx)
        self.checkBox_2.stateChanged.connect(self.checkbox_gy)
        self.checkBox_3.stateChanged.connect(self.checkbox_gz)

    def checkbox_gx(self, state):
        if state:
            self.chart.lineGx, = self.chart.axis.plot(receiver.gx, color='r')
            self.chart.draw()
        else:
            self.chart.lineGx.remove()
            self.chart.draw()
    
    def checkbox_gy(self, state):
        if state:
            self.chart.lineGy, = self.chart.axis.plot(receiver.gy, color='g')
            self.chart.draw()
        else:
            self.chart.lineGy.remove()
            self.chart.draw()
            
    def checkbox_gz(self, state):
        if state:
            self.chart.lineGz, = self.chart.axis.plot(receiver.gz, color='b')
            self.chart.draw()
        else:
            self.chart.lineGz.remove()
            self.chart.draw()
    
    def volverMenu(self):
        from main_app import Ui_MainWindow
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window2)
        self.window2.show()

    def retranslateUi(self, GraphGyroscope):
        _translate = QtCore.QCoreApplication.translate
        GraphGyroscope.setWindowTitle(_translate("GraphGyroscope", "Gráfico Giroscopio"))
        self.checkBox.setText(_translate("GraphGyroscope", "eje X"))
        self.checkBox_2.setText(_translate("GraphGyroscope", "eje Y"))
        self.checkBox_3.setText(_translate("GraphGyroscope", "eje Z"))
        self.pushButton.setText(_translate("GraphGyroscope", "Volver"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GraphGyroscope = QtWidgets.QMainWindow()
    ui = Ui_GraphGyroscope()
    ui.setupUi(GraphGyroscope)
    GraphGyroscope.show()
    sys.exit(app.exec_())
