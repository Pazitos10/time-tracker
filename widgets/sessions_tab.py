from PyQt5 import QtWidgets
from widgets.py_files.widget_sessions_tab import Ui_widget_sessions_tab
from utils import format_timestamp
from state import State

class SessionsTab(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(SessionsTab, self).__init__(parent)
        self.parent = parent
        self.current_index = 0
        self.ui = Ui_widget_sessions_tab()
        self.ui.setupUi(self)
        self.state = State(self.parent.data_path)
        self.state.add_listener(self)
        self.setups()

    def setups(self):
        # Setup UI
        self.ui.push_btn_start_stop.clicked.connect(self.start_stop_session)
        self.update_projects_combo_box()
        self.ui.projects_combo_box.currentIndexChanged.connect(self.combo_box_project_changed)
        self.toggle_btn_title()

    def update_projects_combo_box(self):
        # Updates the project combo box with new/updated project names.
        self.ui.projects_combo_box.clear()
        project_names = self.state.get_project_names()
        self.ui.projects_combo_box.addItems(project_names)
        self.ui.projects_combo_box.setCurrentIndex(self.current_index)

    def toggle_btn_title(self):
        # Verifies if the selected project has an ongoing working session and 
        # toggles the Start/Stop button's title accordingly.
        project_name = self.ui.projects_combo_box.currentText()
        ongoing = self.state.has_ongoing_sessions(project_name)
        btn_title = "Stop" if ongoing  else "Start"
        self.ui.push_btn_start_stop.setText(btn_title)
        self.toggle_labels(ongoing)

    def start_stop_session(self):
        # Starts/Stops a working session for the selected project.
        project_name = self.ui.projects_combo_box.currentText()
        self.current_index = self.ui.projects_combo_box.currentIndex()
        self.state.add_timestamp(project_name)
        self.toggle_btn_title()
        self.set_last_session_timedelta()

    def set_last_session_timedelta(self):
        # Display the last session and total timedelta for the selected project.
        project_name = self.ui.projects_combo_box.currentText()
        if len(project_name) == 0: # when a task is removed currentText() returns ''
            self.current_index = 0
            self.ui.projects_combo_box.setCurrentIndex(self.current_index)
            project_name = self.ui.projects_combo_box.currentText()

        total = self.state.get_total_timedelta(project_name)
        timestamp, ongoing = self.state.get_last_session_timedelta(project_name)
        timestamp, font_size = format_timestamp(str(timestamp))
        self.ui.label_time_spent_value.setText(timestamp)
        self.ui.label_time_spent_value.setStyleSheet(f"font-size: {font_size}px")
        self.ui.label_total.setText(f"Total: {total}")
        self.toggle_labels(ongoing)

    def toggle_labels(self, ongoing):
        # Show/Hide labels depending of the last working session state of a project (finished/ongoing).
        self.ui.label_ongoing.setVisible(ongoing)
        self.ui.frame_report.setVisible(not ongoing)
        self.ui.label_empty_data_file.setVisible(False)

    def show_label_empty_data_file(self):
        # Shows a label to inform the user that the current file has no projects.
        self.ui.label_ongoing.setVisible(False)
        self.ui.frame_report.setVisible(False)
        self.ui.label_empty_data_file.setVisible(True)
    
    def tab_changed(self):
        # Executed when the user switch tabs en the main widget.
        self.combo_box_project_changed()

    def combo_box_project_changed(self):
        # Updates the UI with the timedeltas for the selected project. 
        # Disables the Start/Stop button when there are no projects in the data file,
        # enables it otherwise.
        if self.ui.projects_combo_box.count() > 0:
            self.set_last_session_timedelta()
            self.toggle_btn_title()
            self.ui.push_btn_start_stop.setEnabled(True)
        else:
            self.show_label_empty_data_file()
            self.ui.push_btn_start_stop.setEnabled(False)

    def update_data_path(self, data_path):
        self.state.update_data_path(data_path)
        self.update_projects_combo_box()

    def update_data(self, data):
        # Triggers a UI refresh with new/updated data.
        self.update_projects_combo_box()