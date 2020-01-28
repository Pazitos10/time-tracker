# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/ui/dialog_new_project.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog_new_project(object):
    def setupUi(self, dialog_new_project):
        dialog_new_project.setObjectName("dialog_new_project")
        dialog_new_project.setWindowModality(QtCore.Qt.ApplicationModal)
        dialog_new_project.resize(279, 134)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialog_new_project.sizePolicy().hasHeightForWidth())
        dialog_new_project.setSizePolicy(sizePolicy)
        dialog_new_project.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(dialog_new_project)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(dialog_new_project)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(dialog_new_project)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        spacerItem = QtWidgets.QSpacerItem(17, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(dialog_new_project)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(dialog_new_project)
        self.buttonBox.accepted.connect(dialog_new_project.accept)
        self.buttonBox.rejected.connect(dialog_new_project.reject)
        QtCore.QMetaObject.connectSlotsByName(dialog_new_project)

    def retranslateUi(self, dialog_new_project):
        _translate = QtCore.QCoreApplication.translate
        dialog_new_project.setWindowTitle(_translate("dialog_new_project", "New Project"))
        self.label.setText(_translate("dialog_new_project", "Project name:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog_new_project = QtWidgets.QDialog()
    ui = Ui_dialog_new_project()
    ui.setupUi(dialog_new_project)
    dialog_new_project.show()
    sys.exit(app.exec_())
