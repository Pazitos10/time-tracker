import os
import json

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
        self.state = State('data.json')
        self.state.add_listener(self)
        self.ui.push_btn_new_project.clicked.connect(lambda: NewProject().exec())

    def get_list_item_widget(self, project_name):
        widget = QtWidgets.QWidget()
        ui = Ui_list_item_widget()
        ui.setupUi(widget)
        ui.project_name_label.setText(project_name)
        ui.push_btn_edit.clicked.connect(lambda: self.open_edit_project_dialog(project_name))
        ui.push_btn_remove.clicked.connect(lambda: self.open_remove_project_dialog(project_name))
        return widget

    def open_edit_project_dialog(self, project_name):
        NewProject(edit_mode=True, project_name=project_name).exec()

    def open_remove_project_dialog(self, project_name):
        RemoveProject(project_name).exec()

    def add_item_to_list(self, project_name):
        list_item_widget = self.get_list_item_widget(project_name)
        item = QtWidgets.QListWidgetItem()
        item.setSizeHint(list_item_widget.sizeHint())
        self.ui.projects_list_widget.addItem(item)
        self.ui.projects_list_widget.setItemWidget(item, list_item_widget)

    def update_data(self, data):
        self.data = data
        self.ui.projects_list_widget.clear() #vaciamos la lista
        project_names = self.state.get_project_names()
        for idx, project_name in enumerate(project_names):
            self.add_item_to_list(project_name)

    def tab_changed(self):
        print("hola desde projects tab!")
        #pass