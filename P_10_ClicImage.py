from QLabelClickeable import clickable

import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui
qtCreatorFile = "P_10_ClicImage.ui"  # Nombre del archivo
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        clickable(self.img).connect(self.clicImage)
        self.btn_borrar.clicked.connect(self.borrar)

    def clicImage(self):
        print("Hiciste clic")
        self.txt_Nombre.setText("Amando")
        self.txt_Edad.setText("20")
        self.txt_Ocupacion.setText("Estudiambre")

    def borrar(self):
        self.txt_Nombre.setText("")
        self.txt_Edad.setText("")
        self.txt_Ocupacion.setText("")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())