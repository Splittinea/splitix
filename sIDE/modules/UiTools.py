# UiTools.py
# Provides ui utilities, to simplify PySide6 syntaxes

from PySide6.QtWidgets import QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout

class components :

    @staticmethod
    def button(type, parameters) :

        '''
        The button's id is defined as a variable :
        button1 = components.button(type, parameters list)

        All the colors that may be defined here are written in HEXADECIMAL

        Accepts parameters such as :
        -> image
        -> imagePosition (before or after the text)
        -> displayText
        -> textFont
        -> textColor
        -> backgroundColor
        -> shape
        -> size
        '''

        pass

    @staticmethod
    def label(parameters) :
        pass

    @staticmethod
    def textbox(parameters):
        pass

    @staticmethod
    def vContainer(parameters) :
        pass

    @staticmethod
    def hContainer(parameters) :
        pass

    @staticmethod
    def table(parameters):
        pass

    @staticmethod
    def window(parameters):
        pass

    @staticmethod
    def onClick() :
        pass
    #TODO : Add more functions here :