# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/ui/list_item_widget.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_list_item_widget(object):
    def setupUi(self, list_item_widget):
        list_item_widget.setObjectName("list_item_widget")
        list_item_widget.resize(483, 48)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(list_item_widget.sizePolicy().hasHeightForWidth())
        list_item_widget.setSizePolicy(sizePolicy)
        list_item_widget.setMaximumSize(QtCore.QSize(9999, 48))
        self.horizontalLayout = QtWidgets.QHBoxLayout(list_item_widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.project_name_label = QtWidgets.QLabel(list_item_widget)
        self.project_name_label.setObjectName("project_name_label")
        self.horizontalLayout.addWidget(self.project_name_label)
        spacerItem = QtWidgets.QSpacerItem(169, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.push_btn_edit = QtWidgets.QPushButton(list_item_widget)
        self.push_btn_edit.setObjectName("push_btn_edit")
        self.horizontalLayout.addWidget(self.push_btn_edit)
        spacerItem1 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.push_btn_remove = QtWidgets.QPushButton(list_item_widget)
        self.push_btn_remove.setObjectName("push_btn_remove")
        self.horizontalLayout.addWidget(self.push_btn_remove)

        self.retranslateUi(list_item_widget)
        QtCore.QMetaObject.connectSlotsByName(list_item_widget)

    def retranslateUi(self, list_item_widget):
        _translate = QtCore.QCoreApplication.translate
        list_item_widget.setWindowTitle(_translate("list_item_widget", "Form"))
        self.project_name_label.setText(_translate("list_item_widget", "Project name"))
        self.push_btn_edit.setText(_translate("list_item_widget", "Edit"))
        self.push_btn_remove.setText(_translate("list_item_widget", "Remove"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    list_item_widget = QtWidgets.QWidget()
    ui = Ui_list_item_widget()
    ui.setupUi(list_item_widget)
    list_item_widget.show()
    sys.exit(app.exec_())
