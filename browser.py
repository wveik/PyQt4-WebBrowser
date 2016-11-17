# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'browser.ui'
#
# Created: Thu Nov 17 14:08:32 2016
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):

    def back(self):
        print('Back')

    def forward(self):
        print('forward')

    def reload(self):
        print('reload')

    def goAddress(self):
        print('goAddress')

    def home(self):
        print('home')

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tb_back = QtGui.QToolButton(self.centralwidget)
        self.tb_back.setGeometry(QtCore.QRect(10, 10, 41, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/left-arrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tb_back.setIcon(icon)
        self.tb_back.setIconSize(QtCore.QSize(16, 16))
        self.tb_back.setObjectName(_fromUtf8("tb_back"))
        ################## Event - Возврат
        self.tb_back.clicked.connect(self.back)
        ################## End Event
        self.rb_reload = QtGui.QToolButton(self.centralwidget)
        self.rb_reload.setGeometry(QtCore.QRect(60, 10, 41, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/reload.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rb_reload.setIcon(icon1)
        self.rb_reload.setObjectName(_fromUtf8("rb_reload"))
        ################## Event - Возврат
        self.rb_reload.clicked.connect(self.reload)
        ################## End Event
        self.tb_forward = QtGui.QToolButton(self.centralwidget)
        self.tb_forward.setGeometry(QtCore.QRect(110, 10, 41, 31))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/right-arrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tb_forward.setIcon(icon2)
        self.tb_forward.setObjectName(_fromUtf8("tb_forward"))
        ################## Event - Возврат
        self.tb_forward.clicked.connect(self.forward)
        ################## End Event
        self.tb_home = QtGui.QToolButton(self.centralwidget)
        self.tb_home.setGeometry(QtCore.QRect(160, 10, 41, 31))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/home.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tb_home.setIcon(icon3)
        self.tb_home.setObjectName(_fromUtf8("tb_home"))
        ################## Event - Возврат
        self.tb_home.clicked.connect(self.home)
        ################## End Event
        self.ln_addressbar = QtGui.QLineEdit(self.centralwidget)
        self.ln_addressbar.setGeometry(QtCore.QRect(210, 9, 531, 31))
        self.ln_addressbar.setObjectName(_fromUtf8("ln_addressbar"))
        self.tb_search = QtGui.QToolButton(self.centralwidget)
        self.tb_search.setGeometry(QtCore.QRect(750, 10, 41, 31))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tb_search.setIcon(icon4)
        self.tb_search.setObjectName(_fromUtf8("tb_search"))
        ################## Event - Возврат
        self.tb_search.clicked.connect(self.goAddress)
        ################## End Event
        self.webView = QtWebKit.QWebView(self.centralwidget)
        self.webView.setGeometry(QtCore.QRect(0, 50, 801, 541))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.tb_back.setText(_translate("MainWindow", "...", None))
        self.rb_reload.setText(_translate("MainWindow", "...", None))
        self.tb_forward.setText(_translate("MainWindow", "...", None))
        self.tb_home.setText(_translate("MainWindow", "...", None))
        self.tb_search.setText(_translate("MainWindow", "...", None))

from PyQt4 import QtWebKit
import sys
import resource

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())