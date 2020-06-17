from Final_Interface import *

class Entry_Box(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interface")
        self.setGeometry(500,500,500,500)

        button_1 = QPushButton("Ok",self)
        button_1.move(200,400)
        button_1.clicked.connect(self.show_next_app)

    def show_next_app(self):
        userInfo = QMessageBox.question(self,"Confirmation", "Confirmer",QMessageBox.Yes | QMessageBox.No)
        if userInfo == QMessageBox.Yes:
            window_1.hide()
            window_2.show()
        elif userInfo == QMessageBox.No:
            pass

if __name__ == "__main__":
    import sys
    app = QApplication([])
    window_1 = Entry_Box()
    window_2 = Window()
    window_2.hide()
    window_1.show()
    app.exec_()
    sys.exit()
