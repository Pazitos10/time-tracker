import os
import json
#import ipdb
from PyQt5 import QtGui, QtWidgets
from widgets.py_files.main import Ui_MainWindow
from widgets.py_files.list_item_widget import Ui_list_item_widget
#from widgets.py_files.dialog_new_project import Ui_dialog_new_project
from widgets.py_files.dialog_report import Ui_dialog_report
from widgets.py_files.dialog_about import Ui_dialog_about
from widgets.py_files.dialog_remove_project import Ui_dialog_remove
from widgets.py_files.dialog_create_data_file import Ui_dialog_create_data_file
from widgets.new_project import NewProject
from widgets.projects_tab import ProjectsTab
from widgets.sessions_tab import SessionsTab

from time_tracker import load_data, save_data, create_project

class App(QtWidgets.QMainWindow):
    """docstring for Principal"""
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # #self.ui.push_btn_new_project.clicked.connect(lambda: self.open_dialog(Ui_dialog_new_project))
        # self.ui.push_btn_new_project.clicked.connect(lambda: NewProject().exec())
        # self.ui.action_about.triggered.connect(lambda: self.open_dialog(Ui_dialog_about))
        # self.ui.action_new.triggered.connect(lambda: self.open_dialog(Ui_dialog_create_data_file))
        # self.data = load_data('data.json')
        # if not self.data:
        #     self.open_dialog(Ui_dialog_new_project)
        #     self.data = create_project(project)
        self.ui.tab_widget = QtWidgets.QTabWidget()
        self.ui.tab_widget.addTab(ProjectsTab(), "Projects")
        self.ui.tab_widget.addTab(SessionsTab(), "Sessions")
        self.ui.verticalLayout.addWidget(self.ui.tab_widget)

    def open_dialog(self, ui_dialog):
        dialog = QtWidgets.QDialog()
        dialog.ui = ui_dialog()
        dialog.ui.setupUi(dialog)
        dialog.exec()

    def get_list_item_widget(self, project_name):
        widget = QtWidgets.QWidget()
        ui = Ui_list_item_widget()
        ui.setupUi(widget)
        ui.project_name_label.setText(project_name)
        ui.push_btn_edit.clicked.connect(lambda: self.open_edit_project_dialog(project_name))
        ui.push_btn_remove.clicked.connect(lambda: self.open_remove_project_dialog(project_name))
        return widget

    def open_edit_project_dialog(self, project_name):
        dialog = QtWidgets.QDialog()
        dialog.ui = Ui_dialog_new_project()
        dialog.ui.setupUi(dialog)
        dialog.ui.lineEdit.setText(project_name)
        dialog.accepted.connect(lambda: self.edit_project(project_name, dialog.ui.lineEdit.text()))
        dialog.exec()
    
    def get_project_index(self, project_name):
        res = -1
        for idx, p in enumerate(self.data["projects"]):
            if p["project_name"] == project_name:
                res = idx
        return res

    def edit_project(self, old_name, new_name):
        idx = self.get_project_index(old_name)
        if idx >= 0:
            project_data = self.data["projects"][idx]
            project_data.update({"project_name": new_name})
            self.data["projects"].pop(idx)
            self.data["projects"].insert(idx, project_data)
            self.update_data(save=True)


    def open_remove_project_dialog(self, project_name):
        print(f"Removing project {project_name}")
        dialog = QtWidgets.QDialog()
        dialog.ui = Ui_dialog_remove()
        dialog.ui.setupUi(dialog)
        dialog.accepted.connect(lambda: self.remove_project(project_name))
        dialog.exec()

    def remove_project(self, old_name):
        idx = self.get_project_index(old_name)
        if idx >= 0:
            self.data["projects"].pop(idx)
            self.update_data(save=True)

    def add_item_to_list(self, project_name):
        list_item_widget = self.get_list_item_widget(project_name)
        item = QtWidgets.QListWidgetItem()
        item.setSizeHint(list_item_widget.sizeHint())
        self.ui.projects_list_widget.addItem(item)
        self.ui.projects_list_widget.setItemWidget(item, list_item_widget)

    def update_data(self, save=False):
        self.ui.projects_list_widget.clear() #vaciamos la lista
        #ipdb.set_trace()
        self.ui.projects_combo_box.clear()
        project_names = [p["project_name"] for p in self.data["projects"]]
        self.ui.projects_combo_box.addItems(project_names)
        for idx, project_name in enumerate(project_names):
            self.add_item_to_list(project_name)
        if save: 
            save_data(self.data, 'data.json')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = App()
    MainWindow.show()
    sys.exit(app.exec_())
