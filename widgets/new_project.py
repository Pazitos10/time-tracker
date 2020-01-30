#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from widgets.py_files.dialog_new_project import Ui_dialog_new_project
from state import State

class NewProject(QtWidgets.QDialog):

    def __init__(self, data_path=None, edit_mode=False, project_name=None):
        super(NewProject, self).__init__()
        self.ui = Ui_dialog_new_project()
        self.ui.setupUi(self)
        self.edit_mode = edit_mode
        self.project_name = project_name
        self.state = State(data_path)
        self.setups()

    def setups(self):
        # Setup UI
        if self.edit_mode and self.project_name:
            self.setWindowTitle("Edit project")
            self.ui.lineEdit.setText(self.project_name)
            self.ui.buttonBox.accepted.connect(self.edit_project)
        else:
            self.ui.buttonBox.accepted.connect(self.create_project)

    def create_project(self):
        # Creates a new project.
        project_name = self.ui.lineEdit.text()
        if len(project_name) > 0 and project_name != " ":
            self.state.add_project(project_name)

    def edit_project(self):
        # Edit/update the name of an existing project.
        old_name = self.project_name
        new_name = self.ui.lineEdit.text()
        self.state.update_project(old_name, new_name)