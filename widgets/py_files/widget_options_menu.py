# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/ui/widget_options_menu.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_widget_options_menu(object):
    def setupUi(self, widget_options_menu):
        widget_options_menu.setObjectName("widget_options_menu")
        widget_options_menu.resize(703, 356)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        widget_options_menu.setFont(font)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(widget_options_menu)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(547, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem)
        self.label = QtWidgets.QLabel(widget_options_menu)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(widget_options_menu)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgba(0,0,0,99)")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(547, 57, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.push_button_create_file = QtWidgets.QPushButton(widget_options_menu)
        self.push_button_create_file.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.push_button_create_file.setAutoFillBackground(False)
        self.push_button_create_file.setStyleSheet("padding:5")
        icon = QtGui.QIcon.fromTheme("document-new")
        self.push_button_create_file.setIcon(icon)
        self.push_button_create_file.setIconSize(QtCore.QSize(30, 30))
        self.push_button_create_file.setObjectName("push_button_create_file")
        self.verticalLayout_2.addWidget(self.push_button_create_file)
        spacerItem3 = QtWidgets.QSpacerItem(17, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem3)
        self.push_button_open_file = QtWidgets.QPushButton(widget_options_menu)
        self.push_button_open_file.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.push_button_open_file.setAutoFillBackground(False)
        self.push_button_open_file.setStyleSheet("padding:5")
        icon = QtGui.QIcon.fromTheme("document-open")
        self.push_button_open_file.setIcon(icon)
        self.push_button_open_file.setIconSize(QtCore.QSize(30, 30))
        self.push_button_open_file.setFlat(False)
        self.push_button_open_file.setObjectName("push_button_open_file")
        self.verticalLayout_2.addWidget(self.push_button_open_file)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.retranslateUi(widget_options_menu)
        QtCore.QMetaObject.connectSlotsByName(widget_options_menu)

    def retranslateUi(self, widget_options_menu):
        _translate = QtCore.QCoreApplication.translate
        widget_options_menu.setWindowTitle(_translate("widget_options_menu", "Options Menu"))
        self.label.setText(_translate("widget_options_menu", "Track the time you spend working on your projects"))
        self.label_2.setText(_translate("widget_options_menu", "Start by creating a new file or opening a file to store your data"))
        self.push_button_create_file.setText(_translate("widget_options_menu", "  Create new data file"))
        self.push_button_create_file.setShortcut(_translate("widget_options_menu", "Ctrl+N"))
        self.push_button_open_file.setText(_translate("widget_options_menu", "  Open existing data file"))
        self.push_button_open_file.setShortcut(_translate("widget_options_menu", "Ctrl+O"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget_options_menu = QtWidgets.QWidget()
    ui = Ui_widget_options_menu()
    ui.setupUi(widget_options_menu)
    widget_options_menu.show()
    sys.exit(app.exec_())
