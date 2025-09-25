# sIDE/framework/visuals/windows.py

import os

#--- Framework Generators ---
from framework.parsers.htmlParser import render_html
from framework.parsers.cssParser import render_css
from framework.parsers.jsParser import render_js
#----------------------------

class Window:
    """
    A window is a container for various UI elements.
    """

    def __init__(self, title="Untitled", w=800, h=600, is_home=True):
        self.title = title
        self.width = w
        self.height = h
        self.elements = []
        self.is_home = is_home

    def add_element(self, element):
        self.elements.append(element)

    def render(self):
        print(f"Rendering window: {self.title} ({self.width}x{self.height})")
        
        """
        Generates the HTML, JS, and CSS files for the window
        Packages them into a folder named after the window title
        Then, places it in the sIDE/pages folder
        """

        # Ensures the output dir exists
        output_dir = os.path.join(os.getcwd(), "pages")
        os.makedirs(output_dir, exist_ok=True)

        # Package creation
        folderName = self.title.replace(" ", "_").lower() # Text formatting into a valid folder name
        window_dir = os.path.join(output_dir, folderName)

        # Render the files
        render_html(self, output_dir=window_dir)
        render_css(self, output_dir=window_dir)
        render_js(self, output_dir=window_dir)