# sIDE - main file
# This file serves as the entry point for the sIDE application.

import os
from PySide6.QtWidgets import QApplication

#Home view
from windows.homeScreen import HomeScreen



# Ensures smooth zooming of images
os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"

def main() :
	print("Starting IDE")

	app = QApplication([])

	# Create the main window
	window = HomeScreen()
	window.showMaximized()

	# Start the application event loop
	app.exec()


if __name__ == "__main__":
	main()