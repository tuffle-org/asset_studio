from PySide6.QtWidgets import QMainWindow
from PySide6 import QtCore
from modules.ui_templates.project_manager_ui import ProjectManagerWindowUi


class ProjectManager(QMainWindow):
    """
    This class contains the functionality of Project Manager
    """

    def __init__(self) -> None:
        super(ProjectManager, self).__init__()
        self.__ui: ProjectManagerWindowUi = ProjectManagerWindowUi()
        self.__ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.show()
