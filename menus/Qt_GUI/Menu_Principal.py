# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Proyecto_QT/Menu_Principal.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TowerDefenseMainMenu(object):
    def setupUi(self, TowerDefenseMainMenu):
        TowerDefenseMainMenu.setObjectName("TowerDefenseMainMenu")
        TowerDefenseMainMenu.resize(580, 520)
        self.centralwidget = QtWidgets.QWidget(TowerDefenseMainMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.fondoprincipal = QtWidgets.QLabel(self.centralwidget)
        self.fondoprincipal.setGeometry(QtCore.QRect(-4, -8, 581, 481))
        self.fondoprincipal.setStyleSheet("background-image: url(:/images/main_background.jpg);")
        self.fondoprincipal.setText("")
        self.fondoprincipal.setObjectName("fondoprincipal")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(340, 360, 82, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ajustes_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setBold(True)
        font.setWeight(75)
        self.ajustes_button.setFont(font)
        self.ajustes_button.setObjectName("ajustes_button")
        self.horizontalLayout_2.addWidget(self.ajustes_button)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(430, 360, 82, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.salir_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setBold(True)
        font.setWeight(75)
        self.salir_button.setFont(font)
        self.salir_button.setObjectName("salir_button")
        self.horizontalLayout_4.addWidget(self.salir_button)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(340, 330, 171, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.jugar_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setBold(True)
        font.setWeight(75)
        self.jugar_button.setFont(font)
        self.jugar_button.setObjectName("jugar_button")
        self.horizontalLayout_5.addWidget(self.jugar_button)
        self.tituloprincipal = QtWidgets.QLabel(self.centralwidget)
        self.tituloprincipal.setGeometry(QtCore.QRect(110, 40, 421, 71))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(28)
        self.tituloprincipal.setFont(font)
        self.tituloprincipal.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tituloprincipal.setLineWidth(1)
        self.tituloprincipal.setTextFormat(QtCore.Qt.PlainText)
        self.tituloprincipal.setObjectName("tituloprincipal")
        self.logo_espadas = QtWidgets.QLabel(self.centralwidget)
        self.logo_espadas.setGeometry(QtCore.QRect(230, 10, 131, 131))
        self.logo_espadas.setStyleSheet("background-image: url(:/images/swords.png);")
        self.logo_espadas.setText("")
        self.logo_espadas.setObjectName("logo_espadas")
        self.fondoprincipal.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.horizontalLayoutWidget_4.raise_()
        self.horizontalLayoutWidget_5.raise_()
        self.logo_espadas.raise_()
        self.tituloprincipal.raise_()
        TowerDefenseMainMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TowerDefenseMainMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 580, 20))
        self.menubar.setObjectName("menubar")
        self.menuTOWER_DEFENSE_GAME = QtWidgets.QMenu(self.menubar)
        self.menuTOWER_DEFENSE_GAME.setObjectName("menuTOWER_DEFENSE_GAME")
        TowerDefenseMainMenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TowerDefenseMainMenu)
        self.statusbar.setObjectName("statusbar")
        TowerDefenseMainMenu.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuTOWER_DEFENSE_GAME.menuAction())

        self.retranslateUi(TowerDefenseMainMenu)
        QtCore.QMetaObject.connectSlotsByName(TowerDefenseMainMenu)

    def retranslateUi(self, TowerDefenseMainMenu):
        _translate = QtCore.QCoreApplication.translate
        TowerDefenseMainMenu.setWindowTitle(_translate("TowerDefenseMainMenu", "MainWindow"))
        self.ajustes_button.setText(_translate("TowerDefenseMainMenu", "AJUSTES"))
        self.salir_button.setText(_translate("TowerDefenseMainMenu", "SALIR"))
        self.jugar_button.setText(_translate("TowerDefenseMainMenu", "JUGAR"))
        self.tituloprincipal.setText(_translate("TowerDefenseMainMenu", "TOWER              DEFENSE"))
        self.menuTOWER_DEFENSE_GAME.setTitle(_translate("TowerDefenseMainMenu", " "))
import Resource_File_General_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TowerDefenseMainMenu = QtWidgets.QMainWindow()
    ui = Ui_TowerDefenseMainMenu()
    ui.setupUi(TowerDefenseMainMenu)
    TowerDefenseMainMenu.show()
    sys.exit(app.exec_())