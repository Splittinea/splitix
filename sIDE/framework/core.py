# sIDE/framwork/core.py

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView

import os
import sys
import pathlib

#--- Framework Generators ---
from framework.visuals.windows import Window
#----------------------------

#--- Framework Modules ---
from framework.modules.textFormat import log, nextLine
#----------------------------

"""
Core module for the sIDE framework.
Provides essential classes and functions for building and managing applications.
"""

class Application:
    """
    Entry point of any application made using this framework.
    """

    def __init__(self, name: str = "sIDE"):
        self.name = name
        self.windows = [] # Stores created windows

    def add_window(self, window):
        """
        Adds a window to the application.
        """
        self.windows.append(window)
    
    def build(self):
        """
        Builds the application by generating necessary files.
        """
        for window in self.windows:
            window.render()

        log("green", f"Application '{self.name}' built successfully with {len(self.windows)} windows.")
        nextLine()

    def clean(self):
        """
        Cleans the build directory by removing generated files.
        """
        output_dir = os.path.join(os.getcwd(), "pages")
        if os.path.exists(output_dir):
            try :
                for root, dirs, files in os.walk(output_dir, topdown=False):
                    for name in files:
                        os.remove(os.path.join(root, name))
                    for name in dirs:
                        os.rmdir(os.path.join(root, name))
                os.rmdir(output_dir)

                log("green", f"Cleaned build directory: {output_dir}")
                nextLine()

            except Exception as e:
                log("red", f"Error cleaning build directory: {e}")
                nextLine()

            else :
                log("green", f"Cleaned build directory: {output_dir}")
                nextLine()
        else :
            os.makedirs(output_dir, exist_ok=True)

    def run(self):
        """
        Starts the application.
        """

        log("blue", f"=== Running {self.name} ===")
        log("blue", f"Registered Windows: {len(self.windows)}")

        nextLine()

        for w in self.windows:
            log("blue", f" - {w.title}")

        """
        Displays the main window
        """
        home_window = None
        for w in self.windows:
            if w.is_home:
                home_window = w
                break

        if home_window:
            log("blue", f"Displaying home window: {home_window.title}")
        else:
            log("red", "No home window found.")
            return

        formatted_fileName = home_window.title.replace(" ", "_").lower() # Text formatting into a valid file name
        html_path = os.path.join("pages", formatted_fileName, f"{formatted_fileName}.html")

        # Formats the path to be OS agnostic
        html_path = pathlib.Path(html_path).resolve().as_uri()

        self.qt_app = QApplication(sys.argv)

        main_window = QMainWindow()
        main_window.setWindowTitle(home_window.title)
        main_window.resize(home_window.width, home_window.height)

        webview = QWebEngineView()
        webview.load(html_path)

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.addWidget(webview)
        main_window.setCentralWidget(central_widget)

        main_window.show()
        self.qt_app.exec()