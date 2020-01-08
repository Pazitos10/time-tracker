from PyQt5 import QtWidgets
from widgets.py_files.widget_projects_tab import Ui_widget_projects_tab

from widgets.py_files.list_item_widget import Ui_list_item_widget
#from widgets.py_files.dialog_new_project import Ui_dialog_new_project
from widgets.py_files.dialog_report import Ui_dialog_report
from widgets.py_files.dialog_about import Ui_dialog_about
from widgets.py_files.dialog_remove_project import Ui_dialog_remove
from widgets.py_files.dialog_create_data_file import Ui_dialog_create_data_file
from widgets.new_project import NewProject
from time_tracker import load_data, save_data, create_project

class ProjectsTab(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(ProjectsTab, self).__init__(parent)
        self.parent = parent
        self.ui = Ui_widget_projects_tab()
        self.ui.setupUi(self)
        self.setups()

    def setups(self):
        self.ui.push_btn_new_project.clicked.connect(lambda: self.open_dialog(Ui_dialog_new_project))
        self.ui.push_btn_new_project.clicked.connect(lambda: NewProject().exec())
        #self.ui.action_about.triggered.connect(lambda: self.open_dialog(Ui_dialog_about))
        #self.ui.action_new.triggered.connect(lambda: self.open_dialog(Ui_dialog_create_data_file))
        self.data = load_data('data.json')
        if not self.data:
            self.open_dialog(Ui_dialog_new_project)
            self.data = create_project(project)