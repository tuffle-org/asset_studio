from modules.custom_widgets.custom_main_window import CustomMainWindow
from PySide6 import QtCore
from PySide6.QtWidgets import QListWidgetItem, QFrame
from modules.ui_templates.project_manager_ui import ProjectManagerWindowUi


class ProjectManager(CustomMainWindow):
    """
    This class contains the functionality of Project Manager
    """

    def __init__(self) -> None:
        super(ProjectManager, self).__init__()
        self.__ui: ProjectManagerWindowUi = ProjectManagerWindowUi()
        self.__ui.setupUi(self._central_widget)
        self._setMainFrame(self.__ui.frame_main_frame)
        self.__ui.listWidget_project_list.setFocusPolicy(QtCore.Qt.NoFocus)

        self.items = []
        self.widgets = []
        for i in range(0, 10):
            self.items.append(QListWidgetItem())
            self.widgets.append(QFrame())
            self.widgets[i].setProperty("rounded_corner_frame", True)
            self.widgets[i].setMinimumHeight(60)
            self.__ui.listWidget_project_list.addItem(self.items[i])
            self.__ui.listWidget_project_list.setItemWidget(
                self.items[i], self.widgets[i])
        self.show()
