
from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont, QIcon, QPixmap)
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel,
                               QLineEdit, QListWidget, QMainWindow,
                               QPushButton, QSizePolicy, QVBoxLayout, QWidget, QSizeGrip)
import resources.res_rc
from resources import constants


class ProjectManagerWindowUi(object):
    def setupUi(self, central_widget: QWidget) -> None:
        """
        This function populates a Central Widget with various Ui Elements
        """
        self.frame_main_frame = QFrame(central_widget)
        self.frame_main_frame.setObjectName(u"frame_main_frame")
        self.frame_main_frame.setFrameShape(QFrame.StyledPanel)
        self.frame_main_frame.setFrameShadow(QFrame.Raised)
        self.frame_main_frame.setProperty(
            constants.TRANSPARENT_FRAME_PROPERTY, True)
        self.__horizontal_layout_4 = QHBoxLayout(self.frame_main_frame)
        self.__horizontal_layout_4.setObjectName(u"__horizontal_layout_4")
        self.__horizontal_layout_4.setContentsMargins(10, 15, 10, 15)
        self.__frame_main_left_section = QFrame(self.frame_main_frame)

        self.__frame_main_left_section.setMinimumSize(QSize(735, 500))
        self.__frame_main_left_section.setFrameShape(QFrame.StyledPanel)
        self.__frame_main_left_section.setFrameShadow(QFrame.Raised)
        self.__frame_main_left_section.setProperty(
            constants.TRANSPARENT_FRAME_PROPERTY, True)
        self.__vertical_Layout_3 = QVBoxLayout(self.__frame_main_left_section)
        self.__vertical_Layout_3.setObjectName(u"__vertical_Layout_3")
        self.__vertical_Layout_3.setSpacing(10)
        self.__vertical_Layout_3.setContentsMargins(0, 0, 0, 0)
        self.__frame_top = QFrame(self.__frame_main_left_section)

        self.__frame_top.setMinimumSize(QSize(735, 0))
        self.__frame_top.setFrameShape(QFrame.StyledPanel)
        self.__frame_top.setFrameShadow(QFrame.Raised)
        self.__frame_top.setProperty(
            constants.TRANSPARENT_FRAME_PROPERTY, True)

        self.__horizontal_layout_top = QHBoxLayout(self.__frame_top)
        self.__horizontal_layout_top.setObjectName(u"__horizontal_layout_top")
        self.__horizontal_layout_top.setSpacing(10)
        self.__horizontal_layout_top.setContentsMargins(0, 0, 0, 0)

        self.lineEdit_search_projects = QLineEdit(
            self.__frame_top)
        self.lineEdit_search_projects.setPlaceholderText("Search Projects...")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(constants.LINE_EDIT_FONT_SIZE)
        self.lineEdit_search_projects.setFont(font)
        self.lineEdit_search_projects.setObjectName(
            u"lineEdit_search_projects")
        self.lineEdit_search_projects.setMinimumSize(QSize(0, 40))
        self.__horizontal_layout_top.addWidget(
            self.lineEdit_search_projects, 0, Qt.AlignTop)
# ANCHOR

        self.pushButton_search = QPushButton(
            self.__frame_top)
        self.pushButton_search.setObjectName(u"pushButton_search")
        self.pushButton_search.setMinimumSize(QSize(40, 40))
        self.pushButton_search.setMaximumSize(QSize(40, 40))

        icon = QIcon()
        icon.addFile(u":/icons/search_button.svg",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_search.setIcon(icon)
        self.pushButton_search.setIconSize(QSize(30, 30))
        self.__horizontal_layout_top.addWidget(
            self.pushButton_search, 0, Qt.AlignTop)

        self.__vertical_Layout_3.addWidget(
            self.__frame_top, 0, Qt.AlignTop)

        self.listWidget_project_list = QListWidget(
            self.__frame_main_left_section)

        self.listWidget_project_list.setObjectName(u"listWidget_project_list")

        self.__vertical_Layout_3.addWidget(
            self.listWidget_project_list)

        self.__horizontal_layout_4.addWidget(
            self.__frame_main_left_section)

        self.__frame_main_right_section = QFrame(self.frame_main_frame)
        self.__frame_main_right_section.setObjectName(
            u"__frame_main_right_section")
        self.__frame_main_right_section.setMinimumSize(QSize(210, 300))
        self.__frame_main_right_section.setMaximumSize(QSize(210, 16777215))
        self.__frame_main_right_section.setFrameShape(QFrame.StyledPanel)
        self.__frame_main_right_section.setFrameShadow(QFrame.Raised)
        self.__frame_main_right_section.setProperty(
            constants.TRANSPARENT_FRAME_PROPERTY, True)
        self.__vertical_Layout_2 = QVBoxLayout(self.__frame_main_right_section)
        self.__vertical_Layout_2.setSpacing(8)
        self.__vertical_Layout_2.setObjectName(u"__vertical_Layout_2")
        self.__vertical_Layout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_new_project = QPushButton(
            self.__frame_main_right_section)
        self.pushButton_new_project.setObjectName(u"pushButton_new_project")
        self.pushButton_new_project.setMinimumSize(QSize(200, 40))
        self.pushButton_new_project.setMaximumSize(QSize(200, 40))
        self.pushButton_new_project.setProperty(
            constants.SPECIAL_BUTTON_PROPERTY, True)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(constants.PUSH_BUTTON_FONT_SIZE)
        self.pushButton_new_project.setFont(font)
        self.__vertical_Layout_2.addWidget(
            self.pushButton_new_project, 0, Qt.AlignHCenter | Qt.AlignTop)

        self.pushButton_edit_project = QPushButton(
            self.__frame_main_right_section)
        self.pushButton_edit_project.setObjectName(u"pushButton_edit_project")
        self.pushButton_edit_project.setMinimumSize(QSize(200, 40))
        self.pushButton_edit_project.setMaximumSize(QSize(200, 40))
        self.pushButton_edit_project.setFont(font)
        self.__vertical_Layout_2.addWidget(
            self.pushButton_edit_project, 0, Qt.AlignHCenter | Qt.AlignTop)

        self.pushButton_remove_project = QPushButton(
            self.__frame_main_right_section)
        self.pushButton_remove_project.setObjectName(
            u"pushButton_remove_project")
        self.pushButton_remove_project.setMinimumSize(QSize(200, 40))
        self.pushButton_remove_project.setMaximumSize(QSize(200, 40))
        self.pushButton_remove_project.setFont(font)
        self.__vertical_Layout_2.addWidget(
            self.pushButton_remove_project, 0, Qt.AlignHCenter | Qt.AlignTop)

        self.pushButton_rename_project = QPushButton(
            self.__frame_main_right_section)
        self.pushButton_rename_project.setObjectName(
            u"pushButton_rename_project")
        self.pushButton_rename_project.setMinimumSize(QSize(200, 40))
        self.pushButton_rename_project.setMaximumSize(QSize(200, 40))
        self.pushButton_rename_project.setFont(font)
        self.__vertical_Layout_2.addWidget(
            self.pushButton_rename_project, 0, Qt.AlignHCenter | Qt.AlignTop)

        self.pushButton_import_project = QPushButton(
            self.__frame_main_right_section)
        self.pushButton_import_project.setObjectName(
            u"pushButton_import_project")
        self.pushButton_import_project.setMinimumSize(QSize(200, 40))
        self.pushButton_import_project.setMaximumSize(QSize(200, 40))
        self.pushButton_import_project.setFont(font)
        self.__vertical_Layout_2.addWidget(
            self.pushButton_import_project, 0, Qt.AlignHCenter | Qt.AlignTop)

        self.pushButton_about = QPushButton(self.__frame_main_right_section)
        self.pushButton_about.setObjectName(u"pushButton_about")
        self.pushButton_about.setMinimumSize(QSize(200, 40))
        self.pushButton_about.setMaximumSize(QSize(200, 40))
        self.pushButton_about.setFont(font)
        self.__vertical_Layout_2.addWidget(
            self.pushButton_about, 0, Qt.AlignHCenter | Qt.AlignBottom)

        self.__horizontal_layout_4.addWidget(
            self.__frame_main_right_section, 0, Qt.AlignTop)

        self.pushButton_new_project.setText(u"New Project")
        self.pushButton_edit_project.setText(u"Edit")
        self.pushButton_remove_project.setText(u"Remove")
        self.pushButton_rename_project.setText(u"Rename")
        self.pushButton_import_project.setText(u"Import")
        self.pushButton_about.setText(u"About")
