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
        self.state = State('data.json')
        self.setups()

    def setups(self):
        self.ui.push_btn_start_stop.clicked.connect(self.start_stop_session)
        self.ui.projects_combo_box.clear()
        project_names = self.state.get_project_names()
        self.ui.projects_combo_box.addItems(project_names)
        self.ui.projects_combo_box.currentIndexChanged.connect(self.combobox_project_changed)
        self.toggle_btn_title()

    def toggle_btn_title(self):
        project_name = self.ui.projects_combo_box.currentText()
        ongoing = self.state.are_there_ongoing_sessions(project_name)
        print(ongoing)
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
        #self.ui.label_time_spent_description.setVisible(not ongoing)
    
    def tab_changed(self):
        self.set_last_session_timedelta()

    def combobox_project_changed(self):
        self.set_last_session_timedelta()
        self.toggle_btn_title()