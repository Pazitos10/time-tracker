#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import os
from PyQt5 import QtWidgets, QtCore
from widgets.py_files.dialog_create_data_file import Ui_dialog_create_data_file
from widgets.py_files.dialog_file_exist import Ui_dialog_file_exist
from utils import set_data_path
from state import State

class DialogCreateDataFile(QtWidgets.QDialog):

    def __init__(self, parent=None, filename="data", directory=None):
        super(DialogCreateDataFile, self).__init__()
        self.ui = Ui_dialog_create_data_file()
        self.ui.setupUi(self)
        self.parent = parent
        self.filename = filename
        self.directory = directory
        self.state = None
        self.setups()

    def setups(self):
        # Setup UI
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        #self.toggle_close_button_state()
        self.ui.label_directory_not_selected.hide()
        self.ui.push_btn_directory_selector.clicked.connect(self.open_file_selector)
        self.ui.push_btn_save.clicked.connect(self.create_data_file)

    def open_file_selector(self):
        # Displays a QFileDialog to select a directory
        self.directory = QtWidgets.QFileDialog.getExistingDirectory(
            self,
            "Select a directory",
            os.path.expanduser("~"),
            QtWidgets.QFileDialog.ShowDirsOnly
        )
        if len(self.directory) > 0:
            self.ui.label_selected_directory.setText(self.directory)

    def create_empty_data_file(self, filename):
        # Creates an empty JSON file with a data structure template 
        data = {"projects": []}
        with open(filename, "w+") as f:
            json.dump(data, f)

    def override_confirmed(self):
        # Creates an empty data file overriding an existing one.
        self.create_empty_data_file(self.filename)
        self.state = State(self.filename)
        set_data_path(self.filename)
        self.parent.update_data_path()
        self.close()

    def create_data_file(self):
        # Creates a new data file.
        self.filename = self.ui.line_edit_filename.text()
        if self.directory is not None:
            self.ui.label_directory_not_selected.hide()
            #self.toggle_close_button_state()
            self.filename = f"{self.directory}/{self.filename}.json"
            if os.path.exists(self.filename):
                dialog_file_exist = QtWidgets.QDialog()
                dialog_file_exist.ui = Ui_dialog_file_exist()
                dialog_file_exist.ui.setupUi(dialog_file_exist)
                dialog_file_exist.accepted.connect(self.override_confirmed)
                dialog_file_exist.exec()
            else:
                self.override_confirmed()
        else:
            self.ui.label_directory_not_selected.show()

    def toggle_close_button_state(self):
        if not self.directory:
            self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        else:
            self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, True)
