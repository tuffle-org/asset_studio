# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'config_asset_popup_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class UiCreateProjectPopup(object):
    def setupUi(self, CreateProjectPopup):
        if not CreateProjectPopup.objectName():
            CreateProjectPopup.setObjectName(u"CreateProjectPopup")
        CreateProjectPopup.resize(600, 300)
        CreateProjectPopup.setMinimumSize(QSize(600, 300))
        CreateProjectPopup.setMaximumSize(QSize(600, 300))
        self.horizontalLayout = QHBoxLayout(CreateProjectPopup)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.main_frame = QFrame(CreateProjectPopup)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.__project_name_label = QLabel(self.main_frame)
        self.__project_name_label.setObjectName(u"__project_name_label")

        self.verticalLayout.addWidget(self.__project_name_label)

        self.__project_name_frame = QFrame(self.main_frame)
        self.__project_name_frame.setObjectName(u"__project_name_frame")
        self.__project_name_frame.setFrameShape(QFrame.StyledPanel)
        self.__project_name_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.__project_name_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.project_name_line_edit = QLineEdit(self.__project_name_frame)
        self.project_name_line_edit.setObjectName(u"project_name_line_edit")
        self.project_name_line_edit.setMinimumSize(QSize(0, 32))

        self.horizontalLayout_2.addWidget(self.project_name_line_edit)

        self.create_project_push_button = QPushButton(self.__project_name_frame)
        self.create_project_push_button.setObjectName(u"create_project_push_button")
        self.create_project_push_button.setMinimumSize(QSize(0, 32))

        self.horizontalLayout_2.addWidget(self.create_project_push_button)

        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout.addWidget(self.__project_name_frame)

        self.__project_path_label = QLabel(self.main_frame)
        self.__project_path_label.setObjectName(u"__project_path_label")

        self.verticalLayout.addWidget(self.__project_path_label)

        self.__project_path_frame = QFrame(self.main_frame)
        self.__project_path_frame.setObjectName(u"__project_path_frame")
        self.__project_path_frame.setFrameShape(QFrame.StyledPanel)
        self.__project_path_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.__project_path_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.project_path_line_edit = QLineEdit(self.__project_path_frame)
        self.project_path_line_edit.setObjectName(u"project_path_line_edit")
        self.project_path_line_edit.setMinimumSize(QSize(0, 32))

        self.horizontalLayout_3.addWidget(self.project_path_line_edit)

        self.browse_push_button = QPushButton(self.__project_path_frame)
        self.browse_push_button.setObjectName(u"browse_push_button")
        self.browse_push_button.setMinimumSize(QSize(0, 32))

        self.horizontalLayout_3.addWidget(self.browse_push_button)

        self.horizontalLayout_3.setStretch(0, 3)
        self.horizontalLayout_3.setStretch(1, 1)

        self.verticalLayout.addWidget(self.__project_path_frame)

        self.__conf_label_frame = QFrame(self.main_frame)
        self.__conf_label_frame.setObjectName(u"__conf_label_frame")
        self.__conf_label_frame.setFrameShape(QFrame.StyledPanel)
        self.__conf_label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.__conf_label_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.__width_label = QLabel(self.__conf_label_frame)
        self.__width_label.setObjectName(u"__width_label")

        self.horizontalLayout_4.addWidget(self.__width_label)

        self.__height_label = QLabel(self.__conf_label_frame)
        self.__height_label.setObjectName(u"__height_label")

        self.horizontalLayout_4.addWidget(self.__height_label)

        self.__asset_type_label = QLabel(self.__conf_label_frame)
        self.__asset_type_label.setObjectName(u"__asset_type_label")

        self.horizontalLayout_4.addWidget(self.__asset_type_label)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 2)

        self.verticalLayout.addWidget(self.__conf_label_frame)

        self.__conf_frame = QFrame(self.main_frame)
        self.__conf_frame.setObjectName(u"__conf_frame")
        self.__conf_frame.setFrameShape(QFrame.StyledPanel)
        self.__conf_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.__conf_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.width_line_edit = QLineEdit(self.__conf_frame)
        self.width_line_edit.setObjectName(u"width_line_edit")
        self.width_line_edit.setMinimumSize(QSize(0, 32))
        self.width_line_edit.setCursor(QCursor(Qt.IBeamCursor))
        self.width_line_edit.setMaxLength(3)
        self.width_line_edit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.width_line_edit)

        self.height_line_edit = QLineEdit(self.__conf_frame)
        self.height_line_edit.setObjectName(u"height_line_edit")
        self.height_line_edit.setMinimumSize(QSize(0, 32))
        self.height_line_edit.setMaxLength(3)
        self.height_line_edit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.height_line_edit)

        self.asset_type_combo_box = QComboBox(self.__conf_frame)
        self.asset_type_combo_box.addItem("")
        self.asset_type_combo_box.addItem("")
        self.asset_type_combo_box.setObjectName(u"asset_type_combo_box")
        self.asset_type_combo_box.setMinimumSize(QSize(0, 32))

        self.horizontalLayout_5.addWidget(self.asset_type_combo_box)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 1)
        self.horizontalLayout_5.setStretch(2, 2)

        self.verticalLayout.addWidget(self.__conf_frame)


        self.horizontalLayout.addWidget(self.main_frame)


        self.retranslateUi(CreateProjectPopup)

        QMetaObject.connectSlotsByName(CreateProjectPopup)
    # setupUi

    def retranslateUi(self, CreateProjectPopup):
        CreateProjectPopup.setWindowTitle(QCoreApplication.translate("CreateProjectPopup", u"Form", None))
        self.__project_name_label.setText(QCoreApplication.translate("CreateProjectPopup", u"Project Name", None))
        self.project_name_line_edit.setPlaceholderText(QCoreApplication.translate("CreateProjectPopup", u"My project", None))
        self.create_project_push_button.setText(QCoreApplication.translate("CreateProjectPopup", u"Create Project", None))
        self.__project_path_label.setText(QCoreApplication.translate("CreateProjectPopup", u"Project Directory Path", None))
        self.project_path_line_edit.setPlaceholderText("")
        self.browse_push_button.setText(QCoreApplication.translate("CreateProjectPopup", u"Browse", None))
        self.__width_label.setText(QCoreApplication.translate("CreateProjectPopup", u"Width", None))
        self.__height_label.setText(QCoreApplication.translate("CreateProjectPopup", u"Height", None))
        self.__asset_type_label.setText(QCoreApplication.translate("CreateProjectPopup", u"Asset Type", None))
        self.width_line_edit.setPlaceholderText(QCoreApplication.translate("CreateProjectPopup", u"32px", None))
        self.height_line_edit.setText("")
        self.height_line_edit.setPlaceholderText(QCoreApplication.translate("CreateProjectPopup", u"32px", None))
        self.asset_type_combo_box.setItemText(0, QCoreApplication.translate("CreateProjectPopup", u"Animated", None))
        self.asset_type_combo_box.setItemText(1, QCoreApplication.translate("CreateProjectPopup", u"Sprite", None))

    # retranslateUi

