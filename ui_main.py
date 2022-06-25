# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(770, 326)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 751, 251))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.options = QVBoxLayout()
        self.options.setObjectName(u"options")
        self.line_Edit_module_width = QLineEdit(self.widget)
        self.line_Edit_module_width.setObjectName(u"line_Edit_module_width")

        self.options.addWidget(self.line_Edit_module_width)

        self.lineEdit_module_height = QLineEdit(self.widget)
        self.lineEdit_module_height.setObjectName(u"lineEdit_module_height")

        self.options.addWidget(self.lineEdit_module_height)

        self.lineEdit_font_size = QLineEdit(self.widget)
        self.lineEdit_font_size.setObjectName(u"lineEdit_font_size")

        self.options.addWidget(self.lineEdit_font_size)

        self.lineEdit_quiet_zone = QLineEdit(self.widget)
        self.lineEdit_quiet_zone.setObjectName(u"lineEdit_quiet_zone")

        self.options.addWidget(self.lineEdit_quiet_zone)

        self.lineEdit_text_distance = QLineEdit(self.widget)
        self.lineEdit_text_distance.setObjectName(u"lineEdit_text_distance")

        self.options.addWidget(self.lineEdit_text_distance)

        self.lineEdit_write_text = QLineEdit(self.widget)
        self.lineEdit_write_text.setObjectName(u"lineEdit_write_text")

        self.options.addWidget(self.lineEdit_write_text)

        self.lineEdit_dpi = QLineEdit(self.widget)
        self.lineEdit_dpi.setObjectName(u"lineEdit_dpi")

        self.options.addWidget(self.lineEdit_dpi)

        self.lineEdit_write_path = QLineEdit(self.widget)
        self.lineEdit_write_path.setObjectName(u"lineEdit_write_path")
        self.lineEdit_write_path.setReadOnly(False)

        self.options.addWidget(self.lineEdit_write_path)

        self.horizontalLayout.addLayout(self.options)

        self.code_and_output = QVBoxLayout()
        self.code_and_output.setObjectName(u"code_and_output")
        self.textEdit = QPlainTextEdit(self.widget)
        self.textEdit.setObjectName(u"textEdit")

        self.code_and_output.addWidget(self.textEdit)

        self.button = QPushButton(self.widget)
        self.button.setObjectName(u"button")

        self.code_and_output.addWidget(self.button)

        self.horizontalLayout.addLayout(self.code_and_output)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 770, 28))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow",
                                       u"\u751f\u6210\u6761\u5f62\u7801",
                                       None))
        self.line_Edit_module_width.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindow",
                u"\u4e8c\u7ef4\u7801\u5bbd\u5ea6\uff0c\u9ed8\u8ba40.3", None))
        self.lineEdit_module_height.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindow",
                u"\u4e8c\u7ef4\u7801\u9ad8\u5ea6\uff0c\u9ed8\u8ba415", None))
        self.lineEdit_font_size.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindow", u"\u5b57\u4f53\u5927\u5c0f\uff0c\u9ed8\u8ba410",
                None))
        self.lineEdit_quiet_zone.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindow",
                u"\u4e24\u8fb9\u7a7a\u767d\u5bbd\u5ea6\uff0c\u9ed8\u8ba42",
                None))
        self.lineEdit_text_distance.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindow",
                u"\u4e0b\u65b9\u6587\u672c\u8ddd\u79bb\u6761\u5f62\u7801\u8ddd\u79bb\uff0c\u9ed8\u8ba45.0",
                None))
        self.lineEdit_write_text.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindow",
                u"\u662f\u5426\u5c55\u793a\u6761\u5f62\u7801\u5bf9\u5e94\u6587\u5b57\uff0c\u9ed8\u8ba4\u5c55\u793a\uff0cTure/False",
                None))
        self.lineEdit_dpi.setPlaceholderText(
            QCoreApplication.translate("MainWindow",
                                       u"dpi\uff0c\u9ed8\u8ba4300", None))
        self.lineEdit_write_path.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindow",
                u"\u8f93\u51fa\u56fe\u7247\u8def\u5f84\uff0c\u9ed8\u8ba4\u5f53\u524d\u76ee\u5f55",
                None))
        self.textEdit.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindow",
                u"\u8bf7\u8f93\u5165\u8981\u751f\u6210\u7684\u6761\u5f62\u7801\uff0c\u591a\u4e2a\u4ee5\u56de\u8f66\u5206\u9694",
                None))
        self.button.setText(
            QCoreApplication.translate("MainWindow",
                                       u"\u751f\u6210\u6761\u5f62\u7801",
                                       None))

    # retranslateUi
