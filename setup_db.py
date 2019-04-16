# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from common import MyConfigParser


class Ui_setup_db(object):

    __conf_name = "source/fenqi.conf"  # 配置文件

    def setupUi(self, setup_db):
        setup_db.setObjectName("setup_db")
        setup_db.resize(560, 330)
        setup_db.setFixedSize(setup_db.width(), setup_db.height())
        setup_db.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.db_button = QtWidgets.QDialogButtonBox(setup_db)
        self.db_button.setGeometry(QtCore.QRect(350, 280, 171, 32))
        self.db_button.setOrientation(QtCore.Qt.Horizontal)
        self.db_button.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.db_button.setObjectName("db_button")
        self.db_password = QtWidgets.QLineEdit(setup_db)
        self.db_password.setGeometry(QtCore.QRect(160, 190, 291, 21))
        self.db_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.db_password.setStyleSheet("font: 75 6pt;")
        self.db_password.setObjectName("db_password")
        self.db_username = QtWidgets.QLineEdit(setup_db)
        self.db_username.setGeometry(QtCore.QRect(160, 160, 291, 21))
        self.db_username.setObjectName("db_username")
        self.db_dbname = QtWidgets.QLineEdit(setup_db)
        self.db_dbname.setGeometry(QtCore.QRect(160, 130, 151, 21))
        self.db_dbname.setObjectName("db_dbname")
        self.db_label1 = QtWidgets.QLabel(setup_db)
        self.db_label1.setGeometry(QtCore.QRect(90, 50, 111, 31))
        self.db_label1.setStyleSheet("font: 75 14pt \"Agency FB\";")
        self.db_label1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.db_label1.setObjectName("db_label1")
        self.db_host_tip = QtWidgets.QLabel(setup_db)
        self.db_host_tip.setGeometry(QtCore.QRect(80, 100, 71, 21))
        self.db_host_tip.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.db_host_tip.setObjectName("db_host_tip")
        self.db_dbname_tip = QtWidgets.QLabel(setup_db)
        self.db_dbname_tip.setGeometry(QtCore.QRect(80, 130, 71, 21))
        self.db_dbname_tip.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.db_dbname_tip.setObjectName("db_dbname_tip")
        self.db_username_tip = QtWidgets.QLabel(setup_db)
        self.db_username_tip.setGeometry(QtCore.QRect(80, 160, 71, 21))
        self.db_username_tip.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.db_username_tip.setObjectName("db_username_tip")
        self.db_password_tip = QtWidgets.QLabel(setup_db)
        self.db_password_tip.setGeometry(QtCore.QRect(80, 190, 71, 21))
        self.db_password_tip.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.db_password_tip.setObjectName("db_password_tip")
        self.db_host = QtWidgets.QLineEdit(setup_db)
        self.db_host.setGeometry(QtCore.QRect(160, 100, 291, 21))
        self.db_host.setObjectName("db_host")
        self.db_port_tip = QtWidgets.QLabel(setup_db)
        self.db_port_tip.setGeometry(QtCore.QRect(320, 130, 51, 21))
        self.db_port_tip.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.db_port_tip.setObjectName("db_port_tip")
        self.db_port = QtWidgets.QLineEdit(setup_db)
        self.db_port.setGeometry(QtCore.QRect(380, 130, 71, 21))
        self.db_port.setObjectName("db_port")

        self.retranslateUi(setup_db)
        self.db_button.accepted.connect(self.accept)
        self.db_button.rejected.connect(setup_db.reject)
        QtCore.QMetaObject.connectSlotsByName(setup_db)

    def retranslateUi(self, setup_db):
        _translate = QtCore.QCoreApplication.translate
        setup_db.setWindowModality(QtCore.Qt.ApplicationModal)
        setup_db.setWindowTitle(_translate("setup_db", "数据路连接配置"))
        self.db_label1.setText(_translate("setup_db", "连接设置"))
        self.db_host_tip.setText(_translate("setup_db", "主机地址："))
        self.db_dbname_tip.setText(_translate("setup_db", "数据库名："))
        self.db_username_tip.setText(_translate("setup_db", "连接用户："))
        self.db_password_tip.setText(_translate("setup_db", "连接密码："))
        self.db_port_tip.setText(_translate("setup_db", "端口："))
        # 读取配置文件
        try:
            cf = MyConfigParser()
            cf.read(self.__conf_name)
            self.db_host.setText(cf.get('MYSQL', 'DB_HOST'))
            self.db_port.setText(cf.get('MYSQL', 'DB_PORT'))
            self.db_dbname.setText(cf.get('MYSQL', 'DB_NAME'))
            self.db_username.setText(cf.get('MYSQL', 'DB_USER'))
            self.db_password.setText(cf.get('MYSQL', 'DB_PWD'))
        except Exception:
            pass

    def accept(self):
        cf = MyConfigParser()
        cf.read(self.__conf_name)
        if cf.has_section('MYSQL') == False:
            cf.add_section('MYSQL')
        # 写入配置文件
        cf.set('MYSQL', 'DB_HOST', self.db_host.text())
        cf.set('MYSQL', 'DB_PORT', self.db_port.text())
        cf.set('MYSQL', 'DB_NAME', self.db_dbname.text())
        cf.set('MYSQL', 'DB_USER', self.db_username.text())
        cf.set('MYSQL', 'DB_PWD', self.db_password.text())
        cf.write(open(self.__conf_name, 'w'))
        self.msg_frame('保存成功, 配置已生效')

    def msg_frame(self, text=None):
        message = QtWidgets.QMessageBox()
        message.setWindowTitle("提示")
        message.setText(text)
        message.setIcon(1)
        message.exec_()

