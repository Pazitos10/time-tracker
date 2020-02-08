# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/ui/dialog_about.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog_about(object):
    def setupUi(self, dialog_about):
        dialog_about.setObjectName("dialog_about")
        dialog_about.setWindowModality(QtCore.Qt.ApplicationModal)
        dialog_about.resize(400, 335)
        dialog_about.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(dialog_about)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.app_logo = QtWidgets.QLabel(dialog_about)
        self.app_logo.setText("")
        self.app_logo.setPixmap(QtGui.QPixmap(":/images/icon_full.png"))
        self.app_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.app_logo.setOpenExternalLinks(True)
        self.app_logo.setObjectName("app_logo")
        self.verticalLayout.addWidget(self.app_logo)
        self.app_name = QtWidgets.QLabel(dialog_about)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.app_name.setFont(font)
        self.app_name.setAlignment(QtCore.Qt.AlignCenter)
        self.app_name.setObjectName("app_name")
        self.verticalLayout.addWidget(self.app_name)
        self.app_repo_url = QtWidgets.QLabel(dialog_about)
        self.app_repo_url.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.app_repo_url.sizePolicy().hasHeightForWidth())
        self.app_repo_url.setSizePolicy(sizePolicy)
        self.app_repo_url.setTextFormat(QtCore.Qt.AutoText)
        self.app_repo_url.setScaledContents(False)
        self.app_repo_url.setAlignment(QtCore.Qt.AlignCenter)
        self.app_repo_url.setWordWrap(False)
        self.app_repo_url.setIndent(-1)
        self.app_repo_url.setOpenExternalLinks(True)
        self.app_repo_url.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.app_repo_url.setObjectName("app_repo_url")
        self.verticalLayout.addWidget(self.app_repo_url)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.push_btn_close = QtWidgets.QDialogButtonBox(dialog_about)
        self.push_btn_close.setOrientation(QtCore.Qt.Horizontal)
        self.push_btn_close.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.push_btn_close.setCenterButtons(True)
        self.push_btn_close.setObjectName("push_btn_close")
        self.verticalLayout.addWidget(self.push_btn_close)

        self.retranslateUi(dialog_about)
        self.push_btn_close.accepted.connect(dialog_about.accept)
        self.push_btn_close.rejected.connect(dialog_about.reject)
        QtCore.QMetaObject.connectSlotsByName(dialog_about)

    def retranslateUi(self, dialog_about):
        _translate = QtCore.QCoreApplication.translate
        dialog_about.setWindowTitle(_translate("dialog_about", "About"))
        self.app_name.setText(_translate("dialog_about", "Time Tracker"))
        self.app_repo_url.setText(_translate("dialog_about", "https://github.com/Pazitos10/time_tracker_gui"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog_about = QtWidgets.QDialog()
    ui = Ui_dialog_about()
    ui.setupUi(dialog_about)
    dialog_about.show()
    sys.exit(app.exec_())
