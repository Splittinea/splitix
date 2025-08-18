from PySide6.QtCore import QUrl, QObject, Slot
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QApplication

from pathlib import Path

class sWE :

    # HTML Page importation, pages must be in windows/pages
    @staticmethod
    def newPage(name: str) -> QWebEngineView:
        web_view = QWebEngineView()

        # Construct absolute path to the HTML file
        html_file = Path(__file__).parent.parent / "windows" / "pages" / name

        if not html_file.exists():
            raise FileNotFoundError(f"Page not found: {html_file}")

        # Convert path to QUrl
        file_url = QUrl.fromLocalFile(str(html_file.resolve()))

        # Load the page
        web_view.load(file_url)

        return web_view