import MainWindow  # Это наш конвертированный файл дизайна
import WorkWindow1

from PyQt5 import QtWidgets,QtCore



class Communicate(QtCore.QObject):

    closeApp = QtCore.pyqtSignal()


class Login(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        #self.c = Communicate()
        #self.c.closeApp.connect(self.close)

        self.setWindowTitle('Login')

        layout = QtWidgets.QGridLayout()

        self.button = QtWidgets.QPushButton('Login')
        self.button.clicked.connect(self.login)

        layout.addWidget(self.button)

        self.setLayout(layout)

        #QTest.mouseClick(layout.itemAt(0).widget(), QtCore.Qt.LeftButton)
        #QTest.mouseClick(,QtCore.Qt.LeftButton)

    #def mousePressEvent(self, event):
    #    self.c.closeApp.emit()

    def login(self):
        self.switch_window.emit()

class Controller:

    def __init__(self):
        pass

    def show_login(self):
        self.login = Login()
        self.login.switch_window.connect(self.show_main)
        self.login.show()

    def show_main(self):
        self.window = MainWindow.MainApp()
        self.window.switch_window.connect(self.show_window_two)
        #self.login.close()
        self.window.show()

    def show_window_two(self, text):
        self.window_two = WorkWindow1.WorkApp(text)
        self.window.close()
        self.window_two.show()