#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from widgets.py_files.widget_projects_tab import Ui_widget_projects_tab
from widgets.py_files.list_item_widget import Ui_list_item_widget
from widgets.new_project import NewProject
from widgets.remove_project import RemoveProject
from state import State

class ProjectsTab(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(ProjectsTab, self).__init__(parent)
        self.parent = parent
        self.ui = Ui_widget_projects_tab()
        self.ui.setupUi(self)
        self.state = State(self.parent.data_path)
        self.state.add_listener(self)
        self.ui.push_btn_new_project.clicked.connect(lambda: NewProject().exec())

    def get_list_item_widget(self, project_name):
        # Returns a list item widget of a specific project. 
        widget = QtWidgets.QWidget()
        ui = Ui_list_item_widget()
        ui.setupUi(widget)
        ui.project_name_label.setText(project_name)
        ui.push_btn_edit.clicked.connect(lambda: self.open_edit_project_dialog(project_name))
        ui.push_btn_remove.clicked.connect(lambda: self.open_remove_project_dialog(project_name))
        return widget

    def open_edit_project_dialog(self, project_name):
        # Displays a QDialog to create/edit a new project.
        NewProject(data_path=self.parent.data_path, edit_mode=True, project_name=project_name).exec()

    def open_remove_project_dialog(self, project_name):
        # Displays a QDialog to remove a project.
        RemoveProject(data_path=self.parent.data_path, project_name=project_name).exec()

    def add_item_to_list(self, project_name):
        # Adds a list item widget with a new project data.
        list_item_widget = self.get_list_item_widget(project_name)
        item = QtWidgets.QListWidgetItem()
        item.setSizeHint(list_item_widget.sizeHint())
        self.ui.projects_list_widget.addItem(item)
        self.ui.projects_list_widget.setItemWidget(item, list_item_widget)

    def update_data(self, data):
        # Triggers a UI refresh with new/updated data
        self.ui.projects_list_widget.clear()
        project_names = self.state.get_project_names()
        for idx, project_name in enumerate(project_names):
            self.add_item_to_list(project_name)

    def update_data_path(self, data_path):
        self.state.update_data_path(data_path)

    def tab_changed(self):
        # Executed when the user switch tabs en the main widget.
        pass