# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/ui/widget_sessions_tab.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_widget_sessions_tab(object):
    def setupUi(self, widget_sessions_tab):
        widget_sessions_tab.setObjectName("widget_sessions_tab")
        widget_sessions_tab.resize(662, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(widget_sessions_tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(widget_sessions_tab)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.projects_combo_box = QtWidgets.QComboBox(widget_sessions_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.projects_combo_box.sizePolicy().hasHeightForWidth())
        self.projects_combo_box.setSizePolicy(sizePolicy)
        self.projects_combo_box.setObjectName("projects_combo_box")
        self.horizontalLayout.addWidget(self.projects_combo_box)
        self.push_btn_start_stop = QtWidgets.QPushButton(widget_sessions_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_btn_start_stop.sizePolicy().hasHeightForWidth())
        self.push_btn_start_stop.setSizePolicy(sizePolicy)
        self.push_btn_start_stop.setObjectName("push_btn_start_stop")
        self.horizontalLayout.addWidget(self.push_btn_start_stop)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        self.label_time_spent_description = QtWidgets.QLabel(widget_sessions_tab)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_time_spent_description.setFont(font)
        self.label_time_spent_description.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_time_spent_description.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time_spent_description.setObjectName("label_time_spent_description")
        self.verticalLayout.addWidget(self.label_time_spent_description)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem3)
        self.label_time_spent_value = QtWidgets.QLabel(widget_sessions_tab)
        font = QtGui.QFont()
        font.setPointSize(64)
        self.label_time_spent_value.setFont(font)
        self.label_time_spent_value.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_time_spent_value.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time_spent_value.setObjectName("label_time_spent_value")
        self.verticalLayout.addWidget(self.label_time_spent_value)
        spacerItem4 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)

        self.retranslateUi(widget_sessions_tab)
        QtCore.QMetaObject.connectSlotsByName(widget_sessions_tab)

    def retranslateUi(self, widget_sessions_tab):
        _translate = QtCore.QCoreApplication.translate
        widget_sessions_tab.setWindowTitle(_translate("widget_sessions_tab", "widget_sessions_tab"))
        self.label.setText(_translate("widget_sessions_tab", "Choose a project to start/stop a working session:"))
        self.push_btn_start_stop.setText(_translate("widget_sessions_tab", "Start/Stop"))
        self.label_time_spent_description.setText(_translate("widget_sessions_tab", "Time spent working in the current session"))
        self.label_time_spent_value.setText(_translate("widget_sessions_tab", "00:20:45"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget_sessions_tab = QtWidgets.QWidget()
    ui = Ui_widget_sessions_tab()
    ui.setupUi(widget_sessions_tab)
    widget_sessions_tab.show()
    sys.exit(app.exec_())
