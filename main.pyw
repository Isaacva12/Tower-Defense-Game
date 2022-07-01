# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtWidgets import (QApplication, QDialog, QFileDialog, QInputDialog, QMessageBox)

#Cargar formulario *.ui
form_class = uic.loadUiType("Menuprincipal.ui")[0]

#crear clase MyWindowClass
class MyWindowClass(QMainWindow, form_class):
    MESSAGE = """Prueba de menús con capas de formulario y \n
    barra de botones con iconos y compilacion con recursos\n
    version 1.01 abril 2019"""

    def __init__(self, parent=None):
        QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.pantallas.setCurrentIndex(-1)  # Activamos la pantalla 1

    def abrir(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,
                                                  "Abrir Archivo", '',
                                                  "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            QMessageBox.information(self,'Abrir archivo',fileName)
    def guardar(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Guardar Archivo",'',
                                                  "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            QMessageBox.information(self,'Gurdar archivo',fileName)
    def Acerca(self):
        QMessageBox.information(self,'Informatica Bits',self.MESSAGE)

    def activap2(self):
        self.pantallas.setCurrentIndex(1) # cambiamos a la pantalla 2
    def activap1(self):
        self.pantallas.setCurrentIndex(0) # cambiamos a la pantalla 1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MyWindow = MyWindowClass(None)
    MyWindow.show()
    app.exec_()



