#!/usr/bin/env python
# -*- coding: UTF-8 -*
"""
该脚本为驱动程序，用来展示所有窗口
"""
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        from charge import MainWindow
        self.main_ui = MainWindow()
        self.main_ui.setupUi(self)
        self.main_ui.setupAction()

    def closeEvent(self, e):
        close_tip = '全民分期提示您'
        if self.main_ui.runState == True:
            close_msg = '\n程序运行过程中关闭窗口可能会导致严重的错误， 确认关闭？\n'
        else:
            close_msg = '\n 您要关闭程序吗 ？ '
        result = QtWidgets.QMessageBox.question(self, close_tip, close_msg,
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            e.accept()
        else:
            e.ignore()


class PageDB(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        from setup_db import Ui_setup_db
        self.db_ui = Ui_setup_db()
        self.db_ui.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # 显示启动界面
    splash = QtWidgets.QSplashScreen(QtGui.QPixmap("source/bg_finance.jpg"))
    splash.showMessage("正在启动 . . .", QtCore.Qt.AlignCenter | QtCore.Qt.AlignBottom, QtCore.Qt.white)
    splash.show()

    # 刷新进程并处理主进程事件
    QtWidgets.qApp.processEvents()
    window = MainWindow()
    dbPage = PageDB()

    # ## 绑定菜单栏事件
    window.main_ui.menu_setting_db.triggered.connect(dbPage.show)
    window.show()
    # 隐藏启动界面
    splash.finish(window)
    sys.exit(app.exec_())
