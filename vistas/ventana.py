import sys
import os
myDir=os.getcwd()
sys.path.append(myDir)

from vistas.interface import *
from pytube import YouTube
from getpass import getuser
from controladores.controllers import buscar,descargar,abrirNavegador




def inicio():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.frameDescarga.hide()
    ui.descargar.hide()
    ui.labelTitulo.hide()
    ui.titulo.hide()
    ui.repositorio.clicked.connect(abrirNavegador)
    MainWindow.setWindowTitle("Youtube Download")
    ui.buscar.clicked.connect(lambda:buscar(ui))
    ui.descargar.clicked.connect(lambda:descargar(ui))
    MainWindow.show()
    sys.exit(app.exec_())
