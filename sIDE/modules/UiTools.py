# UiTools.py
# This module contains various UI tools and utilities for the sIDE application.

# Importation of the entire PySide6 module
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

# Each component will have its own class, with associated methods, events and such

# Unfold this arrow to reveal the ui classes
# region ComponentClasses
'''
GLOBAL CLASS : Every component will herit from this class
'''
class UIComponent :
    '''
    Base class for all UI components
    Contains common methods and properties for all components
    '''

    def __init__(self, widget) :
        self.widget = widget

    # Methods
    def setText(self, text: str) : # Defines the component's text (if applicable)
        if hasattr(self.widget, 'setText'):
            self.widget.setText(text)

    def setPlaceholder(self, text: str) : # Defines the component's placeholder text (if applicable)
        if hasattr(self.widget, 'setPlaceholderText'):
            self.widget.setPlaceholderText(text)

    def setStyle(self, style: str) : # Sets the style of the component using a CSS stylesheet
        self.widget.setStyleSheet(style)

    def setFixedSize(self, width: int, height: int) : # Sets the fixed size of the component
        self.widget.setFixedSize(width, height)

    '''
    SCROLL BARS, SLIDERS
    '''
    def setMaxValue(self, value: float) : # Sets the maximum value of the component (if applicable)
        if hasattr(self.widget, 'setMaximum'):
            self.widget.setMaximum(value)
    
    def setMinValue(self, value: float) : # Sets the minimum value of the component (if applicable)
        if hasattr(self.widget, 'setMinimum'):
            self.widget.setMinimum(value)

    def setValue(self, value: float) : # Sets the current value of the component (if applicable)
        if hasattr(self.widget, 'setValue'):
            self.widget.setValue(value)

    '''
    TABLES, LISTS
    '''
    def addItem(self, item: str, rowIndex : int = None, colIndex: int = None, index : int = None) : # Adds an item to the component, at a specific position (if applicable)
        if isinstance(self.widget, QTableWidget):
            if rowIndex is not None and colIndex is not None:
                self.widget.setItem(rowIndex, colIndex, QTableWidgetItem(item))
            else:
                raise ValueError("rowIndex and colIndex must be specified for Table")
        elif isinstance(self.widget, QListWidget):
            if index is not None:
                self.widget.insertItem(index, item)
            else:
                self.widget.addItem(item)
        elif isinstance(self.widget, QComboBox):
            if index is not None:
                self.widget.insertItem(index, item)
            else:
                self.widget.addItem(item)


    def removeItem(self, rowIndex: int = None, colIndex: int = None, index: int = None) : # Removes an item from the component (if applicable)
        if isinstance(self.widget, QTableWidget):
            if rowIndex is not None:
                self.widget.removeRow(rowIndex)
            else:
                raise ValueError("rowIndex must be specified for Table")
        elif isinstance(self.widget, QListWidget):
            if index is not None:
                item = self.widget.takeItem(index)
                del item
            else:
                raise ValueError("index must be specified for List")
        elif isinstance(self.widget, QComboBox):
            if index is not None:
                self.widget.removeItem(index)
            else:
                raise ValueError("index must be specified for DropdownList")

    '''
    COMPONENT CONTROLS
    '''
    def show(self) : # Shows the component
        self.widget.show()

    def hide(self) : # Hides the component
        self.widget.hide()

    def enable(self) : # Enables the component (if it was disabled)
        self.widget.setEnabled(True)
     
    def disable(self) : # Disables the component (grayed out, cannot be interacted with)
        self.widget.setEnabled(False)

    # Properties
    def isShown(self) -> bool : # Control boolean to check if the component is shown or not
        return self.widget.isVisible()

    def isHidden(self) -> bool : # Control boolean to check if the component is hidden or not
        return not self.widget.isVisible()

    def isEnabled(self) -> bool : # Control boolean to check if the component is enabled or not
        return self.widget.isEnabled()
    
    def isDisabled(self) -> bool : # Control boolean to check if the component is disabled or not
        return not self.widget.isEnabled()

    def isClickable(self) -> bool : # Control boolean to check if the component is clickable or not (if applicable)
        return hasattr(self.widget, 'clicked') or hasattr(self.widget, 'mousePressEvent')

    def isChecked(self) -> bool : # Control boolean to check if the component is checked or not (if applicable)
        return getattr(self.widget, 'isChecked', lambda: False)()

    # Events
    def onLeftClick(self, callback) : # Event triggered when the component is left-clicked (if applicable)
        self.widget.mousePressEvent = lambda event: callback() if event.button() == Qt.LeftButton else None

    def onRightClick(self, callback) : # Event triggered when the component is right-clicked (if applicable)
        self.widget.mousePressEvent = lambda event: callback() if event.button() == Qt.RightButton else None

    def onMiddleClick(self, callback) : # Event triggered when the component is middle-clicked (if applicable)
        self.widget.mousePressEvent = lambda event: callback() if event.button() == Qt.MiddleButton else None

    def onDoubleClick(self, callback) : # Event triggered when the component is double-clicked (if applicable)
        self.widget.mouseDoubleClickEvent = lambda event: callback()

    def onHover(self, callback) : # Event triggered when the component is hovered over (if applicable)
        if hasattr(self.widget, 'enterEvent'):
            self.widget.enterEvent = lambda event: callback()

    def onLeave(self, callback) : # Event triggered when the component is no longer hovered over (if applicable)
        if hasattr(self.widget, 'leaveEvent'):
            self.widget.leaveEvent = lambda event: callback()

    def onCheck(self, callback) : # Event triggered when the component is checked (if applicable)
        if hasattr(self.widget, 'stateChanged'):
            self.widget.stateChanged.connect(lambda state: callback(state == Qt.Checked))
    
    # Variables
    def getText(self) -> str : # Outputs the text content of the component (if applicable)
        if hasattr(self.widget, 'text'):
            return self.widget.text()
        return ""

    def getValue(self) -> str : # Outputs the value of the component (if applicable)
        if hasattr(self.widget, 'value'):
            return self.widget.value()
        return 0


'''
WINDOW PARAMETERS :
Regrouping all window related ui components
'''
# Unfold the arrow to show the classes
# region
class Window(UIComponent) :
    '''
    A window component, used to create a new window
    Can be interacted, moved, resized, minimized, maximized and closed
    Its title can be read and modified programmatically
    It holds other UI components
    '''
    def __init__(self) :
        super().__init__(QMainWindow())

    def setTitle(self, title: str) : # Sets the title of the window
        self.widget.setWindowTitle(title)

    def setIcon(self, icon_path: str) : # Sets the icon of the window
        self.widget.setWindowIcon(QIcon(icon_path))


class Layout(UIComponent) :
    '''
    A layout component, used to arrange other UI components in a specific way
    Can be vertical, horizontal, grid, or form layout
    Holds other UI components
    '''
    def __init__(self, layout_type: str = "vertical", parent = None) :
        if layout_type == "vertical":
            super().__init__(QVBoxLayout(parent))
        elif layout_type == "horizontal":
            super().__init__(QHBoxLayout(parent))
        elif layout_type == "grid":
            super().__init__(QGridLayout(parent))
        elif layout_type == "form":
            super().__init__(QFormLayout(parent))
        else:
            raise ValueError("Invalid layout type. Choose from 'vertical', 'horizontal', 'grid', or 'form'.")

    def addWidget(self, widget: UIComponent) : # Adds a widget to the layout
        self.widget.addWidget(widget.widget)

    def addLayout(self, layout: 'Layout') : # Adds a layout to the layout
        self.widget.addLayout(layout.widget)
# endregion


'''
TEXT ELEMENTS :
Regrouping all text-related UI components, such as labels and text boxes
'''
# Unfold the arrow to show the classes
# region
class Label(UIComponent) :
    '''
    Label : 
    A simple text label component.
    Cannot be clicked, nor interacted with.
    The text can be dynamicaly changed
    '''
    def __init__(self, text: str = "", parent = None) :
        super().__init__(QLabel(text, parent))


class TextBox(UIComponent) :
    '''
    A component used to input text
    Can be interacted, clicked, and text can be inputted
    Its contents can be read and modified programmatically
    The component can also be enabled or disabled (grayed out)
    '''
    def __init__(self, text: str = "", parent = None) :
        super().__init__(QLineEdit(text, parent))

    def clear(self) : # Clears the content of the text box
        self.widget.clear()

# endregion


'''
SELECTORS :
Regrouping all selector-related UI components, such as checkboxes, radio buttons and dropdowns
'''
# Unfold the arrow to show the classes
# region
class CheckBox(UIComponent) :
    '''
    A checkbox component, used to select or deselect an option
    Can be interacted, clicked, and checked or unchecked
    Its state can be read and modified programmatically
    The component can also be enabled or disabled (grayed out)
    Allows for multiple boxes to be checked at the same time
    '''
    def __init__(self, text: str = "", parent = None) :
        super().__init__(QCheckBox(text, parent))

class RadioButton(UIComponent) :
    '''
    A radio button component, used to select one option among a group
    Can be interacted, clicked, and selected or deselected
    Its state can be read and modified programmatically
    The component can also be enabled or disabled (grayed out)
    Only one button in a group can be selected at a time
    '''
    def __init__(self, text: str = "", parent = None) :
        super().__init__(QRadioButton(text, parent))

# endregion

'''
CONTAINERS :
Regrouping all container-related UI components, such as group boxes and tabs
'''
# Unfold the arrow to show the classes
# region

class Table(UIComponent) :
    '''
    Table :
    A component made of rows and columns to display data in a structured way
    '''

    def __init__(self, rows: int = 0, columns: int = 0, parent = None) :
        super().__init__(QTableWidget(rows, columns, parent))

class DropdownList(UIComponent) :
    '''
    Dropdown List :
    A component with entries, that can be selected from a dropdown menu
    '''

    def __init__(self, parent = None) :
        super().__init__(QComboBox(parent))

class List(UIComponent) :
    '''
    List :
    A component with entries, that can be selected from a list
    '''
    def __init__(self, parent = None) :
        super().__init__(QListWidget(parent))
# endregion
# endregion ComponentClasses

'''
DOCUMENT GENERATOR CLASS
'''
class Generator:
    """
    DOCUMENT GENERATOR CLASS

    This class generates HTML, CSS, and JS files from UiTools components.
    Each component has a unique ID for consistent referencing in HTML, CSS, and JS.
    """

    def __init__(self, components: list, output_dir: str = "sIDE/windows/pages"):
        """
        Initialize the generator.

        :param components: list of root components to generate (e.g., label1, textbox1, checkbox1)
        :param output_dir: output directory for the generated package
        """
        self.components = components
        self.output_dir = output_dir   # Output folder for the page package
        self.html_content = ""         # Stores HTML content
        self.css_content = ""          # Stores CSS content
        self.js_content = ""           # Stores JS content
        self.indent = "   "            # Indentation spaces for readability
        self.indent_level = 0          # Current indentation level
        self.component_ids = {}        # Stores generated unique IDs per component

    # ----------- ID GENERATION -----------
    def generate_id(self, component):
        """
        Generate a unique, readable ID for a component.
        Reuse the same ID for CSS and JS.
        """
        if component in self.component_ids:
            return self.component_ids[component]

        widget_type = type(component.widget).__name__
        # Count existing components of the same type to generate a new unique ID
        count = sum(1 for c in self.component_ids if type(c.widget).__name__ == widget_type) + 1
        unique_id = f"{widget_type}_{count}"
        self.component_ids[component] = unique_id
        return unique_id

    # ----------- HTML GENERATION -----------
    def generate_html(self):
        """
        Generate full HTML content from the root components list.
        Adds DOCTYPE, head, and body sections.
        """
        self.html_content += "<!DOCTYPE html>\n<html>\n<head>\n"
        self.indent_level += 1
        self.html_content += f"{self.indent*self.indent_level}<meta charset='UTF-8'>\n"
        self.html_content += f"{self.indent*self.indent_level}<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n"
        self.html_content += f"{self.indent*self.indent_level}<title>Generated UI</title>\n"
        self.html_content += f"{self.indent*self.indent_level}<link rel='stylesheet' href='styles.css'>\n"
        self.html_content += f"{self.indent*self.indent_level}<script src='script.js' defer></script>\n"
        self.indent_level -= 1
        self.html_content += "</head>\n<body>\n"
        self.indent_level += 1

        # Parse each root component
        for comp in self.components:
            self._html_component(comp)

        self.indent_level -= 1
        self.html_content += "</body>\n</html>"

    def _html_component(self, component):
        """
        Generate HTML for a single component instance.
        Supports QLabel, QLineEdit, QCheckBox, QRadioButton.
        """
        element_id = self.generate_id(component)
        space = self.indent * self.indent_level

        # Map component type to proper HTML representation
        if isinstance(component.widget, QLabel):
            # Label -> <span>
            self.html_content += f"{space}<span id='{element_id}'>{component.getText()}</span>\n"
        elif isinstance(component.widget, QLineEdit):
            # TextBox -> <input type='text'>
            value = component.getText() or ""
            self.html_content += f"{space}<input type='text' id='{element_id}' value='{value}' />\n"
        elif isinstance(component.widget, QCheckBox):
            # CheckBox -> <input type='checkbox'> with label text
            checked = " checked" if component.isChecked() else ""
            self.html_content += f"{space}<input type='checkbox' id='{element_id}'{checked} /> {component.getText()}\n"
        elif isinstance(component.widget, QRadioButton):
            # RadioButton -> <input type='radio'> with label text
            checked = " checked" if component.isChecked() else ""
            self.html_content += f"{space}<input type='radio' id='{element_id}'{checked} /> {component.getText()}\n"
        else:
            # Fallback for unknown widgets -> <div>
            self.html_content += f"{space}<div id='{element_id}'></div>\n"

    # ----------- CSS GENERATION -----------
    def generate_css(self):
        """
        Generate CSS by collecting style sheets from all components.
        Styles are applied based on unique component IDs.
        """
        self.css_content = "/* Generated CSS */\n"
        for comp in self.components:
            element_id = self.generate_id(comp)
            style = comp.widget.styleSheet()
            if style:
                self.css_content += f"/* Styles for {element_id} */\n#{element_id} {{ {style} }}\n"

    # ----------- JS GENERATION -----------
    def generate_js(self):
        """
        Generate JavaScript event bindings for clickable components.
        Currently supports simple click events.
        """
        self.js_content = "// Generated JavaScript\n"
        for comp in self.components:
            element_id = self.generate_id(comp)
            if comp.isClickable():
                self.js_content += (
                    f"document.getElementById('{element_id}').addEventListener('click', function() {{\n"
                    f"{self.indent}// TODO: handle click\n"
                    "});\n"
                )

    # ----------- PACKAGE EXPORT -----------
    def generate_package(self, package_name: str):
        """
        Generate a complete package with HTML, CSS, and JS files.
        Files are named after the package and stored in a dedicated folder.
        """
        import os
        base_path = os.path.join(self.output_dir, package_name)
        os.makedirs(base_path, exist_ok=True)

        self.generate_html()
        self.generate_css()
        self.generate_js()

        # Write files
        with open(os.path.join(base_path, f"{package_name}.html"), "w", encoding="utf-8") as f:
            f.write(self.html_content)
        with open(os.path.join(base_path, "styles.css"), "w", encoding="utf-8") as f:
            f.write(self.css_content)
        with open(os.path.join(base_path, "script.js"), "w", encoding="utf-8") as f:
            f.write(self.js_content)


class Application:
    """
    Splitix Application
    Entry point of the framework. 
    Holds the root layout and generates the HTML/CSS/JS package.
    """

    def __init__(self, name: str = "App", output_dir: str = "sIDE/windows/pages"):
        self.name = name
        self.output_dir = output_dir
        self.root_layout = None
        self.generator = None

    def set_layout(self, layout):
        """Define the root layout of the application"""
        self.root_layout = layout

    def build(self):
        """Generate HTML, CSS, and JS from the root layout"""
        if not self.root_layout:
            raise ValueError("No root layout defined. Use set_layout() first.")
        
        from UiTools import Generator
        self.generator = Generator([self.root_layout], output_dir=self.output_dir)
        self.generator.generate_package(self.name)

    def preview(self):
        """Open the generated HTML in the default web browser"""
        import webbrowser, os
        html_file = os.path.join(self.output_dir, self.name, f"{self.name}.html")
        if os.path.exists(html_file):
            webbrowser.open(f"file://{os.path.abspath(html_file)}")
        else:
            print("[ERROR] Build first with .build() before preview().")

