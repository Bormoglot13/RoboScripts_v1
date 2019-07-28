import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий
import datetime
#from DisplayablePath import *
import time

from PyQt5 import QtWidgets,QtCore
#from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtTest import QTest


import MainWindow  # Это наш конвертированный файл дизайна
import WorkWindow1
import Controller


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    controller = Controller.Controller()
    controller.show_main()
    #window = ExampleApp()  # Создаём объект класса ExampleApp
    #window.show()  # Показываем окно
    #window2 = WorkApp()  # Создаём объект класса ExampleApp
    #window2.show()
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()