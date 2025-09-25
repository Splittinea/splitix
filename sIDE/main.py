#--- Framework Generators ---
from framework.core import Application
#----------------------------

#--- Views ---
from views.home import homeView
#-------------

# Entry point of the application
app = Application("sIDE")

# Load views
home_window = homeView()
app.add_window(home_window)

# Run the application
def main():
    app.clean()
    app.build()
    app.run()

if __name__ == "__main__":
    main()

