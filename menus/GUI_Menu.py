from PyQt5 import QtCore, QtGui, QtWidgets
from games.game1 import Juego
from .Qt_GUI.Resource_File_General_rc import *



class Ui_TowerDefenseMainMenu(object):

    def __init__(self):

        self.speed = "Media"
        self.difficulty = "Media"

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

        #Button action

        self.salir_button.clicked.connect(lambda:self.closescr(TowerDefenseMainMenu))
        self.ajustes_button.clicked.connect(self.menu_ajustes_partida)
        self.jugar_button.clicked.connect(lambda:self.closescr(TowerDefenseMainMenu))
        self.jugar_button.clicked.connect(self.run_game)
    def retranslateUi(self, TowerDefenseMainMenu):
        _translate = QtCore.QCoreApplication.translate
        TowerDefenseMainMenu.setWindowTitle(_translate("TowerDefenseMainMenu", "MainWindow"))
        self.ajustes_button.setText(_translate("TowerDefenseMainMenu", "AJUSTES"))
        self.salir_button.setText(_translate("TowerDefenseMainMenu", "SALIR"))
        self.jugar_button.setText(_translate("TowerDefenseMainMenu", "JUGAR"))
        self.tituloprincipal.setText(_translate("TowerDefenseMainMenu", "TOWER              DEFENSE"))
        self.menuTOWER_DEFENSE_GAME.setTitle(_translate("TowerDefenseMainMenu", " "))

    def run_game(self):
        self.ui = Ui_TowerDefenseMainMenu()
        j = Juego(self.ui.speed, self.ui.difficulty)
        j.run()

    def closescr (self, Form):
        Form.hide()

    def menu_ajustes_partida (self):
        self.menu_ajustes_partida = QtWidgets.QMainWindow()
        self.ui = Ui_TowerDefenseAjustesPartida()
        self.ui.setupUi(self.menu_ajustes_partida)
        self.menu_ajustes_partida.show()




class Ui_TowerDefenseAjustesPartida(object):

    def __init__(self):
        Ui_TowerDefenseMainMenu.__init__(self)

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(580, 520)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fondoajustes = QtWidgets.QLabel(self.centralwidget)
        self.fondoajustes.setGeometry(QtCore.QRect(0, 0, 581, 481))
        self.fondoajustes.setStyleSheet("background-image: url(:/images/second_background.jpg);")
        self.fondoajustes.setText("")
        self.fondoajustes.setObjectName("fondoajustes")
        self.tituloajustes = QtWidgets.QLabel(self.centralwidget)
        self.tituloajustes.setGeometry(QtCore.QRect(180, 30, 270, 71))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(28)
        self.tituloajustes.setFont(font)
        self.tituloajustes.setStyleSheet("")
        self.tituloajustes.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tituloajustes.setLineWidth(1)
        self.tituloajustes.setTextFormat(QtCore.Qt.PlainText)
        self.tituloajustes.setObjectName("tituloajustes")
        self.label_pantalla = QtWidgets.QLabel(self.centralwidget)
        self.label_pantalla.setGeometry(QtCore.QRect(210, 220, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_pantalla.setFont(font)
        self.label_pantalla.setObjectName("label_pantalla")
        self.label_velocidad = QtWidgets.QLabel(self.centralwidget)
        self.label_velocidad.setGeometry(QtCore.QRect(190, 160, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_velocidad.setFont(font)
        self.label_velocidad.setObjectName("label_velocidad")
        self.label_dificultad = QtWidgets.QLabel(self.centralwidget)
        self.label_dificultad.setGeometry(QtCore.QRect(190, 190, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_dificultad.setFont(font)
        self.label_dificultad.setObjectName("label_dificultad")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(500, 410, 41, 41))
        self.backButton.setStyleSheet("image: url(:/images/go_back.png);")
        self.backButton.setText("")
        self.backButton.setObjectName("backButton")
        self.pantallaBox = QtWidgets.QComboBox(self.centralwidget)
        self.pantallaBox.setGeometry(QtCore.QRect(270, 220, 101, 21))
        self.pantallaBox.setObjectName("pantallaBox")
        self.pantallaBox.addItem("")
        self.pantallaBox.addItem("")
        self.velocidadBox = QtWidgets.QComboBox(self.centralwidget)
        self.velocidadBox.setGeometry(QtCore.QRect(270, 160, 101, 20))
        self.velocidadBox.setObjectName("velocidadBox")
        self.velocidadBox.addItem("")
        self.velocidadBox.addItem("")
        self.label_velocidad_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_velocidad_2.setGeometry(QtCore.QRect(130, 120, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_velocidad_2.setFont(font)
        self.label_velocidad_2.setObjectName("label_velocidad_2")
        self.dificultadbox = QtWidgets.QComboBox(self.centralwidget)
        self.dificultadbox.setGeometry(QtCore.QRect(270, 190, 101, 20))
        self.dificultadbox.setObjectName("dificultadbox")
        self.dificultadbox.addItem("")
        self.dificultadbox.addItem("")
        self.dificultadbox.addItem("")
        self.guardar_config_button = QtWidgets.QPushButton(self.centralwidget)
        self.guardar_config_button.setGeometry(QtCore.QRect(240, 300, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setBold(True)
        font.setWeight(75)
        self.guardar_config_button.setFont(font)
        self.guardar_config_button.setObjectName("guardar_config_button")
        self.label_pantalla_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_pantalla_2.setGeometry(QtCore.QRect(210, 250, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_pantalla_2.setFont(font)
        self.label_pantalla_2.setObjectName("label_pantalla_2")
        self.pantallaBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.pantallaBox_2.setGeometry(QtCore.QRect(270, 250, 101, 21))
        self.pantallaBox_2.setObjectName("pantallaBox_2")
        self.pantallaBox_2.addItem("")
        self.pantallaBox_2.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 580, 20))
        self.menubar.setObjectName("menubar")
        self.menuTOWER_DEFENSE_GAME = QtWidgets.QMenu(self.menubar)
        self.menuTOWER_DEFENSE_GAME.setObjectName("menuTOWER_DEFENSE_GAME")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menuTOWER_DEFENSE_GAME.addAction(self.action)
        self.menubar.addAction(self.menuTOWER_DEFENSE_GAME.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Button action
        self.guardar_config_button.clicked.connect(self.save_settings)
        self.backButton.clicked.connect(lambda:self.closescr(MainWindow))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tituloajustes.setText(_translate("MainWindow", "AJUSTES PARTIDA"))
        self.label_pantalla.setText(_translate("MainWindow", "Mapa"))
        self.label_velocidad.setText(_translate("MainWindow", "Velocidad"))
        self.label_dificultad.setText(_translate("MainWindow", "Dificultad"))
        self.pantallaBox.setItemText(0, _translate("MainWindow", "Arena_1"))
        self.velocidadBox.setItemText(0, _translate("MainWindow", "Media"))
        self.velocidadBox.setItemText(1, _translate("MainWindow", "Rapida"))
        self.label_velocidad_2.setText(_translate("MainWindow", "Configuración de la partida"))
        self.dificultadbox.setItemText(0, _translate("MainWindow", "Media"))
        self.dificultadbox.setItemText(1, _translate("MainWindow", "Alta"))
        self.dificultadbox.setItemText(2, _translate("MainWindow", "Experto"))
        self.guardar_config_button.setText(_translate("MainWindow", "GUARDAR"))
        self.label_pantalla_2.setText(_translate("MainWindow", "Modo"))
        self.pantallaBox_2.setItemText(0, _translate("MainWindow", "Supervivencia"))
        self.menuTOWER_DEFENSE_GAME.setTitle(_translate("MainWindow", " "))
        self.action.setText(_translate("MainWindow", " "))

    def closescr (self, Form):
        Form.hide()
        print(self.speed)

    def save_settings(self):

        self.speed = self.velocidadBox.currentText()
        self.difficulty = self.dificultadbox.currentText()
        self.map = self.pantallaBox.currentText()
        self.mode = self.pantallaBox_2.currentText()


