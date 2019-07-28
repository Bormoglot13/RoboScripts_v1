# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import os

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(275, 241)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        #self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        #self.treeWidget.setColumnCount(1)
        #self.treeWidget.setObjectName("treeWidget")
        #self.treeWidget.headerItem().setText(0, "Доступные модули")
        #self.verticalLayout.addWidget(self.treeWidget)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        #self.listWidget.headerItem().setText(0, "Доступные модули")

        layout = QtWidgets.QGridLayout()
        self.line_edit = QtWidgets.QLineEdit()
        layout.addWidget(self.line_edit)


        self.verticalLayout.addWidget(self.listWidget)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setObjectName("button")
        self.verticalLayout.addWidget(self.button)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Загрузить модуль"))
        self.button.setText(_translate("MainWindow", "Далее"))

class MainApp(QtWidgets.QMainWindow, Ui_MainWindow):

    switch_window = QtCore.pyqtSignal(str)
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.module_url = ''
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.browse_folder)
        #self.line_edit.setText(module_url)   # Выполнить функцию browse_folder
                                                            # при нажатии кнопки
        self.button.clicked.connect(self.switch)

    def switch(self):
        self.switch_window.emit(self.module_url)
        #if self.module_url is not None and self.module_url != '':
        #    self.switch_window.emit(self.line_edit.text())
            #self.switch_window.emit(self.module_url)
        #else:
        #    self.switch_window.emit(self.line_edit.text())

    def browse_folder(self):
        self.listWidget.clear()  # На случай, если в списке уже есть элементы
        file = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите модуль",None,"*.py")
        # открыть диалог выбора директории и установить значение переменной
        # равной пути к выбранной директории
        #print(file[0])
        if file:
            dir_list = []
            i = 0
            basedir = os.path.dirname(file[0])
            parent_dir, cur_dir = os.path.split(basedir)[0], os.path.split(basedir)[1]
            while cur_dir is not None and cur_dir != '':
                dir_list.append((cur_dir, i))
                parent_dir, cur_dir = os.path.split(parent_dir)[0], os.path.split(parent_dir)[1]
                i = i + 1
            dir_list = sorted(dir_list, key=lambda dir: dir[1], reverse=True)
            for k,dir in enumerate(dir_list):
                self.listWidget.addItem(k*3*" " + dir[0])
            self.listWidget.addItem(i*3*" " + os.path.basename(file[0]))
            self.module_url = file[0]
            #time.sleep(5)
            #window2 = WorkApp(file[0])  # Создаём объект класса ExampleApp
            #window2.show()
            #paths = DisplayablePath.make_tree(Path(os.path.dirname(file[0])))
            #for path in paths:
            #    self.listWidget.addItem(path.displayable())
            #for top, dirs, files in os.walk(os.path.dirname(file[0])):
            #    for nm in files:
            #        print(nm)
            #        self.listWidget.addItem(os.path.join(top, nm))
            #for folder in os.path.dirname(file[0]):
            #    self.listWidget.addItem(file[0])
        #if directory:  # не продолжать выполнение, если пользователь не выбрал директорию
        #    for file_name in os.listdir(directory):  # для каждого файла в директории
        #        self.listWidget.addItem(file_name)   # добавить файл в listWidget

