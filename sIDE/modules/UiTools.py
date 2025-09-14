# UiTools.py
# This module contains various UI tools and utilities for the sIDE application.

# Importation of the entire PySide6 module
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

# Each component will have its own class, with associated methods, events and such


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
        # QTableWidget
        if hasattr(self.widget, 'setItem') and rowIndex is not None and colIndex is not None:
            self.widget.setItem(rowIndex, colIndex, QTableWidgetItem(item))
    
        # QListWidget
        elif hasattr(self.widget, 'addItem') and isinstance(self.widget, QListWidget):
            if index is not None:
                self.widget.insertItem(index, item)
            else:
                self.widget.addItem(item)
    
        # QComboBox
        elif hasattr(self.widget, 'addItem') and isinstance(self.widget, QComboBox):
            if index is not None:
                self.widget.insertItem(index, item)
            else:
                self.widget.addItem(item)


    def removeItem(self, rowIndex: int = None, colIndex: int = None, index: int = None) : # Removes an item from the component (if applicable)
        # QTableWidget
        if hasattr(self.widget, 'removeRow') and rowIndex is not None:
            self.widget.removeRow(rowIndex)
    
        # QListWidget
        elif isinstance(self.widget, QListWidget):
            if index is not None:
                item = self.widget.takeItem(index)
                del item  # optional, to remove reference
            else:
                raise ValueError("index must be specified for QListWidget")
    
        # QComboBox
        elif isinstance(self.widget, QComboBox):
            if index is not None:
                self.widget.removeItem(index)
            else:
                raise ValueError("index must be specified for QComboBox")

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

