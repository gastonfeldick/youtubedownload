# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(800, 600))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.encabezado = QtWidgets.QFrame(self.frame)
        self.encabezado.setMaximumSize(QtCore.QSize(1920, 40))
        self.encabezado.setStyleSheet("background:rgb(0, 0, 0);COLOR:(170, 255, 255);")
        self.encabezado.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.encabezado.setFrameShadow(QtWidgets.QFrame.Raised)
        self.encabezado.setObjectName("encabezado")
        self.repositorio = QtWidgets.QCommandLinkButton(self.encabezado)
        self.repositorio.setGeometry(QtCore.QRect(10, 0, 200, 30))
        self.repositorio.setMaximumSize(QtCore.QSize(200, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.repositorio.setFont(font)
        self.repositorio.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.repositorio.setStyleSheet("QPushButton#repositorio{\n"
                                       "    background-color:rgb(0, 0, 0);\n"
                                       "    color:rgb(255, 0, 0);\n"
                                       "}\n"
                                       "QPushButton:hover#repositorio{\n"
                                       "    background-color:rgb(85, 255, 255);\n"
                                       "}\n"
                                       "")
        self.repositorio.setObjectName("repositorio")
        self.verticalLayout_2.addWidget(self.encabezado)
        self.Descarga = QtWidgets.QFrame(self.frame)
        self.Descarga.setMaximumSize(QtCore.QSize(1920, 400))
        self.Descarga.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Descarga.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Descarga.setObjectName("Descarga")
        self.frameDescarga = QtWidgets.QWidget(self.Descarga)
        self.frameDescarga.setGeometry(QtCore.QRect(120, 130, 551, 121))
        self.frameDescarga.setObjectName("frameDescarga")
        self.barra = QtWidgets.QProgressBar(self.frameDescarga)
        self.barra.setGeometry(QtCore.QRect(10, 60, 531, 31))
        self.barra.setProperty("value", 0)
        self.barra.setObjectName("barra")
        self.estado = QtWidgets.QLabel(self.frameDescarga)
        self.estado.setGeometry(QtCore.QRect(210, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.estado.setFont(font)
        self.estado.setObjectName("estado")
        self.label = QtWidgets.QLabel(self.Descarga)
        self.label.setGeometry(QtCore.QRect(330, 40, 100, 80))
        self.label.setMaximumSize(QtCore.QSize(100, 80))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("imagenes/R (1).png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.Descarga)
        self.label_4.setGeometry(QtCore.QRect(290, 10, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.Descarga)
        self.cuerpo = QtWidgets.QFrame(self.frame)
        self.cuerpo.setMaximumSize(QtCore.QSize(1920, 300))
        self.cuerpo.setStyleSheet("background:rgb(221, 221, 221)")
        self.cuerpo.setInputMethodHints(QtCore.Qt.ImhDate)
        self.cuerpo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cuerpo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cuerpo.setObjectName("cuerpo")
        self.formato = QtWidgets.QComboBox(self.cuerpo)
        self.formato.setGeometry(QtCore.QRect(150, 10, 111, 21))
        self.formato.setStyleSheet("BACKGROUND:rgb(255, 255, 255)")
        self.formato.setObjectName("formato")
        self.formato.addItem("")
        self.formato.addItem("")
        self.label_2 = QtWidgets.QLabel(self.cuerpo)
        self.label_2.setGeometry(QtCore.QRect(60, 40, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.url = QtWidgets.QLineEdit(self.cuerpo)
        self.url.setGeometry(QtCore.QRect(150, 50, 451, 21))
        self.url.setStyleSheet("BACKGROUND:rgb(255, 255, 255)")
        self.url.setObjectName("url")
        self.label_3 = QtWidgets.QLabel(self.cuerpo)
        self.label_3.setGeometry(QtCore.QRect(60, 0, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.descargar = QtWidgets.QPushButton(self.cuerpo)
        self.descargar.setGeometry(QtCore.QRect(300, 220, 161, 50))
        self.descargar.setMaximumSize(QtCore.QSize(200, 50))
        self.descargar.setStyleSheet("\n"
                                     "QPushButton:hover#descargar{\n"
                                     "    background-color:rgb(255, 0, 0)\n"
                                     "}")
        self.descargar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imagenes/DOWNLOAD.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.descargar.setIcon(icon)
        self.descargar.setIconSize(QtCore.QSize(150, 120))
        self.descargar.setObjectName("descargar")
        self.buscar = QtWidgets.QPushButton(self.cuerpo)
        self.buscar.setGeometry(QtCore.QRect(150, 90, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.buscar.setFont(font)
        self.buscar.setStyleSheet("QPushButton#buscar{\n"
                                  "    background-color:rgb(255, 0, 0);\n"
                                  "    color:rgb(255, 255, 255);\n"
                                  "}\n"
                                  "QPushButton:hover#buscar{\n"
                                  "background-color:rgb(255, 255, 255);\n"
                                  "    color:rgb(255, 0, 0);\n"
                                  "\n"
                                  "}")
        self.buscar.setObjectName("buscar")
        self.labelTitulo = QtWidgets.QLabel(self.cuerpo)
        self.labelTitulo.setGeometry(QtCore.QRect(250, 160, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setObjectName("labelTitulo")
        self.titulo = QtWidgets.QLabel(self.cuerpo)
        self.titulo.setGeometry(QtCore.QRect(330, 160, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.titulo.setFont(font)
        self.titulo.setText("")
        self.titulo.setObjectName("titulo")
        self.label_3.raise_()
        self.formato.raise_()
        self.label_2.raise_()
        self.url.raise_()
        self.descargar.raise_()
        self.buscar.raise_()
        self.labelTitulo.raise_()
        self.titulo.raise_()
        self.verticalLayout_2.addWidget(self.cuerpo)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.repositorio.setText(_translate("MainWindow", "Repositorio: gitlab"))
        self.estado.setText(_translate("MainWindow", "Descargando"))
        self.label_4.setText(_translate("MainWindow", "YOUTUBE DOWNLOAD"))
        self.formato.setItemText(0, _translate("MainWindow", "MP4"))
        self.formato.setItemText(1, _translate("MainWindow", "MP3"))
        self.label_2.setText(_translate("MainWindow", "URL"))
        self.label_3.setText(_translate("MainWindow", "Formato"))
        self.buscar.setText(_translate("MainWindow", "BUSCAR"))
        self.labelTitulo.setText(_translate("MainWindow", "Titulo"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
