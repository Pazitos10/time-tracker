# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/ui/widget_projects_tab.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_widget_projects_tab(object):
    def setupUi(self, widget_projects_tab):
        widget_projects_tab.setObjectName("widget_projects_tab")
        widget_projects_tab.resize(662, 392)
        self.verticalLayout = QtWidgets.QVBoxLayout(widget_projects_tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.push_btn_new_project = QtWidgets.QPushButton(widget_projects_tab)
        self.push_btn_new_project.setObjectName("push_btn_new_project")
        self.horizontalLayout.addWidget(self.push_btn_new_project)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.projects_list_widget = QtWidgets.QListWidget(widget_projects_tab)
        self.projects_list_widget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.projects_list_widget.setObjectName("projects_list_widget")
        self.verticalLayout.addWidget(self.projects_list_widget)

        self.retranslateUi(widget_projects_tab)
        QtCore.QMetaObject.connectSlotsByName(widget_projects_tab)

    def retranslateUi(self, widget_projects_tab):
        _translate = QtCore.QCoreApplication.translate
        widget_projects_tab.setWindowTitle(_translate("widget_projects_tab", "widget_projects_tab"))
        self.push_btn_new_project.setText(_translate("widget_projects_tab", "New"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget_projects_tab = QtWidgets.QWidget()
    ui = Ui_widget_projects_tab()
    ui.setupUi(widget_projects_tab)
    widget_projects_tab.show()
    sys.exit(app.exec_())
