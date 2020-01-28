import os
import json
from PyQt5 import QtWidgets

def open_dialog(ui_dialog):
    dialog = QtWidgets.QDialog()
    dialog.ui = ui_dialog()
    dialog.ui.setupUi(dialog)
    dialog.exec()

def get_data_path():
    path = "settings.json"
    if os.path.exists(path):
        f = open(path, "r")
        settings = json.loads(f.read())
        f.close()
        return settings.get("data_path") 
    else:
        return "./data.json"

def set_data_path(path):
    settings = {"data_path": path}
    with open("settings.json", "w+") as f:
        json.dump(settings, f)

def format_timestamp(timestamp):
    if "," in timestamp:
        days = timestamp.split(",")[0]
        hms = timestamp.split(",")[1]
        hms = hms.split(".")[0]
        return f"{days}, {hms}", "48"
    else:
        if "." in timestamp:
            timestamp = timestamp.split(".")[0]    
        return timestamp, "60"

def get_project_index(data, project_name):
    res = -1
    for idx, p in enumerate(data["projects"]):
        if p["project_name"] == project_name:
            res = idx
    return res