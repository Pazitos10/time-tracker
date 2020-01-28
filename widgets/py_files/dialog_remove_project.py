# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/ui/dialog_remove_project.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog_remove_project(object):
    def setupUi(self, dialog_remove_project):
        dialog_remove_project.setObjectName("dialog_remove_project")
        dialog_remove_project.setWindowModality(QtCore.Qt.WindowModal)
        dialog_remove_project.setEnabled(True)
        dialog_remove_project.resize(340, 96)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialog_remove_project.sizePolicy().hasHeightForWidth())
        dialog_remove_project.setSizePolicy(sizePolicy)
        dialog_remove_project.setMaximumSize(QtCore.QSize(340, 122))
        dialog_remove_project.setModal(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(dialog_remove_project)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(dialog_remove_project)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 14, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(dialog_remove_project)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(dialog_remove_project)
        self.buttonBox.accepted.connect(dialog_remove_project.accept)
        self.buttonBox.rejected.connect(dialog_remove_project.reject)
        QtCore.QMetaObject.connectSlotsByName(dialog_remove_project)

    def retranslateUi(self, dialog_remove_project):
        _translate = QtCore.QCoreApplication.translate
        dialog_remove_project.setWindowTitle(_translate("dialog_remove_project", "Remove project"))
        self.label.setText(_translate("dialog_remove_project", "Are you sure you want to remove this project?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog_remove_project = QtWidgets.QDialog()
    ui = Ui_dialog_remove_project()
    ui.setupUi(dialog_remove_project)
    dialog_remove_project.show()
    sys.exit(app.exec_())
