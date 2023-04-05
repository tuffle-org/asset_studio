
from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont, QIcon, QPixmap)
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel,
                               QLineEdit, QListWidget, QMainWindow,
                               QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import resources.res_rc


class ProjectManagerWindowUi(object):
    def setupUi(self, main_window: QMainWindow) -> None:
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(1000, 662)
        main_window.setMinimumSize(QSize(1000, 630))
        self.__central_widget = QWidget(main_window)
        self.__central_widget.setObjectName(u"__central_widget")
        self.__vertical_Layout = QVBoxLayout(self.__central_widget)
        self.__vertical_Layout.setSpacing(0)
        self.__vertical_Layout.setObjectName(u"__vertical_Layout")
        self.__vertical_Layout.setContentsMargins(10, 5, 10, 10)
        self.__frame_title_bar = QFrame(self.__central_widget)
        self.__frame_title_bar.setObjectName(u"__frame_title_bar")
        self.__frame_title_bar.setMinimumSize(QSize(0, 36))
        self.__frame_title_bar.setMaximumSize(QSize(16777215, 32))
        self.__frame_title_bar.setFrameShape(QFrame.StyledPanel)
        self.__frame_title_bar.setFrameShadow(QFrame.Raised)
        self.__horizontal_layout = QHBoxLayout(self.__frame_title_bar)
        self.__horizontal_layout.setSpacing(0)
        self.__horizontal_layout.setObjectName(u"__horizontal_layout")
        self.__horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.__frame_left_title_section = QFrame(self.__frame_title_bar)
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
        self.__label_logo.setMinimumSize(QSize(30, 30))
        self.__label_logo.setMaximumSize(QSize(30, 30))
        self.__label_logo.setPixmap(QPixmap(u":/logos/logo.svg"))
        self.__label_logo.setScaledContents(True)

        self.__horizontal_layout_3.addWidget(self.__label_logo)

        self.__label_app_title = QLabel(self.__frame_left_title_section)
        self.__label_app_title.setObjectName(u"__label_app_title")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(14)
        self.__label_app_title.setFont(font)

        self.__horizontal_layout_3.addWidget(self.__label_app_title)

        self.__horizontal_layout.addWidget(self.__frame_left_title_section)

        self.__frame_right_section = QFrame(self.__frame_title_bar)
        self.__frame_right_section.setObjectName(u"__frame_right_section")
        self.__frame_right_section.setFrameShape(QFrame.StyledPanel)
        self.__frame_right_section.setFrameShadow(QFrame.Raised)
        self.__horizontal_layout_2 = QHBoxLayout(self.__frame_right_section)
        self.__horizontal_layout_2.setSpacing(15)
        self.__horizontal_layout_2.setObjectName(u"__horizontal_layout_2")
        self.__horizontal_layout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_minimize = QPushButton(self.__frame_right_section)
        self.pushButton_minimize.setObjectName(u"pushButton_minimize")
        self.pushButton_minimize.setMinimumSize(QSize(18, 18))
        self.pushButton_minimize.setMaximumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(u":/icons/minimize_button.svg",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_minimize.setIcon(icon)
        self.pushButton_minimize.setIconSize(QSize(30, 30))
        # self.pushButton_minimize.setStyleSheet(
        #     "background-color: rgba(0,0,0,0);")
        self.__horizontal_layout_2.addWidget(self.pushButton_minimize)

        self.pushButton_maximize = QPushButton(self.__frame_right_section)
        self.pushButton_maximize.setObjectName(u"pushButton_maximize")
        self.pushButton_maximize.setMinimumSize(QSize(18, 18))
        self.pushButton_maximize.setMaximumSize(QSize(30, 30))
        icon1 = QIcon()
        icon1.addFile(u":/icons/maximize_button.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_maximize.setIcon(icon1)
        self.pushButton_maximize.setIconSize(QSize(30, 30))

        self.__horizontal_layout_2.addWidget(self.pushButton_maximize)

        self.pushButton_close = QPushButton(self.__frame_right_section)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setMinimumSize(QSize(30, 30))
        self.pushButton_close.setMaximumSize(QSize(30, 30))
        icon2 = QIcon()
        icon2.addFile(u":/icons/close_button.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_close.setIcon(icon2)
        self.pushButton_close.setIconSize(QSize(30, 30))

        self.__horizontal_layout_2.addWidget(self.pushButton_close)

        self.__horizontal_layout.addWidget(
            self.__frame_right_section, 0, Qt.AlignRight)

        self.__vertical_Layout.addWidget(self.__frame_title_bar)

        self.__frame_main_frame = QFrame(self.__central_widget)
        self.__frame_main_frame.setObjectName(u"__frame_main_frame")
        self.__frame_main_frame.setFrameShape(QFrame.StyledPanel)
        self.__frame_main_frame.setFrameShadow(QFrame.Raised)
        self.__horizontal_layout_4 = QHBoxLayout(self.__frame_main_frame)
        self.__horizontal_layout_4.setObjectName(u"__horizontal_layout_4")
        self.__horizontal_layout_4.setContentsMargins(0, -1, 0, -1)
        self.__frame_main_left_section = QFrame(self.__frame_main_frame)
        self.__frame_main_left_section.setObjectName(
            u"__frame_main_left_section")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.__frame_main_left_section.sizePolicy().hasHeightForWidth())
        self.__frame_main_left_section.setSizePolicy(sizePolicy)
        self.__frame_main_left_section.setMinimumSize(QSize(735, 0))
        self.__frame_main_left_section.setFrameShape(QFrame.StyledPanel)
        self.__frame_main_left_section.setFrameShadow(QFrame.Raised)
        self.__vertical_Layout_3 = QVBoxLayout(self.__frame_main_left_section)
        self.__vertical_Layout_3.setObjectName(u"__vertical_Layout_3")
        self.__vertical_Layout_3.setContentsMargins(0, -1, -1, -1)
        self.lineEdit_search_projects = QLineEdit(
            self.__frame_main_left_section)
        self.lineEdit_search_projects.setObjectName(
            u"lineEdit_search_projects")
        self.lineEdit_search_projects.setMinimumSize(QSize(0, 40))

        self.__vertical_Layout_3.addWidget(self.lineEdit_search_projects)

        self.listWidget_project_list = QListWidget(
            self.__frame_main_left_section)
        self.listWidget_project_list.setObjectName(u"listWidget_project_list")

        self.__vertical_Layout_3.addWidget(self.listWidget_project_list)

        self.__horizontal_layout_4.addWidget(self.__frame_main_left_section)

        self.__frame_main_right_section = QFrame(self.__frame_main_frame)
        self.__frame_main_right_section.setObjectName(
            u"__frame_main_right_section")
        self.__frame_main_right_section.setMinimumSize(QSize(210, 300))
        self.__frame_main_right_section.setMaximumSize(QSize(210, 16777215))
        self.__frame_main_right_section.setFrameShape(QFrame.StyledPanel)
        self.__frame_main_right_section.setFrameShadow(QFrame.Raised)
        self.__vertical_Layout_2 = QVBoxLayout(self.__frame_main_right_section)
        self.__vertical_Layout_2.setSpacing(8)
        self.__vertical_Layout_2.setObjectName(u"__vertical_Layout_2")
        self.__vertical_Layout_2.setContentsMargins(0, -1, 0, -1)
        self.pushButton_new_project = QPushButton(
            self.__frame_main_right_section)
        self.pushButton_new_project.setObjectName(u"pushButton_new_project")
        self.pushButton_new_project.setMinimumSize(QSize(200, 40))
        self.pushButton_new_project.setMaximumSize(QSize(200, 40))

        self.__vertical_Layout_2.addWidget(
            self.pushButton_new_project, 0, Qt.AlignHCenter | Qt.AlignTop)

        self.pushButton_edit_project = QPushButton(
            self.__frame_main_right_section)
        self.pushButton_edit_project.setObjectName(u"pushButton_edit_project")
        self.pushButton_edit_project.setMinimumSize(QSize(200, 40))
        self.pushButton_edit_project.setMaximumSize(QSize(200, 40))

        self.__vertical_Layout_2.addWidget(
            self.pushButton_edit_project, 0, Qt.AlignHCenter | Qt.AlignTop)

        self.pushButton_remove_project = QPushButton(
            self.__frame_main_right_section)
        self.pushButton_remove_project.setObjectName(
            u"pushButton_remove_project")
        self.pushButton_remove_project.setMinimumSize(QSize(200, 40))
        self.pushButton_remove_project.setMaximumSize(QSize(200, 40))

        self.__vertical_Layout_2.addWidget(
            self.pushButton_remove_project, 0, Qt.AlignHCenter | Qt.AlignTop)

        self.pushButton_rename_project = QPushButton(
            self.__frame_main_right_section)
        self.pushButton_rename_project.setObjectName(
            u"pushButton_rename_project")
        self.pushButton_rename_project.setMinimumSize(QSize(200, 40))
        self.pushButton_rename_project.setMaximumSize(QSize(200, 40))

        self.__vertical_Layout_2.addWidget(
            self.pushButton_rename_project, 0, Qt.AlignHCenter | Qt.AlignTop)

        self.pushButton_import_project = QPushButton(
            self.__frame_main_right_section)
        self.pushButton_import_project.setObjectName(
            u"pushButton_import_project")
        self.pushButton_import_project.setMinimumSize(QSize(200, 40))
        self.pushButton_import_project.setMaximumSize(QSize(200, 40))

        self.__vertical_Layout_2.addWidget(
            self.pushButton_import_project, 0, Qt.AlignHCenter | Qt.AlignTop)

        self.pushButton_about = QPushButton(self.__frame_main_right_section)
        self.pushButton_about.setObjectName(u"pushButton_about")
        self.pushButton_about.setMinimumSize(QSize(200, 40))
        self.pushButton_about.setMaximumSize(QSize(200, 40))

        self.__vertical_Layout_2.addWidget(
            self.pushButton_about, 0, Qt.AlignHCenter | Qt.AlignBottom)

        self.__horizontal_layout_4.addWidget(
            self.__frame_main_right_section, 0, Qt.AlignRight | Qt.AlignTop)

        self.__vertical_Layout.addWidget(self.__frame_main_frame)

        main_window.setCentralWidget(self.__central_widget)

        self.__retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def __retranslateUi(self, main_window: QMainWindow) -> None:
        main_window.setWindowTitle(QCoreApplication.translate(
            "main_window", u"main_window", None))
        self.__label_logo.setText("")
        self.__label_app_title.setText(
            QCoreApplication.translate("main_window", u"Asset Studio", None))
        self.pushButton_minimize.setText("")
        self.pushButton_maximize.setText("")
        self.pushButton_close.setText("")
        self.pushButton_new_project.setText(
            QCoreApplication.translate("main_window", u"New Project", None))
        self.pushButton_edit_project.setText(
            QCoreApplication.translate("main_window", u"Edit", None))
        self.pushButton_remove_project.setText(
            QCoreApplication.translate("main_window", u"Remove", None))
        self.pushButton_rename_project.setText(
            QCoreApplication.translate("main_window", u"Rename", None))
        self.pushButton_import_project.setText(
            QCoreApplication.translate("main_window", u"Import", None))
        self.pushButton_about.setText(
            QCoreApplication.translate("main_window", u"About", None))
    # retranslateUi
