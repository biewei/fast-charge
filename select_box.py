# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QDialog, QCheckBox, QMessageBox, QApplication
from PyQt5 import QtWidgets, QtCore
from collections import OrderedDict
from yaml import load as ym_load
from common import MyConfigParser
import MySQLdb


class GetDataList(QtCore.QThread):
    # 控制台信号
    signal = QtCore.pyqtSignal(str, int)
    # 结果集信号
    signal2 = QtCore.pyqtSignal(OrderedDict)

    # 配置文件
    __conf_name = 'source/config.conf'
    # 还款时间
    deadline = None
    # 查询还款状态
    select_status = 1

    def __init__(self, deadline, opt_overdue=False, parent=None):
        super(GetDataList, self).__init__(parent)
        self.deadline = deadline
        if opt_overdue == True:
            self.select_status = 6
        # 加载配置文件
        cf = MyConfigParser()
        cf.read(self.__conf_name)
        # 数据库连接
        self.__connect = MySQLdb.connect(
                cf.get('MYSQL', 'DB_HOST'),
                cf.get('MYSQL', 'DB_USER'),
                cf.get('MYSQL', 'DB_PWD'),
                cf.get('MYSQL', 'DB_NAME'),
                charset='utf8')

    def __del__(self):
        self.__connect.close()

    def run(self):
        self.msleep(500)
        try:
            # 获取油标,查询待下载列表
            cursor = self.__connect.cursor()
            cursor.execute("SELECT d.borrow_id, d.borrow_uid, SUM(d.capital) capital, SUM(d.interest) interest, "
                           "d.sort_order, d.total, m.user_name, mm.account_money, mm.back_money, mi.idcard "
                           "FROM lzh_investor_detail d "
                           "INNER JOIN lzh_borrow_info b ON b.id=d.borrow_id "
                           "INNER JOIN lzh_members m ON m.id=d.borrow_uid "
                           "LEFT JOIN lzh_member_money mm ON mm.uid=m.id "
                           "LEFT JOIN lzh_member_info mi ON mi.uid=m.id "
                           "WHERE b.borrow_type=9 and b.borrow_u_id=0 and d.deadline=%s AND d.status=%s "
                           "GROUP BY d.borrow_uid ORDER BY borrow_id ASC" % (self.deadline, self.select_status))
            # 获取查询结果，存入字典
            dataMap = OrderedDict()
            for ogroup in cursor.fetchall():
                dataMap["Borrow_%s" % ('%06d' % ogroup[0])] = {
                    "borrow_id": ogroup[0],
                    "borrow_uid": ogroup[1],
                    "capital": ogroup[2],
                    "interest": ogroup[3],
                    "sort_order": ogroup[4],
                    "total": ogroup[5],
                    "user_name": ogroup[6],
                    "act_money": round(ogroup[7] + ogroup[8], 2),
                    "idcard": ogroup[9]
                }
            cursor.close()
            # 发送数据给主进程处理
            if len(dataMap) == 0:
                self.signal.emit('错误：未查询到待还款列表，请检查您的选项！', 0)
            else:
                self.signal2.emit(dataMap)
        except Exception as e:
            self.signal.emit('错误：%s' % e, 0)


# 选择充值账户
class SelectAccount(QDialog):
    # 复选框列表
    checkBoxMap = None
    # 原始数据集
    dataMap = None
    # 选中结果集
    resultMap = None
    index_begin = None

    # 控制台信号
    signal = QtCore.pyqtSignal(str, int)

    def __init__(self):
        super(SelectAccount, self).__init__()
        self.setObjectName("select_account")
        self.resize(700, 460)
        self.setMinimumSize(QtCore.QSize(700, 460))
        self.setMaximumSize(QtCore.QSize(700, 460))
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowStaysOnTopHint)
        self.button = QtWidgets.QDialogButtonBox(self)
        self.button.setGeometry(QtCore.QRect(430, 410, 161, 32))
        self.button.setOrientation(QtCore.Qt.Horizontal)
        self.button.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button.setObjectName("button")
        self.check_all = QtWidgets.QCheckBox(self)
        self.check_all.setGeometry(QtCore.QRect(60, 410, 91, 31))
        self.check_all.setObjectName("check_all")
        self.check_all.setChecked(False)
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setGeometry(QtCore.QRect(20, 20, 661, 380))
        self.scrollArea.setMaximumSize(QtCore.QSize(1000, 1000000))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Panel)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea_widget = QtWidgets.QWidget()
        self.scrollArea_widget.setEnabled(True)
        self.scrollArea_widget.setGeometry(QtCore.QRect(0, 0, 640, 380))
        self.scrollArea_widget.setStyleSheet("background-color:#FFFFFF;")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_widget.sizePolicy().hasHeightForWidth())
        self.scrollArea_widget.setSizePolicy(sizePolicy)
        self.scrollArea_widget.setMaximumSize(QtCore.QSize(700, 1000000))
        self.scrollArea_widget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.scrollArea_widget.setObjectName("scrollArea_widget")
        self.scrollArea.setWidget(self.scrollArea_widget)
        # 添加内容
        self.setWindowTitle("选择充值账户")
        self.check_all.setText("全选/取消")

    def add_check_box(self, dataMap):
        self.dataMap = dataMap
        self.checkBoxMap = OrderedDict()
        i = 1
        for index in dataMap:
            self.checkBoxMap[index] = QCheckBox(self.scrollArea_widget)
            x = 20
            y = (i * 30 - 20)
            self.checkBoxMap[index].setGeometry(QtCore.QRect(x, y, 700, 20))
            self.checkBoxMap[index].setChecked(False)
            self.checkBoxMap[index].setObjectName(index)
            # 设置余额足够时不可选中
            benxi = round(dataMap[index]['capital'] + dataMap[index]['interest'], 2)
            charge_money = round(benxi - dataMap[index]['act_money'], 2)
            if charge_money <= 0:
                self.checkBoxMap[index].setStyleSheet("color: #CCCCCC")
                self.checkBoxMap[index].setEnabled(False)
            # 设置控件文本内容
            self.checkBoxMap[index].setText(
                    "[%s] 标号：%s , 期数：%s/%s, 本息：%s/%s, 账户余额：%s, 用户名：%s " %
                    ('%04d' % i, dataMap[index]['borrow_id'], dataMap[index]['sort_order'], dataMap[index]['total'],
                     dataMap[index]['capital'], dataMap[index]['interest'], dataMap[index]['act_money'],
                     dataMap[index]['user_name']))
            i += 1
        # 默认未选中
        self.resultMap = {}
        # 设置滚动区域高度(必须)
        self.scrollArea_widget.setMinimumHeight(i * 30)
        # 绑定事件
        self.__bind_action()

    def __bind_action(self):
        # 全选/取消
        self.check_all.clicked.connect(self.__select_all)
        # 单个选择/取消
        for index in self.checkBoxMap:
            # lambda 需要定义默认参数，否则循环会被覆盖
            self.checkBoxMap[index].clicked.connect(lambda s, i=index, fun=self.__select: fun(s, i))
        # 取消事件绑定
        self.button.rejected.connect(self.closeEvent)

    def closeEvent(self, event=None):
        reply = QMessageBox.question(self, '温馨提示', "确认关闭？",
                                     QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                     QtWidgets.QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.signal.emit('操作取消！', 0)
            self.reject()
        else:
            event and event.ignore()

    # 复选框选择时触发事件
    def __select(self, state, index):
        if not state:
            if index in self.resultMap:
                self.resultMap.pop(index)
            self.check_all.setChecked(False)
            self.index_begin = None
        else:
            # 监听 Shift 按键批量选择
            if QApplication.keyboardModifiers() == QtCore.Qt.ShiftModifier:
                if not self.index_begin:
                    self.index_begin = int(index[7:])
                else:
                    index_end = int(index[7:]) + 1
                    for i in range(self.index_begin, index_end):
                        key_name = 'Borrow_%s' % ('%06d' % i)
                        if key_name not in self.dataMap:
                            continue
                        if self.checkBoxMap[key_name].isEnabled():
                            self.checkBoxMap[key_name].setChecked(True)
                            self.resultMap[key_name] = self.dataMap[key_name]
            else:
                self.resultMap[index] = self.dataMap[index]

    # 全选或取消全选
    def __select_all(self, is_checked):
        if is_checked:
            self.resultMap = self.dataMap.copy()
            for index in self.checkBoxMap:
                if self.checkBoxMap[index].isEnabled():
                    self.checkBoxMap[index].setChecked(True)
        else:
            self.resultMap.clear()
            for index in self.checkBoxMap:
                if self.checkBoxMap[index].isEnabled():
                    self.checkBoxMap[index].setChecked(False)
        self.index_begin = None


# 选择银行卡
class SelectCard(QDialog):
    # 复选框列表
    checkBoxMap = None
    # 配置文件数据
    dataMap = None
    # 选中结果集
    resultMap = None
    # 银行卡配置文件
    __card_conf = "source/card.yaml"

    # 控制台信号
    signal = QtCore.pyqtSignal(str, int)

    def __init__(self):
        super(SelectCard, self).__init__()
        self.setObjectName("select_card")
        self.resize(660, 460)
        self.setMinimumSize(QtCore.QSize(660, 460))
        self.setMaximumSize(QtCore.QSize(660, 460))
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowStaysOnTopHint)
        self.button = QtWidgets.QDialogButtonBox(self)
        self.button.setGeometry(QtCore.QRect(430, 410, 161, 32))
        self.button.setOrientation(QtCore.Qt.Horizontal)
        self.button.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button.setObjectName("button")
        self.check_all = QtWidgets.QCheckBox(self)
        self.check_all.setGeometry(QtCore.QRect(60, 410, 91, 31))
        self.check_all.setObjectName("check_all")
        self.check_all.setChecked(False)
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setGeometry(QtCore.QRect(20, 20, 621, 380))
        self.scrollArea.setMaximumSize(QtCore.QSize(1000, 10000))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Panel)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea_widget = QtWidgets.QWidget()
        self.scrollArea_widget.setEnabled(True)
        self.scrollArea_widget.setGeometry(QtCore.QRect(0, 0, 600, 380))
        self.scrollArea_widget.setStyleSheet("background-color:#FFFFFF;")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_widget.sizePolicy().hasHeightForWidth())
        self.scrollArea_widget.setSizePolicy(sizePolicy)
        self.scrollArea_widget.setMaximumSize(QtCore.QSize(660, 100000))
        self.scrollArea_widget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.scrollArea_widget.setObjectName("scrollArea_widget")
        self.scrollArea.setWidget(self.scrollArea_widget)
        # 添加内容
        self.setWindowTitle("选择银行卡")
        self.check_all.setText("全选/取消")

    def add_check_box(self):
        # 读取银行卡配置列表
        try:
            with open(self.__card_conf, "r", encoding='utf-8') as fp:
                self.dataMap = ym_load(fp)
        except Exception as e:
            self.signal.emit('错误：%s' % e)
            self.accept()
        else:
            i = 1
            self.checkBoxMap = OrderedDict()
            for index in self.dataMap:
                self.checkBoxMap[index] = QCheckBox(self.scrollArea_widget)
                x = 20
                y = (i * 30)
                self.checkBoxMap[index].setGeometry(QtCore.QRect(x, y, 600, 20))
                self.checkBoxMap[index].setChecked(False)
                self.checkBoxMap[index].setObjectName(index)
                self.checkBoxMap[index].setText('银行：[%s], 卡号 >>> %s' %
                                                (self.dataMap[index]['name'], self.dataMap[index]['number']))
                i += 1
            # 默认未选中
            self.resultMap = {}
            # 设置滚动区域高度(必须)
            self.scrollArea_widget.setMinimumHeight(i*30 + 15)
            # 绑定事件
            self.__bind_action()

    def __bind_action(self):
        # 全选/取消
        self.check_all.clicked.connect(self.__select_all)
        # 单个选择/取消
        for index in self.checkBoxMap:
            # lambda 需要定义默认参数，否则循环将被覆盖
            self.checkBoxMap[index].clicked.connect(lambda s, i=index, fun=self.__select: fun(s, i))
        # 取消事件绑定
        self.button.rejected.connect(self.closeEvent)

    def closeEvent(self, event=None):
        reply = QMessageBox.question(self, '温馨提示', "确认关闭？",
                                     QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                     QtWidgets.QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.signal.emit('操作取消！', 0)
            self.reject()
        else:
            event and event.ignore()

    # 复选框选择时触发事件
    def __select(self, state, index):
        if not state:
            if index in self.resultMap:
                self.resultMap.pop(index)
            self.check_all.setChecked(False)
        else:
            self.resultMap[index] = self.dataMap[index]

    # 全选或取消全选
    def __select_all(self, is_checked):
        if is_checked:
            self.resultMap = self.dataMap.copy()
            for index in self.checkBoxMap:
                self.checkBoxMap[index].setChecked(True)
        else:
            self.resultMap.clear()
            for index in self.checkBoxMap:
                self.checkBoxMap[index].setChecked(False)



