from windows_ui import show_main_window 
import importlib

windows_ui = importlib.import_module("windows_ui")
windows_ui.show_main_window()

if __name__ == "__main__":
    show_main_window()
