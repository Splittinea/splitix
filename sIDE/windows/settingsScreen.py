# settingsScreen.py
# This file contains the SettingsScreen class, which is the settings window of the sIDE application.

# It is written in HTML, pass through a Qt WebEngineView, and serves as a page for the IDE.

from PySide6.QtWidgets import QMainWindow

from modules.WebEngine import sWE  # Custom WebEngine class to handle web pages

class SettingsScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle("Settings")

        # Using sWE, displays a new web page
        self.web_view = sWE.newPage("settingsScreen.html")

        # Set the central widget of the main window to the web view
        self.setCentralWidget(self.web_view)