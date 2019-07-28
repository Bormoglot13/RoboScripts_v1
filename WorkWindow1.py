# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'workWindow1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий
import datetime
import time

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(474, 240)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(12, 12, 451, 16))
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(10, 100, 454, 96))
        self.listWidget.setObjectName("listWidget")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(12, 48, 221, 31))
        self.textEdit.setObjectName("textEdit")
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 30, 451, 61))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.btnStart = QtWidgets.QPushButton(Form)
        self.btnStart.setGeometry(QtCore.QRect(10, 200, 113, 32))
        self.btnStart.setObjectName("btnStart")
        self.btnExcel = QtWidgets.QPushButton(Form)
        self.btnExcel.setGeometry(QtCore.QRect(240, 50, 83, 32))
        self.btnExcel.setObjectName("btnExcel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Роботизация"))
        self.label.setText(_translate("Form", "Модуль"))
        self.btnStart.setText(_translate("Form", "Старт"))
        self.btnExcel.setText(_translate("Form", "Обзор"))



class WorkApp(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self,module_url):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.module_url = module_url
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.btnExcel.clicked.connect(self.browse_excel)
        self.btnStart.clicked.connect(self.start)
        _translate = QtCore.QCoreApplication.translate
        self.ModuleName, self.ModuleDesc = self.readDesc()
        self.label.setText(_translate("Form", "Модуль" + ": " + self.ModuleName))

    def browse_excel(self):
        self.listWidget.clear()  # На случай, если в списке уже есть элементы
        file = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл Excel",None,"*.xls;*.xlsx")
        # открыть диалог выбора директории и установить значение переменной
        # равной пути к выбранной директории
        #print(file[0])
        if file:
            self.textEdit.setText(os.path.basename(file[0]))
            self.excel_url = file[0]

    def readDesc(self):
        import json
        base_dir = os.path.dirname(self.module_url)
        with open(os.path.join(base_dir,'description.json'), encoding='utf-8') as json_file:
            data = json.load(json_file)
        return data['name'], data['description']

    def log(self,text):
        self.listWidget.addItem(str(datetime.datetime.now()) + "\t" + text)

    def start(self):
        self.listWidget.clear()  # На случай, если в списке уже есть элементы
        self.log("Стартуем...")
        os.system('python ' + self.module_url  + ' ' + self.excel_url)
        self.log("Работа скрипта завершена")

        #import main
        #main.main()
