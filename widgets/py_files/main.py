# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets/ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(662, 392)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(662, 392))
        MainWindow.setMaximumSize(QtCore.QSize(662, 392))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icon_full.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_4.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 662, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuReport = QtWidgets.QMenu(self.menubar)
        self.menuReport.setObjectName("menuReport")
        MainWindow.setMenuBar(self.menubar)
        self.action_about = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("help")
        self.action_about.setIcon(icon)
        self.action_about.setObjectName("action_about")
        self.action_new = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("document-new")
        self.action_new.setIcon(icon)
        self.action_new.setShortcutVisibleInContextMenu(True)
        self.action_new.setObjectName("action_new")
        self.action_open = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("document-open")
        self.action_open.setIcon(icon)
        self.action_open.setObjectName("action_open")
        self.action_close = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("document-close")
        self.action_close.setIcon(icon)
        self.action_close.setObjectName("action_close")
        self.action_exit = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("application-exit")
        self.action_exit.setIcon(icon)
        self.action_exit.setObjectName("action_exit")
        self.actionProjects_Chart = QtWidgets.QAction(MainWindow)
        self.actionProjects_Chart.setObjectName("actionProjects_Chart")
        self.actionTime_Series_Chart = QtWidgets.QAction(MainWindow)
        self.actionTime_Series_Chart.setObjectName("actionTime_Series_Chart")
        self.menuFile.addAction(self.action_new)
        self.menuFile.addAction(self.action_open)
        self.menuFile.addAction(self.action_close)
        self.menuFile.addAction(self.action_exit)
        self.menuHelp.addAction(self.action_about)
        self.menuReport.addAction(self.actionProjects_Chart)
        self.menuReport.addAction(self.actionTime_Series_Chart)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuReport.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Time Tracker"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuReport.setTitle(_translate("MainWindow", "Report"))
        self.action_about.setText(_translate("MainWindow", "About"))
        self.action_new.setText(_translate("MainWindow", "New"))
        self.action_new.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.action_open.setText(_translate("MainWindow", "Open"))
        self.action_open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_close.setText(_translate("MainWindow", "Close"))
        self.action_close.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.action_exit.setText(_translate("MainWindow", "Exit"))
        self.action_exit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionProjects_Chart.setText(_translate("MainWindow", "Projects Chart"))
        self.actionTime_Series_Chart.setText(_translate("MainWindow", "Time-Series Chart"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
