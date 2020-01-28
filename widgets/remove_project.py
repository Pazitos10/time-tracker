from PyQt5 import QtWidgets
from widgets.py_files.dialog_remove_project import Ui_dialog_remove_project
from utils import get_project_index
from state import State

class RemoveProject(QtWidgets.QDialog):

    def __init__(self, parent=None, project_name=None):
        super(RemoveProject, self).__init__()
        self.parent = parent
        self.ui = Ui_dialog_remove_project()
        self.ui.setupUi(self)
        self.project_name = project_name
        self.state = State(self.parent.data_path)
        self.setups()

    def setups(self):
        self.ui.buttonBox.accepted.connect(self.remove_project)

    def remove_project(self):
        print(self.project_name)
        self.state.remove_project(self.project_name)