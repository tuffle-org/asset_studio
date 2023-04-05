from PySide6.QtCore import QCoreApplication, QMetaObject
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QMainWindow, QWidget)

import resources.res_rc


class SplashWindowUi(object):
    """
    This class contains the UI elements for Splash Screen
    """

    def setupUi(self, main_window: QMainWindow) -> None:
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(300, 300)
        self.__central_widget: QWidget = QWidget(main_window)
        self.__central_widget.setObjectName(u"centralwidget")
        self.__horizontal_Layout: QHBoxLayout = QHBoxLayout(
            self.__central_widget)
        self.__horizontal_Layout.setObjectName(u"horizontalLayout")
        self.__label: QLabel = QLabel(self.__central_widget)
        self.__label.setObjectName(u"label")
        self.__label.setPixmap(QPixmap(u":/logos/logo.svg"))
        self.__label.setScaledContents(True)

        self.__horizontal_Layout.addWidget(self.__label)

        main_window.setCentralWidget(self.__central_widget)

        self.__retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def __retranslateUi(self, main_window: QMainWindow) -> None:
        main_window.setWindowTitle(QCoreApplication.translate(
            "main_window", u"main_window", None))
        self.__label.setText("")
    # retranslateUi
