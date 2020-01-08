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
        self.lineEdit = QtWidgets.QLineEdit(dialog_create_data_file)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
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
        self.push_btn_file_chooser = QtWidgets.QPushButton(dialog_create_data_file)
        self.push_btn_file_chooser.setObjectName("push_btn_file_chooser")
        self.horizontalLayout_2.addWidget(self.push_btn_file_chooser)
        self.label_4 = QtWidgets.QLabel(dialog_create_data_file)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(dialog_create_data_file)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(dialog_create_data_file)
        self.buttonBox.accepted.connect(dialog_create_data_file.accept)
        self.buttonBox.rejected.connect(dialog_create_data_file.reject)
        QtCore.QMetaObject.connectSlotsByName(dialog_create_data_file)

    def retranslateUi(self, dialog_create_data_file):
        _translate = QtCore.QCoreApplication.translate
        dialog_create_data_file.setWindowTitle(_translate("dialog_create_data_file", "Dialog"))
        self.label.setText(_translate("dialog_create_data_file", "Please, set a filename and choose a directory to save your data."))
        self.label_2.setText(_translate("dialog_create_data_file", "Filename:"))
        self.lineEdit.setPlaceholderText(_translate("dialog_create_data_file", "my_data_file"))
        self.label_3.setText(_translate("dialog_create_data_file", "Directory:"))
        self.push_btn_file_chooser.setText(_translate("dialog_create_data_file", "Select ..."))
        self.label_4.setText(_translate("dialog_create_data_file", "Not selected yet."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog_create_data_file = QtWidgets.QDialog()
    ui = Ui_dialog_create_data_file()
    ui.setupUi(dialog_create_data_file)
    dialog_create_data_file.show()
    sys.exit(app.exec_())
