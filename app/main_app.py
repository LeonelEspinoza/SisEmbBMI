# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from cambiar_menu import Ui_ChangeSizeWindow
from win_aceleracion import Ui_GraphAcceleration
from win_giroscopio import Ui_GraphGyroscope
from win_rms import Ui_RMS
from win_fft import Ui_FFT

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(300, 120, 181, 431))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 15, 0, 15)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.verticalLayout.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.verticalLayout.addWidget(self.pushButton_7)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #agregar funciones a los botones
        self.pushButton_2.clicked.connect(self.menuCambiarTamano)
        self.pushButton_2.clicked.connect(MainWindow.close)

        self.pushButton_3.clicked.connect(self.graficoAceleracion)
        self.pushButton_3.clicked.connect(MainWindow.close)

        self.pushButton_5.clicked.connect(self.graficoGiroscopio)
        self.pushButton_5.clicked.connect(MainWindow.close)

        self.pushButton_6.clicked.connect(self.graficoRMS)
        self.pushButton_6.clicked.connect(MainWindow.close)

        self.pushButton_7.clicked.connect(self.graficoFFT)
        self.pushButton_7.clicked.connect(MainWindow.close)

        self.pushButton.clicked.connect(self.pedirVentana)

        self.pushButton_4.clicked.connect(self.cerrarConexion)
        self.pushButton_4.clicked.connect(MainWindow.close)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def menuCambiarTamano(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_ChangeSizeWindow()
        self.ui.setupUi(self.window2)
        self.window2.show()
    
    def graficoAceleracion(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_GraphAcceleration()
        self.ui.setupUi(self.window2)
        self.window2.show()
    
    def graficoGiroscopio(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_GraphGyroscope()
        self.ui.setupUi(self.window2)
        self.window2.show()
    
    def graficoRMS(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_RMS()
        self.ui.setupUi(self.window2)
        self.window2.show()
    
    def graficoFFT(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_FFT()
        self.ui.setupUi(self.window2)
        self.window2.show()
    
    def pedirVentana(slef):
        print("pidiendo ventana")
    
    def cerrarConexion(self):
        print("cerrando conexion")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Menu Principal"))
        self.pushButton.setText(_translate("MainWindow", "Soicitar ventana"))
        self.pushButton_3.setText(_translate("MainWindow", "Gráfico aceleración "))
        self.pushButton_5.setText(_translate("MainWindow", "Gráfico giroscopio"))
        self.pushButton_6.setText(_translate("MainWindow", "Gráfico RMS"))
        self.pushButton_7.setText(_translate("MainWindow", "Gráfico FFT"))
        self.pushButton_2.setText(_translate("MainWindow", "Cambiar tamaño ventana"))
        self.pushButton_4.setText(_translate("MainWindow", "Cerrar conexión"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())