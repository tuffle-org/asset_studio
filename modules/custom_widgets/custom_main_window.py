from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QFrame, QHBoxLayout,
                               QLabel, QPushButton, QSizeGrip)
from PySide6.QtGui import QFont, QPixmap, QIcon
from PySide6.QtCore import Qt, QSize
from modules.custom_widgets.custom_title_bar import CustomTitleBar
from resources import constants


class CustomMainWindow(QMainWindow):
    """
    A custom window with custom title bar
    """

    def __init__(self):
        super(CustomMainWindow, self).__init__()
        self.resize(1000, 600)
        self.setMinimumSize(QSize(1000, 600))
        self.setWindowFlags(Qt.FramelessWindowHint)
        self._central_widget = QWidget(self)
        self._central_widget.setObjectName(u"_central_widget")
        self._vertical_Layout = QVBoxLayout(self._central_widget)
        self._vertical_Layout.setSpacing(0)
        self._vertical_Layout.setObjectName(u"_vertical_Layout")
        self._vertical_Layout.setContentsMargins(0, 0, 0, 0)
        self.__custom_title_bar = CustomTitleBar(self._central_widget)
        self._vertical_Layout.addWidget(self.__custom_title_bar)

        self.__size_grip_frame = QFrame(self._central_widget)
        self.__size_grip_frame.setMaximumHeight(5)
        self.__size_grip_frame.setFrameShape(QFrame.StyledPanel)
        self.__size_grip_frame.setFrameShadow(QFrame.Raised)
        self.__size_grip_frame.setProperty(
            constants.TRANSPARENT_FRAME_PROPERTY, True)
        self.__size_grip_frame.setObjectName("__size_grip_frame")
        self.__horizontal_layout_grip = QHBoxLayout(self.__size_grip_frame)
        self.__horizontal_layout_grip.setObjectName(
            u"__horizontal_layout_grip")
        self.__horizontal_layout_grip.setContentsMargins(0, 0, 0, 0)

        self.__size_grip_right = QSizeGrip(self._central_widget)
        self.__horizontal_layout_grip.addWidget(
            self.__size_grip_right, 0, Qt.AlignRight)

        self.setCentralWidget(self._central_widget)
        self.__mouse_pressed = False

        self.__custom_title_bar.pushButton_close.pressed.connect(self.close)
        self.__custom_title_bar.pushButton_minimize.pressed.connect(
            self.showMinimized)
        self.__custom_title_bar.pushButton_maximize.pressed.connect(
            self.__maximizeWindow)

    def _setMainFrame(self, main_widget: QFrame):
        self._vertical_Layout.addWidget(main_widget)
        self._vertical_Layout.addWidget(self.__size_grip_frame)

    def __maximizeWindow(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.__custom_title_bar.underMouse():
            self.__mouse_pressed = True
            self.m_Position = event.globalPos()-self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.__mouse_pressed:
            self.move(QMouseEvent.globalPos()-self.m_Position)

    def mouseReleaseEvent(self, QMouseEvent):
        self.__mouse_pressed = False
