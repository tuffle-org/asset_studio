from PySide6.QtWidgets import QMainWindow
from PySide6 import QtCore
from modules.ui_templates.splash_ui import SplashWindowUi
from modules.worker_modules.project_manager import ProjectManager


class SplashScreen(QMainWindow):
    """
    This class contains the functionality of Splash Screen
    """

    def __init__(self) -> None:
        super(SplashScreen, self).__init__()
        self.__ui: SplashWindowUi = SplashWindowUi()
        self.__ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.__timer = QtCore.QTimer(self)
        self.__timer.singleShot(1000, self.__openProjectManager)
        self.show()

    def __openProjectManager(self):
        """
        This function changes the screen to Project Manager
        """
        self.__project_manager = ProjectManager()
        self.close()
