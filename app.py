from PyQt5 import QtGui, QtWidgets
from widgets.py_files.main import Ui_MainWindow
from widgets.projects_tab import ProjectsTab
from widgets.sessions_tab import SessionsTab
from widgets.py_files.dialog_create_data_file import Ui_dialog_create_data_file
from widgets.py_files.dialog_about import Ui_dialog_about
from utils import open_dialog
from time_tracker import load_data
from state import State

class App(QtWidgets.QMainWindow):
    """docstring for Principal"""
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tab_widget = QtWidgets.QTabWidget()
        self.ui.verticalLayout.addWidget(self.ui.tab_widget)
        self.ui.action_about.triggered.connect(lambda: open_dialog(Ui_dialog_about))
        self.ui.action_new.triggered.connect(lambda: open_dialog(Ui_dialog_create_data_file))
        self.ui.tab_widget.addTab(ProjectsTab(self), "Projects")
        self.ui.tab_widget.addTab(SessionsTab(self), "Sessions")
        self.ui.tab_widget.currentChanged.connect(lambda: self.ui.tab_widget.currentWidget().tab_changed())     
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = App()
    MainWindow.show()
    sys.exit(app.exec_())
