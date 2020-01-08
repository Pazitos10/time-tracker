from PyQt5 import QtWidgets
from widgets.py_files.dialog_new_project import Ui_dialog_new_project

class NewProject(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(NewProject, self).__init__(parent)
        self.parent = parent
        self.ui = Ui_dialog_new_project()
        self.ui.setupUi(self)
        self.setups()

    def setups(self):
        self.ui.buttonBox.accepted.connect(self.create_project)

    def create_project(self):
        #TODO: add validation and error messages
        project_name = self.ui.lineEdit.text()
        if len(project_name) > 0 and project_name != " ":
            print(f"creando projecto {project_name}")
            create_project(project_name)
