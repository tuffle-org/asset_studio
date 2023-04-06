from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QFrame, QHBoxLayout,
                               QLabel, QPushButton, QSizeGrip)
from PySide6.QtGui import QFont, QPixmap, QIcon
from PySide6.QtCore import Qt, QSize
from resources import constants
from resources import res_rc


class CustomTitleBar(QFrame):
    def __init__(self, parent: QWidget) -> None:
        super(CustomTitleBar, self).__init__(parent)
        self.setMinimumSize(QSize(1000, 36))
        self.setMaximumSize(QSize(16777215, 36))
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)

        self.__horizontal_layout = QHBoxLayout(self)
        self.__horizontal_layout.setSpacing(0)
        self.__horizontal_layout.setObjectName(u"__horizontal_layout")
        self.__horizontal_layout.setContentsMargins(5, 0, 5, 0)
        self.__frame_left_title_section = QFrame(self)
        self.__frame_left_title_section.setObjectName(
            u"__frame_left_title_section")
        self.__frame_left_title_section.setFrameShape(QFrame.StyledPanel)
        self.__frame_left_title_section.setFrameShadow(QFrame.Raised)
        self.__horizontal_layout_3 = QHBoxLayout(
            self.__frame_left_title_section)
        self.__horizontal_layout_3.setSpacing(12)
        self.__horizontal_layout_3.setObjectName(u"__horizontal_layout_3")
        self.__horizontal_layout_3.setContentsMargins(0, 0, 0, 0)
        self.__label_logo = QLabel(self.__frame_left_title_section)
        self.__label_logo.setObjectName(u"__label_logo")
        self.__label_logo.setMinimumSize(QSize(20, 20))
        self.__label_logo.setMaximumSize(QSize(20, 20))
        self.__label_logo.setPixmap(QPixmap(u":/logos/logo.svg"))
        self.__label_logo.setScaledContents(True)

        self.__horizontal_layout_3.addWidget(self.__label_logo)

        self.__label_app_title = QLabel(self.__frame_left_title_section)
        self.__label_app_title.setObjectName(u"__label_app_title")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        self.__label_app_title.setFont(font)

        self.__horizontal_layout_3.addWidget(self.__label_app_title)

        self.__horizontal_layout.addWidget(self.__frame_left_title_section)

        self.__frame_right_section = QFrame(self)
        self.__frame_right_section.setObjectName(u"__frame_right_section")
        self.__frame_right_section.setFrameShape(QFrame.StyledPanel)
        self.__frame_right_section.setFrameShadow(QFrame.Raised)

        self.__horizontal_layout_2 = QHBoxLayout(self.__frame_right_section)
        self.__horizontal_layout_2.setSpacing(15)
        self.__horizontal_layout_2.setObjectName(u"__horizontal_layout_2")
        self.__horizontal_layout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_minimize = QPushButton(self.__frame_right_section)
        self.pushButton_minimize.setObjectName(u"pushButton_minimize")
        self.pushButton_minimize.setMinimumSize(QSize(20, 20))
        self.pushButton_minimize.setMaximumSize(QSize(20, 20))
        icon = QIcon()
        icon.addFile(u":/icons/minimize_button.svg",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_minimize.setIcon(icon)
        self.pushButton_minimize.setIconSize(QSize(20, 20))
        self.pushButton_minimize.setProperty(
            constants.MIN_MAX_TITLE_BUTTON_PROPERTY, True)
        self.__horizontal_layout_2.addWidget(self.pushButton_minimize)

        self.pushButton_maximize = QPushButton(self.__frame_right_section)
        self.pushButton_maximize.setObjectName(u"pushButton_maximize")
        self.pushButton_maximize.setMinimumSize(QSize(20, 20))
        self.pushButton_maximize.setMaximumSize(QSize(20, 20))
        icon1 = QIcon()
        icon1.addFile(u":/icons/maximize_button.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_maximize.setIcon(icon1)
        self.pushButton_maximize.setIconSize(QSize(20, 20))
        self.pushButton_maximize.setProperty(
            constants.MIN_MAX_TITLE_BUTTON_PROPERTY, True)
        self.__horizontal_layout_2.addWidget(self.pushButton_maximize)

        self.pushButton_close = QPushButton(self.__frame_right_section)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setMinimumSize(QSize(20, 20))
        self.pushButton_close.setMaximumSize(QSize(20, 20))
        icon2 = QIcon()
        icon2.addFile(u":/icons/close_button.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_close.setIcon(icon2)
        self.pushButton_close.setIconSize(QSize(20, 20))
        self.pushButton_close.setProperty(
            constants.CLOSE_TITLE_BUTTON_PROPERTY, True)
        self.__horizontal_layout_2.addWidget(self.pushButton_close)

        self.__horizontal_layout.addWidget(
            self.__frame_right_section, 0, Qt.AlignRight)

        self.__label_logo.setText("")
        self.__label_app_title.setText(u"Asset Studio")
        self.pushButton_minimize.setText("")
        self.pushButton_maximize.setText("")
        self.pushButton_close.setText("")
