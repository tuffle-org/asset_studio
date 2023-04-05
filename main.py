from PySide6.QtWidgets import QApplication
from modules.worker_modules.splash import SplashScreen
import sys
if __name__ == "__main__":
    app: QApplication = QApplication(sys.argv)
    with open("resources/dark_theme_stylesheet.css", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)
    splash_screen: SplashScreen = SplashScreen()

    sys.exit(app.exec())
