from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
import sys

import test


class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        self.initUI(MainWindow)
        #self.botonCambiar = QtWidgets.QPushButton("Cambiar",self)

        
        #self.line_edit = QtWidgets.QLineEdit(self)
    
    def initUI(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 600, 450))
        self.stackedWidget.setObjectName("stackedWidget")

        self.page1 = QWidget()
        self.page1.setObjectName("page_1")
        self.gridLayoutWidget = QWidget(self.page1)

        self.gridLayoutWidget.setGeometry(QtCore.QRect(170, 150, 271, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        #botones page_1
        self.botonSolicitarVentana = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.botonSolicitarVentana.setObjectName("Solicitar ventana de datos")
        self.gridLayout.addWidget(self.botonSolicitarVentana, 0, 0)

        self.botonCambiarVentana = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.botonCambiarVentana.setObjectName("Cambiar tamaño de la ventana")
        self.gridLayout.addWidget(self.botonCambiarVentana, 0, 1)

        self.botonCerrarConexion = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.botonCerrarConexion.setObjectName("Cerrar conexion")
        self.gridLayout.addWidget(self.botonCerrarConexion, 1, 0)

        self.botonGraficos = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.botonGraficos.setObjectName("Ver gráficos")
        self.gridLayout.addWidget(self.botonGraficos, 1, 1)

        self.stackedWidget.addWidget(self.page1)

    
        #self.botonSolicitarVentana.clicked.connect(test.test_print)
        #self.botonCambiarVentana.clicked.connect(self.cambiarVentana)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.botonSolicitarVentana.setText(_translate("MainWindow", "Solicitar ventana"))
        self.botonCambiarVentana.setText(_translate("MainWindow","Cambiar tamaño ventana"))
        self.botonCerrarConexion.setText(_translate("MainWindow","Cerrar conexion"))
        self.botonGraficos.setText(_translate("MainWindow","Ver gráficos"))

    def ventana_page2(self):
        pass
    
    def enviarCambio(self):
        #se extrae el texto introducido
        text = self.line_edit.text()
        print(f"Se cambio la configuracion a {text}")
        text = int(text)
        #funcion de otra parte que cambie el valor de la ventana

        #volemos al menu
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show() 
    sys.exit(app.exec_())