from PyQt5.QtWidgets import QSplashScreen
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QTimer

class SplashScreen(QSplashScreen):
    def __init__(self):
        pixmap = QPixmap("../assets/splash.png")
        super().__init__(pixmap)
        self.setFont(QFont("Arial", 14))

        self.showMessage(
            "Loading Corrode Browser 0.1 Beta...",
            Qt.AlignBottom | Qt.AlignCenter,
            Qt.white
        )

        QTimer.singleShot(2000, self.close)