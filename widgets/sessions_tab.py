from PyQt5 import QtWidgets
from widgets.py_files.widget_sessions_tab import Ui_widget_sessions_tab

class SessionsTab(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(SessionsTab, self).__init__(parent)
        self.parent = parent
        self.ui = Ui_widget_sessions_tab()
        self.ui.setupUi(self)
        self.setups()

    def setups(self):
        pass