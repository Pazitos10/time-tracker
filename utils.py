from PyQt5 import QtWidgets

def open_dialog(ui_dialog):
    dialog = QtWidgets.QDialog()
    dialog.ui = ui_dialog()
    dialog.ui.setupUi(dialog)
    dialog.exec()

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