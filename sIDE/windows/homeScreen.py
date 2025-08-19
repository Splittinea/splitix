# homeScreen.py 
# This file contains the HomeScreen class, which is the main window of the sIDE application. 
# It is written in HTML, pass through a Qt WebEngineView, and serves as the starting point for the IDE.

import os

from PySide6.QtCore import QObject, Slot, QUrl
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWebChannel import QWebChannel
from PySide6.QtGui import QIcon

from modules.WebEngine import sWE # modules/WebEngine.py => class sWE

# Backend
class Backend(QObject):

    @Slot()
    def exitApp(self):
        QApplication.quit()

    @Slot()
    def newProject(self):
        print("New Project Issued")

    @Slot()
    def openProject(self):
        print("Open Project Issued")

    @Slot()
    def openSettings(self):
        print("Settings Issued")


class HomeScreen(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("sIDE - Welcome")
        
        # Page Icon
        icon_path = os.path.join(os.path.dirname(__file__), "../src/icons/sIDE.png")
        self.setWindowIcon(QIcon(icon_path))

        # WebEngineView
        self.web_view = sWE.newPage("homeScreen.html") # pages/homeScreen.html
        self.setCentralWidget(self.web_view)

        # WebChannel + Backend
        self.channel = QWebChannel()
        self.backend = Backend()
        self.channel.registerObject("backend", self.backend)
        # ^ Linked to pages/buttons.js => const backend = channel.objects.backend; (line 18)

        self.web_view.page().setWebChannel(self.channel)