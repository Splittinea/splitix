# settingsScreen.py
# This file contains the SettingsScreen class, which is the settings window of the sIDE application.

# It is written in HTML, pass through a Qt WebEngineView, and serves as a page for the IDE.

from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QObject, Slot
from PySide6.QtWebChannel import QWebChannel
from PySide6.QtGui import QIcon

from modules.WebEngine import sWE  # modules/WebEngine.py => class sWE

# Backend
class Backend(QObject):

    @Slot()
    def saveSettings(self):
        print("Settings saved")
    @Slot()
    def resetSettings(self):
        print("Settings reset to default")
        
    @Slot()
    def closeSettings(self):
        print("Settings window closed")


class SettingsScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings")
        self.setWindowIcon(QIcon("../src/icons/sIDE.png"))

        # WebEngineView
        self.web_view = sWE.newPage("settingsScreen.html")

        # WebChannel + Backend
        self.channel = QWebChannel()
        self.backend = Backend()
        self.channel.registerObject("backend", self.backend)
        # ^ Linked to pages/filename.js => const backend = channel.objects.backend; (line XX)

        # Set the central widget of the main window to the web view
        self.setCentralWidget(self.web_view)