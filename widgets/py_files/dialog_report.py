# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/ui/dialog_report.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog_report(object):
    def setupUi(self, dialog_report):
        dialog_report.setObjectName("dialog_report")
        dialog_report.setWindowModality(QtCore.Qt.ApplicationModal)
        dialog_report.resize(288, 184)
        dialog_report.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(dialog_report)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_time_spent_description = QtWidgets.QLabel(dialog_report)
        self.label_time_spent_description.setObjectName("label_time_spent_description")
        self.verticalLayout.addWidget(self.label_time_spent_description)
        self.label_time_spent_value = QtWidgets.QLabel(dialog_report)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_time_spent_value.setFont(font)
        self.label_time_spent_value.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time_spent_value.setObjectName("label_time_spent_value")
        self.verticalLayout.addWidget(self.label_time_spent_value)
        self.label_ongoing_session_description = QtWidgets.QLabel(dialog_report)
        self.label_ongoing_session_description.setObjectName("label_ongoing_session_description")
        self.verticalLayout.addWidget(self.label_ongoing_session_description)
        self.label_time_spent_in_ongoing_session_value = QtWidgets.QLabel(dialog_report)
        self.label_time_spent_in_ongoing_session_value.setObjectName("label_time_spent_in_ongoing_session_value")
        self.verticalLayout.addWidget(self.label_time_spent_in_ongoing_session_value)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.push_btn_close = QtWidgets.QDialogButtonBox(dialog_report)
        self.push_btn_close.setOrientation(QtCore.Qt.Horizontal)
        self.push_btn_close.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.push_btn_close.setCenterButtons(True)
        self.push_btn_close.setObjectName("push_btn_close")
        self.verticalLayout.addWidget(self.push_btn_close)

        self.retranslateUi(dialog_report)
        self.push_btn_close.accepted.connect(dialog_report.accept)
        self.push_btn_close.rejected.connect(dialog_report.reject)
        QtCore.QMetaObject.connectSlotsByName(dialog_report)

    def retranslateUi(self, dialog_report):
        _translate = QtCore.QCoreApplication.translate
        dialog_report.setWindowTitle(_translate("dialog_report", "Report"))
        self.label_time_spent_description.setText(_translate("dialog_report", "Time spent working on project \"Test\":"))
        self.label_time_spent_value.setText(_translate("dialog_report", "1 day, 7:54:21"))
        self.label_ongoing_session_description.setText(_translate("dialog_report", "Ongoing session: True"))
        self.label_time_spent_in_ongoing_session_value.setText(_translate("dialog_report", "Time spent in ongoing session: 0:14:12"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog_report = QtWidgets.QDialog()
    ui = Ui_dialog_report()
    ui.setupUi(dialog_report)
    dialog_report.show()
    sys.exit(app.exec_())
