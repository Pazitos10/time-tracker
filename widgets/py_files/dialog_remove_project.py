# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/ui/dialog_remove_project.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog_remove(object):
    def setupUi(self, dialog_remove):
        dialog_remove.setObjectName("dialog_remove")
        dialog_remove.setWindowModality(QtCore.Qt.WindowModal)
        dialog_remove.setEnabled(True)
        dialog_remove.resize(340, 96)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialog_remove.sizePolicy().hasHeightForWidth())
        dialog_remove.setSizePolicy(sizePolicy)
        dialog_remove.setMaximumSize(QtCore.QSize(340, 122))
        dialog_remove.setModal(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(dialog_remove)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(dialog_remove)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 14, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(dialog_remove)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(dialog_remove)
        self.buttonBox.accepted.connect(dialog_remove.accept)
        self.buttonBox.rejected.connect(dialog_remove.reject)
        QtCore.QMetaObject.connectSlotsByName(dialog_remove)

    def retranslateUi(self, dialog_remove):
        _translate = QtCore.QCoreApplication.translate
        dialog_remove.setWindowTitle(_translate("dialog_remove", "Remove project"))
        self.label.setText(_translate("dialog_remove", "Are you sure you want to remove this project?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog_remove = QtWidgets.QDialog()
    ui = Ui_dialog_remove()
    ui.setupUi(dialog_remove)
    dialog_remove.show()
    sys.exit(app.exec_())
