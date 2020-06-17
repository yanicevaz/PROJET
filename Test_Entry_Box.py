from PySide2.QtWidgets import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from stl import mesh
from mpl_toolkits import mplot3d
import sys
from Bateau import *

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        #self.__gravite = 9.81 #Initiale
        self.__boat = ""
        self.__gravite = 0
        #Config initiale
        self.setWindowTitle("Position d'équilibre d'un bateau")
        self.setMinimumSize(500, 300)
        #Layouts
        self.layout = QVBoxLayout()
        self.layoutEntrees = QHBoxLayout()
        self.layoutBateau1 = QHBoxLayout()
        self.layoutBateau2 = QHBoxLayout()
        #Messages bienvenue et choix, ajout au layout
        self.welcome = QLabel("Bienvenue sur l'interface de calcul de position de bateaux à l'équilibre")
        self.choix1 = QLabel("Veuillez entrez votre masse (en kg) ainsi que  votre choix de gravité : ")
        self.choix2 = QLabel("Veuillez choisir votre bateau")
        self.layout.addWidget(self.welcome)
        self.layout.addWidget(self.choix1)
        #Creation menu déroulant
        self.choose = QComboBox()
        self.choose.addItem("Gravite terrestre") #9.81
        self.choose.addItem("Gravite lunaire") #1.62
        self.choose.addItem("Gravite martienne") #3.71
        #Entrée de la masse
        self.entreemasse = QLabel("Entrez la masse du bateau :")
        self.txtenter = QLineEdit("300")
        #Organisation des layouts
        self.layoutEntrees.addWidget(self.choose)
        self.layoutEntrees.addWidget(self.entreemasse)
        self.layoutEntrees.addWidget(self.txtenter)
        #Ajout au layout en respectant l'ordre
        self.layout.addLayout(self.layoutEntrees)
        self.layout.addWidget(self.choix2)
        #Bouton + image
        # self.buttonbateau = QPushButton("bato 1")
        # self.buttonbateau.setStyleSheet("background-image: url(bah-tot.jpg)")
        # self.buttonbateau.setFixedSize(200,121)
        #self.layout.addWidget(self.buttonbateau)
        self.VHullButton = QRadioButton()
        self.VHullButton.setText("Bateau 1 : V_Hull")
        self.layoutBateau1.addWidget(self.VHullButton)
        self.RectangularButton = QRadioButton()
        self.RectangularButton.setText("Bateau 2 : Rectangular_HULL")
        self.layoutBateau1.addWidget(self.RectangularButton)
        self.layout.addLayout(self.layoutBateau1)
        self.buttonvalidate = QPushButton("Valider")
        self.buttonvalidate.clicked.connect(self.buttonClicked)
        self.layout.addWidget(self.buttonvalidate)
        self.setLayout(self.layout)

    def buttonClicked(self):
        #Recuperation de la valeur du menu déroulant
        if self.choose.currentText() == "Gravite lunaire":
            self.__gravite = 1.62
        elif self.choose.currentText() == "Gravite martienne":
            self.__gravite = 3.71
        elif self.choose.currentText() == "Gravite terrestre":
            self.__gravite = 9.81

        #Recuperation de la masse
        self.__masse = self.txtenter.text()

        #Recuperation du choix de fichier
        if (self.RectangularButton.isChecked() == False and self.VHullButton.isChecked()) == False:
            self.txtErreur = QLabel("Vous devez choisir un modèle de bateau !")
            self.layout.addWidget(self.txtErreur)
            #self.setLayout(self.layout)
        if self.RectangularButton.isChecked() == True :
            self.__boat = "Rectangular_HULL.stl"
        elif self.VHullButton.isChecked() == True :
            self.__boat = "V_HULL.stl"

        #Test
        monBateau = Bateau("Salut",self.__masse,self.__boat,self.__gravite)
        print(monBateau.getCoque())

if __name__ == "__main__":
    application = QApplication([])
    window = Window()
    window.show()
    application.exec_()
