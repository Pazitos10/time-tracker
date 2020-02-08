# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/ui/dialog_file_exist.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog_file_exist(object):
    def setupUi(self, dialog_file_exist):
        dialog_file_exist.setObjectName("dialog_file_exist")
        dialog_file_exist.resize(392, 118)
        self.verticalLayout = QtWidgets.QVBoxLayout(dialog_file_exist)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(dialog_file_exist)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.buttonBox = QtWidgets.QDialogButtonBox(dialog_file_exist)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(dialog_file_exist)
        self.buttonBox.accepted.connect(dialog_file_exist.accept)
        self.buttonBox.rejected.connect(dialog_file_exist.reject)
        QtCore.QMetaObject.connectSlotsByName(dialog_file_exist)

    def retranslateUi(self, dialog_file_exist):
        _translate = QtCore.QCoreApplication.translate
        dialog_file_exist.setWindowTitle(_translate("dialog_file_exist", "File already exist"))
        self.label.setText(_translate("dialog_file_exist", "A file with the same name already exist in that directory. \n"
" Click \"OK\" to override"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog_file_exist = QtWidgets.QDialog()
    ui = Ui_dialog_file_exist()
    ui.setupUi(dialog_file_exist)
    dialog_file_exist.show()
    sys.exit(app.exec_())
