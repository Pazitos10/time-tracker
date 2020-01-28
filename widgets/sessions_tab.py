from PyQt5 import QtWidgets
from widgets.py_files.widget_sessions_tab import Ui_widget_sessions_tab
from utils import format_timestamp
from state import State

class SessionsTab(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(SessionsTab, self).__init__(parent)
        self.parent = parent
        self.ui = Ui_widget_sessions_tab()
        self.ui.setupUi(self)
        self.state = State(self.parent.data_path)
        self.setups()

    def setups(self):
        self.ui.push_btn_start_stop.clicked.connect(self.start_stop_session)
        self.update_projects_combo_box()
        self.ui.projects_combo_box.currentIndexChanged.connect(self.combobox_project_changed)
        self.toggle_btn_title()

    def update_projects_combo_box(self):
        self.ui.projects_combo_box.clear()
        project_names = self.state.get_project_names()
        self.ui.projects_combo_box.addItems(project_names)

    def toggle_btn_title(self):
        project_name = self.ui.projects_combo_box.currentText()
        ongoing = self.state.are_there_ongoing_sessions(project_name)
        btn_title = "Stop" if ongoing  else "Start"
        self.ui.push_btn_start_stop.setText(btn_title)
        self.toggle_labels(ongoing)

    def start_stop_session(self):
        project_name = self.ui.projects_combo_box.currentText()
        self.state.add_timestamp(project_name)
        self.toggle_btn_title()
        self.set_last_session_timedelta()

    def set_last_session_timedelta(self):
        project_name = self.ui.projects_combo_box.currentText()
        total = self.state.get_total_timedelta(project_name)
        timestamp, ongoing = self.state.get_last_session_timedelta(project_name)
        timestamp, font_size = format_timestamp(str(timestamp))
        self.ui.label_time_spent_value.setText(timestamp)
        self.ui.label_time_spent_value.setStyleSheet(f"font-size: {font_size}px")
        self.ui.label_total.setText(f"Total: {total}")
        self.toggle_labels(ongoing)

    def toggle_labels(self, ongoing):
        self.ui.label_ongoing.setVisible(ongoing)
        self.ui.frame_report.setVisible(not ongoing)
        self.ui.label_empty_data_file.setVisible(False)

    def show_label_empty_data_file(self):
        self.ui.label_ongoing.setVisible(False)
        self.ui.frame_report.setVisible(False)
        self.ui.label_empty_data_file.setVisible(True)
    
    def tab_changed(self):
        self.combobox_project_changed()

    def combobox_project_changed(self):
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