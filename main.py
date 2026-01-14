import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QAction, QToolBar
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from browser_tab import BrowserTab
from splash import SplashScreen
from about import AboutDialog

class CorrodeBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Corrode Browser 0.1 Beta")
        self.setWindowIcon(QIcon("../assets/icons/corrode.png"))
        self.setGeometry(200, 100, 1200, 800)

        # Tabs
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.tabs.currentChanged.connect(self.update_title)
        self.setCentralWidget(self.tabs)

        # Toolbar
        toolbar = QToolBar("Main Toolbar")
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        new_tab_action = QAction(QIcon("../assets/icons/24.png"), "New Tab", self)
        new_tab_action.triggered.connect(self.add_tab)

        about_action = QAction("About", self)
        about_action.triggered.connect(self.open_about)

        toolbar.addAction(new_tab_action)
        toolbar.addAction(about_action)

        # first tab
        self.add_tab()

    def add_tab(self):
        tab = BrowserTab(self)
        index = self.tabs.addTab(tab, "New Tab")
        self.tabs.setCurrentIndex(index)

        # update tab title dynamically
        tab.webview.titleChanged.connect(
            lambda title, t=tab: self.update_tab_title(t, title)
        )

    def update_tab_title(self, tab, title):
        index = self.tabs.indexOf(tab)
        if index != -1:
            self.tabs.setTabText(index, title[:20])

    def update_title(self):
        current = self.tabs.currentWidget()
        if current:
            self.setWindowTitle("Corrode – " + current.webview.title())

    def close_tab(self, index):
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)

    def open_about(self):
        dialog = AboutDialog(self)
        dialog.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    splash = SplashScreen()
    splash.show()

    window = CorrodeBrowser()
    splash.finish(window)

    window.show()
    sys.exit(app.exec_())