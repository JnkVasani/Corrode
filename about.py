from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About Corrode Browser")
        self.resize(400, 300)

        logo = QLabel()
        logo.setPixmap(QPixmap("../assets/icons/corrode.png").scaled(120, 120, Qt.KeepAspectRatio))

        title = QLabel("Corrode Browser 0.1 Beta")
        title.setFont(QFont("Arial", 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)

        dev = QLabel("Developed by: Janak Vasani")
        dev.setAlignment(Qt.AlignCenter)

        ok = QPushButton("Close")
        ok.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(logo)
        layout.addWidget(title)
        layout.addWidget(dev)
        layout.addWidget(ok)

        self.setLayout(layout)