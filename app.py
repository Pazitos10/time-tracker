#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from PyQt5 import QtWidgets

from widgets.py_files.main import Ui_MainWindow
from widgets.projects_tab import ProjectsTab
from widgets.sessions_tab import SessionsTab
from widgets.py_files.dialog_about import Ui_dialog_about
from widgets.py_files.widget_options_menu import Ui_widget_options_menu
from widgets.dialog_create_data_file import DialogCreateDataFile
from utils import open_dialog, get_data_path, set_data_path, is_valid_file
from reportingtools import reportutils


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.data_path = get_data_path()
        self.tabs = []
        self.options_menu_widget = None
        self.tab_widget = None
        self.setups()

    def setups(self):
        # Setup UI
        self.ui.action_about.triggered.connect(lambda: open_dialog(Ui_dialog_about))
        self.ui.action_new.triggered.connect(lambda: DialogCreateDataFile(parent=self).exec())
        self.ui.action_open.triggered.connect(self.open_existing_file)
        self.ui.action_close.triggered.connect(self.close_current_file)
        self.ui.action_exit.triggered.connect(self.close_app)
        self.ui.actionProjects_Chart.triggered.connect(self.make_projects_chart)
        self.ui.actionTime_Series_Chart.triggered.connect(self.make_timeseries_chart)
        if self.data_path == "" or not os.path.exists(self.data_path):
            self.setup_options_menu()
            self.ui.action_close.setEnabled(False)
        else:
            self.setup_tabs()
            self.ui.action_close.setEnabled(True)
        self.update_window_title()
    
    def setup_options_menu(self):
        if self.tab_widget:
            self.ui.verticalLayout.removeWidget(self.tab_widget)
            self.tab_widget.hide()
            self.ui.verticalLayout.update()
        if not self.options_menu_widget:
            self.options_menu_widget = QtWidgets.QWidget()
            self.options_menu_widget.ui = Ui_widget_options_menu()
            self.options_menu_widget.ui.setupUi(self.options_menu_widget)
            self.options_menu_widget.ui.push_button_create_file.clicked.connect(lambda: DialogCreateDataFile(parent=self).exec())
            self.options_menu_widget.ui.push_button_open_file.clicked.connect(self.open_existing_file)
        else:
            self.options_menu_widget.show()
        self.ui.verticalLayout.addWidget(self.options_menu_widget)

    def setup_tabs(self):
        if self.options_menu_widget:
            self.ui.verticalLayout.removeWidget(self.options_menu_widget)
            self.options_menu_widget.hide()
            self.ui.verticalLayout.update()
        if not self.tab_widget:
            self.tab_widget = QtWidgets.QTabWidget()
            self.tabs = [ProjectsTab(self), SessionsTab(self)]
            self.tab_widget.addTab(self.tabs[0], "Projects")
            self.tab_widget.addTab(self.tabs[1], "Sessions")
            self.tab_widget.currentChanged.connect(lambda: self.tab_widget.currentWidget().tab_changed())
        else:
            self.tab_widget.show()
        self.ui.verticalLayout.addWidget(self.tab_widget)

    def open_existing_file(self):
        # Display a QFileDialog to select the data file
        data_path = QtWidgets.QFileDialog.getOpenFileName(
            caption="Select your data file", 
            filter="*.json")[0]
        if data_path and is_valid_file(data_path):
            self.data_path = data_path
            set_data_path(self.data_path)
            self.update_data_path()
            self.setup_tabs()
        else:
            #launch invalid file format dialog.
            QtWidgets.QMessageBox.critical(self, 
                "Couldn't read the file", 
                "Please select a file with the valid format or create a new one."
            )

    def update_data_path(self):
        # Notify the tabs (children widgets) that the data file has changed.
        self.data_path = get_data_path()
        for tab in self.tabs:
            tab.update_data_path(self.data_path)
        self.update_window_title()

    def update_window_title(self):
        # Changes the window title according to the data file in use.
        settings_path = self.data_path.replace(os.path.expanduser("~"), "~")
        settings_path = "" if len(settings_path) == 0 else f"({settings_path})"
        self.setWindowTitle(f"Time Tracker {settings_path}")

    def close_current_file(self):
        self.setup_options_menu()
        self.data_path = ""
        self.update_window_title()
        set_data_path(self.data_path)
        #self.update_data_path()

    def make_projects_chart(self):
        """Creates a chart displaying the work done on each project. Automatically opens a browser window containing the chart."""
        df, _ = reportutils.dataframe_from_json(self.data_path)
        reportutils.plot_project_bar(df)

    def make_timeseries_chart(self):
        """
        Creates a chart displaying the work done over time. Automatically opens a browser window containing the chart.

        Default time frequency used is daily.
        Future plan: Provide a selector to daily/weekly/monthly/quarterly views.
        """
        _, projects = reportutils.dataframe_from_json(self.data_path)
        reportutils.plot_timeseries_bar(projects, 'D')

    def close_app(self):
        sys.exit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = App()
    MainWindow.show()
    sys.exit(app.exec_())
