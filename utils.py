#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import json
from PyQt5 import QtWidgets

appname = "time-tracker"
SETTINGS_PATH = f"./settings.json"
PROJECT_TEMPLATE={"projects": []}
SETTINGS_TEMPLATE={"data_path": ""}

def open_dialog(ui_dialog):
    # Generic function to display a QDialog.
    dialog = QtWidgets.QDialog()
    dialog.ui = ui_dialog()
    dialog.ui.setupUi(dialog)
    dialog.exec()

def read_json(path):
    try:
        f = open(path, "r")
        content = json.loads(f.read())
        f.close()
        return content
    except FileNotFoundError:
        os.makedirs(USER_CONFIG_DIR, exist_ok=True)
        open(path, "r").close()
        if "settings.json" in path:
            return SETTINGS_TEMPLATE
        else:
            return PROJECT_TEMPLATE


def get_data_path():
    # Reads the settings file to get the data file path
    settings = read_json(SETTINGS_PATH)
    if "data_path" in settings.keys():
        return settings.get("data_path") 
    else:
        set_data_path("") # resets data_path to ""
        return ""

def is_valid_file(path):
    if os.path.exists(path):
        data = read_json(path)
        return "projects" in data.keys() and type(data.get("projects")) == list
    else:
        return False

def set_data_path(path):
    # Writes the settings file with a new data file path
    settings = {"data_path": path}
    with open(SETTINGS_PATH, "w+") as f:
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