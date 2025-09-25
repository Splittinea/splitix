# sIDE/framework/modules/textFormat.py
# Simple class for text formatting inside print statements

from colorama import init, Fore, Style
import sys

init(autoreset=True, convert=True)

def log(color: str, message: str):
    colors = {
        "black": Fore.BLACK,
        "red": Fore.RED,
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "blue": Fore.BLUE,
        "magenta": Fore.MAGENTA,
        "cyan": Fore.CYAN,
        "white": Fore.WHITE
    }
    color_code = colors.get(color.lower(), Fore.RESET)
    print(f"{color_code}{message}{Style.RESET_ALL}")
    
def nextLine():
    """
    Prints a newline to the console.
    """
    print("\n")
