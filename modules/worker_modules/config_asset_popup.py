import re
from modules.custom_widgets.custom_main_window import CustomMainWindow
from PySide6 import QtCore
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QListWidgetItem, QFrame, QFileDialog
from modules.ui_templates.config_asset_popup_ui import UiCreateProjectPopup


class AssetWindow(CustomMainWindow):
    """
    This class contains the functionality of Project Manager
    """

    def __init__(self) -> None:
        super(AssetWindow, self).__init__()
        self.__ui: UiCreateProjectPopup = UiCreateProjectPopup()
        self.__ui.setupUi(self)
        self._setMainFrame(self.__ui.main_frame)

        # custom vars
        self.width: int = 32
        self.height: int = 32
        self.project_name: str = None
        self.project_path: str = None
        self.asset_type: str = self.__ui.asset_type_combo_box.currentText()


        # ui changes
        self._CustomMainWindow__custom_title_bar.setMinimumSize(QSize(600, 36))
        self._CustomMainWindow__custom_title_bar.pushButton_minimize.hide()
        self._CustomMainWindow__custom_title_bar.pushButton_maximize.hide()

        # signals
        self.__ui.create_project_push_button.clicked.connect(self._create_new_project)
        self.__ui.browse_push_button.clicked.connect(self._fetch_project_path)
        self.__ui.width_line_edit.textChanged.connect(self._save_width)
        self.__ui.height_line_edit.textChanged.connect(self._save_height)
        self.__ui.project_name_line_edit.textChanged.connect(self._save_project_name)
        self.__ui.project_path_line_edit.textChanged.connect(self._save_project_path)
        self.__ui.asset_type_combo_box.currentTextChanged.connect(self._save_asset_type)

        self.show()

    def _create_new_project(self) -> None:
        if self._validate_project_name():
            print("Invalid Project name")
            return
        if self.project_name and self.project_path:
            print(
                f"Created Project {self.project_name} at \n",
                f"{self.project_path}\n",
                f"Width: {self.width}, Height: {self.height}, Type: {self.asset_type}"
            )
            self.close()

    def _fetch_project_path(self) -> None:
        dir = QFileDialog.getExistingDirectory(
            self, "Select Directory",
            "/home",
            QFileDialog.ShowDirsOnly #| QFileDialog.DontResolveSymlinks
        )
        self.__ui.project_path_line_edit.setText(dir)

    def _save_width(self, text: str) -> None:
        self.width = int(text)
        if int(text) > 128:
            self.width = 128
            self.__ui.width_line_edit.setText("128")

    def _save_height(self, text: str) -> None:
        self.height = int(text)
        if int(text) > 128:
            self.height = 128
            self.__ui.height_line_edit.setText("128")

    def _save_project_name(self, text: str) -> None:
        self.project_name = text

    def _save_project_path(self, text: str) -> None:
        self.project_path = text
 
    def _save_asset_type(self, text: str) -> None:
        self.asset_type = text

    def _validate_project_name(self) -> None:
        """Validates correct project file name."""
        if not self.project_name:
            return
        regex_res = re.search(
            r'[,.!@#$%^&*-+~`?=]|[/()[\]\\:"\'{}|<>]+|^[0-9]',
            self.project_name
        )
        if regex_res is None:
            return False
        return True
