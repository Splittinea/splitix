# DevTools.py
# Provides debugging tools

class DebugTools :
    # Turn that off in production, show debugging messages
    DEBUG_MODE = True

    @staticmethod
    def log(warning_level = "info", infos = "") :
       wl = warning_level.upper()

       #Prints logs infos in the format [LEVEL] : Message

       print(f"[{wl}] : {infos}")