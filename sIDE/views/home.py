# views/home.py
# The home view of the application

#--- Framework Generators ---
from framework.visuals.windows import Window
#----------------------------

#--- Framework Modules ---
from framework.modules.textFormat import log, nextLine
#----------------------------

# Sample window

def homeView() :
    # Sample window
    home = Window(title = "Home", w=1920, h=1080, is_home=True)

    return home