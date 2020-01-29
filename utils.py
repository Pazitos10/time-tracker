import os
import json
from PyQt5 import QtWidgets

def open_dialog(ui_dialog):
    # Generic function to display a QDialog.
    dialog = QtWidgets.QDialog()
    dialog.ui = ui_dialog()
    dialog.ui.setupUi(dialog)
    dialog.exec()

def get_data_path():
    # Reads the settings file to get the data file path
    path = "settings.json"
    if os.path.exists(path):
        f = open(path, "r")
        settings = json.loads(f.read())
        f.close()
        return settings.get("data_path") 
    else:
        return "./data.json"

def set_data_path(path):
    # Writes the settings file with a new data file path
    settings = {"data_path": path}
    with open("settings.json", "w+") as f:
        json.dump(settings, f)

def format_timestamp(timestamp):
    # Returns a formatted timestamp and the font size for
    # it to be displayed.
    if "," in timestamp:
        days = timestamp.split(",")[0]
        hms = timestamp.split(",")[1]
        hms = hms.split(".")[0]
        return f"{days}, {hms}", "48"
    else:
        if "." in timestamp:
            timestamp = timestamp.split(".")[0]    
        return timestamp, "60"