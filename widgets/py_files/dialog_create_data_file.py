# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/ui/dialog_create_data_file.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog_create_data_file(object):
    def setupUi(self, dialog_create_data_file):
        dialog_create_data_file.setObjectName("dialog_create_data_file")
        dialog_create_data_file.resize(460, 152)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialog_create_data_file.sizePolicy().hasHeightForWidth())
        dialog_create_data_file.setSizePolicy(sizePolicy)
        dialog_create_data_file.setMaximumSize(QtCore.QSize(460, 152))
        self.verticalLayout = QtWidgets.QVBoxLayout(dialog_create_data_file)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(dialog_create_data_file)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(dialog_create_data_file)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.line_edit_filename = QtWidgets.QLineEdit(dialog_create_data_file)
        self.line_edit_filename.setObjectName("line_edit_filename")
        self.horizontalLayout.addWidget(self.line_edit_filename)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(dialog_create_data_file)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.push_btn_directory_selector = QtWidgets.QPushButton(dialog_create_data_file)
        self.push_btn_directory_selector.setObjectName("push_btn_directory_selector")
        self.horizontalLayout_2.addWidget(self.push_btn_directory_selector)
        self.label_selected_directory = QtWidgets.QLabel(dialog_create_data_file)
        self.label_selected_directory.setObjectName("label_selected_directory")
        self.horizontalLayout_2.addWidget(self.label_selected_directory)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_directory_not_selected = QtWidgets.QLabel(dialog_create_data_file)
        self.label_directory_not_selected.setAlignment(QtCore.Qt.AlignCenter)
        self.label_directory_not_selected.setObjectName("label_directory_not_selected")
        self.verticalLayout.addWidget(self.label_directory_not_selected)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.push_btn_save = QtWidgets.QPushButton(dialog_create_data_file)
        self.push_btn_save.setObjectName("push_btn_save")
        self.horizontalLayout_3.addWidget(self.push_btn_save)
        spacerItem1 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(dialog_create_data_file)
        QtCore.QMetaObject.connectSlotsByName(dialog_create_data_file)

    def retranslateUi(self, dialog_create_data_file):
        _translate = QtCore.QCoreApplication.translate
        dialog_create_data_file.setWindowTitle(_translate("dialog_create_data_file", "New data file"))
        self.label.setText(_translate("dialog_create_data_file", "Please, set a filename and select a directory to save your data."))
        self.label_2.setText(_translate("dialog_create_data_file", "Filename:"))
        self.line_edit_filename.setText(_translate("dialog_create_data_file", "data"))
        self.line_edit_filename.setPlaceholderText(_translate("dialog_create_data_file", "my_data_file"))
        self.label_3.setText(_translate("dialog_create_data_file", "Directory:"))
        self.push_btn_directory_selector.setText(_translate("dialog_create_data_file", "Select ..."))
        self.label_selected_directory.setText(_translate("dialog_create_data_file", "Not selected yet."))
        self.label_directory_not_selected.setText(_translate("dialog_create_data_file", "Please set a valid directory."))
        self.push_btn_save.setText(_translate("dialog_create_data_file", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog_create_data_file = QtWidgets.QDialog()
    ui = Ui_dialog_create_data_file()
    ui.setupUi(dialog_create_data_file)
    dialog_create_data_file.show()
    sys.exit(app.exec_())
