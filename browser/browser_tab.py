from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class BrowserTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.webview = QWebEngineView()

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.load_url)

        back_btn = QPushButton("←")
        back_btn.clicked.connect(self.webview.back)

        forward_btn = QPushButton("→")
        forward_btn.clicked.connect(self.webview.forward)

        reload_btn = QPushButton("⟳")
        reload_btn.clicked.connect(self.webview.reload)

        home_btn = QPushButton("⌂")
        home_btn.clicked.connect(self.load_home)

        bar = QHBoxLayout()
        bar.addWidget(back_btn)
        bar.addWidget(forward_btn)
        bar.addWidget(reload_btn)
        bar.addWidget(home_btn)
        bar.addWidget(self.url_bar)

        layout = QVBoxLayout()
        layout.addLayout(bar)
        layout.addWidget(self.webview)
        self.setLayout(layout)

        self.webview.urlChanged.connect(self.update_url)

        self.load_home()

    def load_home(self):
        self.webview.setHtml(open("../browser/homepage.html", "r").read())

    def load_url(self):
        url = self.url_bar.text()

        if url.startswith("http"):
            self.webview.load(QUrl(url))
        else:
            self.webview.load(QUrl("https://www.google.com/search?q=" + url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())