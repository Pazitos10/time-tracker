import os
from PyQt5 import QtGui, QtWidgets
from widgets.py_files.main import Ui_MainWindow
from widgets.projects_tab import ProjectsTab
from widgets.sessions_tab import SessionsTab
from widgets.py_files.dialog_create_data_file import Ui_dialog_create_data_file
from widgets.py_files.dialog_about import Ui_dialog_about
from widgets.dialog_create_data_file import DialogCreateDataFile
from utils import open_dialog, get_data_path, set_data_path
from time_tracker import load_data
from state import State

class App(QtWidgets.QMainWindow):
    """docstring for Principal"""
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.data_path = get_data_path()
        self.setups()

    def setups(self):
        self.ui.tab_widget = QtWidgets.QTabWidget()
        self.ui.verticalLayout.addWidget(self.ui.tab_widget)
        self.ui.action_about.triggered.connect(lambda: open_dialog(Ui_dialog_about))
        self.ui.action_new.triggered.connect(lambda: DialogCreateDataFile(parent=self).exec())
        self.ui.action_open.triggered.connect(self.open_existing_file)
        self.tabs = [ProjectsTab(self), SessionsTab(self)]
        self.ui.tab_widget.addTab(self.tabs[0], "Projects")
        self.ui.tab_widget.addTab(self.tabs[1], "Sessions")
        self.ui.tab_widget.currentChanged.connect(lambda: self.ui.tab_widget.currentWidget().tab_changed())
        self.update_window_title()

    def open_existing_file(self):
        data_path = QtWidgets.QFileDialog.getOpenFileName(
            caption="Select your data file", 
            filter="*.json")[0]
        if data_path:
            self.data_path = data_path
        set_data_path(self.data_path)
        self.update_data_path()

    def update_data_path(self):
        self.data_path = get_data_path()
        for tab in self.tabs:
            tab.update_data_path(self.data_path)
        self.update_window_title()

    def update_window_title(self):
        settings_path = self.data_path.replace(os.path.expanduser("~"), "~")
        self.setWindowTitle(f"Time Tracker ({settings_path})")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = App()
    MainWindow.show()
    sys.exit(app.exec_())
