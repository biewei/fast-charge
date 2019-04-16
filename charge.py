# -*- coding: utf-8 -*-
from PyQt5 import QtGui
from selenium import webdriver
from select_box import *
from PIL import ImageGrab
import pyautogui
import numpy as np
import cv2
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 660)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 660))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 660))
        MainWindow.setWindowIcon(QtGui.QIcon('source/icon/main_icon.png'))
        self.frame_main = QtWidgets.QWidget(MainWindow)
        self.frame_main.setObjectName("frame_main")
        self.frame_box = QtWidgets.QFrame(self.frame_main)
        self.frame_box.setGeometry(QtCore.QRect(0, 0, 1001, 641))
        self.frame_box.setStyleSheet("QFrame#frame_box{background-color: rgb(113, 113, 113);}")
        self.frame_box.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_box.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_box.setObjectName("frame_box")
        self.console = QtWidgets.QTextBrowser(self.frame_box)
        self.console.setGeometry(QtCore.QRect(20, 50, 680, 560))
        self.console.setStyleSheet("color: rgb(0, 235, 0);background-color: rgb(72, 72, 72);"
                                   "padding-left:5px;")
        self.console.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.console.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.console.setLineWidth(1)
        self.console.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.console.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.console.setObjectName("console")
        self.progress = QtWidgets.QProgressBar(self.frame_box)
        self.progress.setGeometry(QtCore.QRect(20, 20, 961, 15))
        self.progress.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progress.setAutoFillBackground(False)
        self.progress.setStyleSheet("QProgressBar::chunk{background:qlineargradient("
                                    "spread:pad,x1:0,y1:0,x2:1,y2:0,stop:0 #7CFBFB,stop:1 #E98EE9);}")
        self.progress.setProperty("value", 100)
        self.progress.setTextVisible(False)
        self.progress.setObjectName("progress")
        self.cz_calendar = QtWidgets.QCalendarWidget(self.frame_box)
        self.cz_calendar.setGeometry(QtCore.QRect(715, 70, 271, 225))
        self.cz_calendar.setStyleSheet("")
        self.cz_calendar.setObjectName("cz_calendar")
        self.frame_one = QtWidgets.QFrame(self.frame_box)
        self.frame_one.setGeometry(QtCore.QRect(715, 337, 271, 271))
        self.frame_one.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_one.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_one.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_one.setObjectName("frame_one")
        self.card_manage = QtWidgets.QToolButton(self.frame_one)
        self.card_manage.setGeometry(QtCore.QRect(140, 140, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(9)
        self.card_manage.setFont(font)
        self.card_manage.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.card_manage.setMouseTracking(False)
        self.card_manage.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.card_manage.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.card_manage.setAcceptDrops(False)
        self.card_manage.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.card_manage.setStyleSheet("font: 75 11pt \"Agency FB\";color:#5D94E6;border:none;text-decoration:underline;")
        self.card_manage.setInputMethodHints(QtCore.Qt.ImhNone)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../FQ-Tool/source/icon/search.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.card_manage.setIcon(icon)
        self.card_manage.setIconSize(QtCore.QSize(22, 22))
        self.card_manage.setAutoRepeat(False)
        self.card_manage.setAutoExclusive(False)
        self.card_manage.setAutoRepeatInterval(100)
        self.card_manage.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.card_manage.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.card_manage.setAutoRaise(False)
        self.card_manage.setArrowType(QtCore.Qt.NoArrow)
        self.card_manage.setObjectName("card_manage")
        self.btn_start = QtWidgets.QToolButton(self.frame_one)
        self.btn_start.setGeometry(QtCore.QRect(60, 190, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_start.setFont(font)
        self.btn_start.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_start.setMouseTracking(False)
        self.btn_start.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btn_start.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.btn_start.setAcceptDrops(False)
        self.btn_start.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_start.setStyleSheet("background-color: rgb(0, 229, 168);border-radius:15px;font: 75 14pt 'Agency FB';"
                                     "hover{background-color: rgb(0, 255, 127);}")
        self.btn_start.setInputMethodHints(QtCore.Qt.ImhNone)
        self.btn_start.setIconSize(QtCore.QSize(26, 26))
        self.btn_start.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.btn_start.setAutoRaise(False)
        self.btn_start.setArrowType(QtCore.Qt.NoArrow)
        self.btn_start.setObjectName("btn_start")
        self.GroupBox = QtWidgets.QGroupBox(self.frame_one)
        self.GroupBox.setGeometry(QtCore.QRect(5, 20, 261, 106))
        self.GroupBox.setObjectName("GroupBox")
        self.cz_phone = QtWidgets.QLineEdit(self.GroupBox)
        self.cz_phone.setGeometry(QtCore.QRect(98, 30, 151, 26))
        self.cz_phone.setStyleSheet("padding-left:5px;")
        self.cz_phone.setObjectName("cz_phone")
        self.cz_money_tip = QtWidgets.QLabel(self.GroupBox)
        self.cz_money_tip.setGeometry(QtCore.QRect(18, 66, 71, 26))
        self.cz_money_tip.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.cz_money_tip.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cz_money_tip.setObjectName("cz_money_tip")
        self.cz_money = QtWidgets.QLineEdit(self.GroupBox)
        self.cz_money.setGeometry(QtCore.QRect(98, 66, 151, 26))
        self.cz_money.setStyleSheet("padding-left:5px;")
        self.cz_money.setObjectName("cz_money")
        self.cz_phone_tip = QtWidgets.QLabel(self.GroupBox)
        self.cz_phone_tip.setGeometry(QtCore.QRect(18, 30, 71, 26))
        self.cz_phone_tip.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.cz_phone_tip.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cz_phone_tip.setObjectName("cz_phone_tip")
        self.cz_overdue = QtWidgets.QCheckBox(self.frame_one)
        self.cz_overdue.setGeometry(QtCore.QRect(30, 140, 101, 31))
        self.cz_overdue.setObjectName("cz_overdue")
        self.line = QtWidgets.QFrame(self.frame_box)
        self.line.setGeometry(QtCore.QRect(720, 305, 261, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.frame_main)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 23))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_setting = QtWidgets.QMenu(self.menubar)
        self.menu_setting.setObjectName("menu_setting")
        self.menu_setting_config = QtWidgets.QMenu(self.menu_setting)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("source/icon/setting.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_setting_config.setIcon(icon1)
        self.menu_setting_config.setObjectName("menu_setting_config")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setAcceptDrops(False)
        self.statusbar.setToolTipDuration(-1)
        self.statusbar.setInputMethodHints(QtCore.Qt.ImhNone)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        status_msg = QtWidgets.QLabel('♬ 好好充值，天天向上！')
        status_msg.setStyleSheet("font: 75 9pt \"Agency FB\";")
        self.statusbar.addPermanentWidget(status_msg, stretch=1)
        MainWindow.setStatusBar(self.statusbar)
        self.menu_file_close = QtWidgets.QAction(MainWindow)
        self.menu_file_close.setObjectName("menu_file_close")
        self.menu_setting_open_config = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("source/icon/file.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_setting_open_config.setIcon(icon2)
        self.menu_setting_open_config.setObjectName("menu_setting_open_config")
        self.menu_help_chm = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("source/icon/help.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_help_chm.setIcon(icon3)
        self.menu_help_chm.setIconVisibleInMenu(True)
        self.menu_help_chm.setShortcutVisibleInContextMenu(False)
        self.menu_help_chm.setObjectName("menu_help_chm")
        self.menu_help_version = QtWidgets.QAction(MainWindow)
        self.menu_help_version.setObjectName("menu_help_version")
        self.menu_setting_db = QtWidgets.QAction(MainWindow)
        self.menu_setting_db.setIcon(icon1)
        self.menu_setting_db.setObjectName("menu_setting_db")
        self.menu_setting_oss = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("source/icon/oss.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_setting_oss.setIcon(icon4)
        self.menu_setting_oss.setObjectName("menu_setting_oss")
        self.menu_setting_theme = QtWidgets.QAction(MainWindow)
        self.menu_setting_theme.setObjectName("menu_setting_theme")
        self.menu_setting_bank = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("source/icon/bank_card.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_setting_bank.setIcon(icon5)
        self.menu_setting_bank.setObjectName("menu_setting_bank")
        self.menu_setting_close = QtWidgets.QAction(MainWindow)
        self.menu_setting_close.setObjectName("menu_setting_close")
        self.menu_setting_config.addAction(self.menu_setting_db)
        self.menu_setting.addAction(self.menu_setting_config.menuAction())
        self.menu_setting.addAction(self.menu_setting_open_config)
        self.menu_setting.addSeparator()
        self.menu_setting.addAction(self.menu_setting_bank)
        self.menu_setting.addAction(self.menu_setting_close)
        self.menu_help.addAction(self.menu_help_chm)
        self.menu_help.addAction(self.menu_help_version)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_setting.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "自动化充值"))
        self.console.setHtml(_translate("MainWindow", "！自动化充值工具 Author: biewei<br/>"
                                                      "！使用前请认真阅读帮助手册<br/><br/>"))
        self.cz_overdue.setText(_translate("MainWindow", "逾期标的充值"))
        self.card_manage.setText(_translate("MainWindow", "  充值卡管理  "))
        self.btn_start.setText(_translate("MainWindow", "开始充值"))
        self.GroupBox.setTitle(_translate("MainWindow", "定向充值"))
        self.cz_money_tip.setText(_translate("MainWindow", "充值金额："))
        self.cz_phone_tip.setText(_translate("MainWindow", "手机号码："))
        self.menu_file.setTitle(_translate("MainWindow", "文件(F)"))
        self.menu_setting.setTitle(_translate("MainWindow", "设置(S)"))
        self.menu_setting_config.setTitle(_translate("MainWindow", "配置管理"))
        self.menu_help.setTitle(_translate("MainWindow", "帮助(H)"))
        self.menu_file_close.setText(_translate("MainWindow", "关闭"))
        self.menu_setting_open_config.setText(_translate("MainWindow", "配置文件"))
        self.menu_help_chm.setText(_translate("MainWindow", "使用说明"))
        self.menu_help_version.setText(_translate("MainWindow", "版本"))
        self.menu_setting_db.setText(_translate("MainWindow", "数据库(MySQL)"))
        self.menu_setting_oss.setText(_translate("MainWindow", "云存储(OSS)"))
        self.menu_setting_theme.setText(_translate("MainWindow", "主题"))
        self.menu_setting_bank.setText(_translate("MainWindow", "银行卡"))
        self.menu_setting_close.setText(_translate("MainWindow", "关闭"))


# 主程序逻辑类
class MainWindow(Ui_MainWindow):
    # 程序运行状态
    runState = False
    # 浏览器句柄
    browser = None

    def setupAction(self):
        # ## 主程序事件绑定
        self.btn_start.clicked.connect(self.__run_start)

    # 加载浏览器驱动
    def __load_drive(self):
        admin_login = 'https://www.huishangsuo.com/hss'
        admin_index = 'https://www.huishangsuo.com/Admin/Index/index'
        self.show_log('正在登录后台，请稍等 . . .')
        try:
            if not self.browser:
                ie_options = webdriver.IeOptions()
                ie_options.add_argument('-lang=zh-cn')
                self.browser = webdriver.Ie(options=ie_options)
                page_init = admin_login
            else:
                page_init = admin_index
            # 加载初始页面
            self.browser.get(page_init)
            while admin_index not in self.browser.current_url:
                time.sleep(0.5)
            self.show_log('登录成功!', level='warning')
            return True
        except Exception as e:
            self.browser = None
            self.__log('错误：(%s)' % e, 0)
            return False

    def __run_start(self):
        # 获取当前选中日期, 计算还款时间
        date = self.cz_calendar.selectedDate().toString("yyyy-MM-dd")
        time_array = time.strptime('%s %s' % (date, '23:59:59'), "%Y-%m-%d %H:%M:%S")
        deadline = int(time.mktime(time_array))
        # 获取逾期还款选项
        opt_overdue = self.cz_overdue.isChecked()

        # 开始运行程序
        self.__btn_disable()
        if not self.__load_drive():
            return
        try:
            get_data = GetDataList(deadline, opt_overdue)
            get_data.signal.connect(self.__log)
            get_data.signal2.connect(self.__select_account)
        except Exception as e:
            self.__log('错误：%s' % e, 0)
        else:
            get_data.start()
            self.show_log('正在查询待还款列表，请稍等 . . .')

    # 选择充值账户
    def __select_account(self, data_map):
        self.select_act = SelectAccount()
        self.select_act.signal.connect(self.__log)
        self.select_act.button.accepted.connect(self.__select_card)
        self.select_act.add_check_box(data_map)
        self.select_act.show()

    def __select_card(self):
        if len(self.select_act.resultMap) == 0:
            return
        # 复制数据并销毁窗口资源
        self.account_map = self.select_act.resultMap
        self.select_act.accept()
        self.select_act = None
        # 选择充值银行卡
        self.select_card = SelectCard()
        self.select_card.signal.connect(self.__log)
        self.select_card.button.accepted.connect(self.__work_one)
        self.select_card.add_check_box()
        self.select_card.show()

    def __work_one(self):
        if len(self.select_card.resultMap) == 0:
            return
        # 开启模板匹配线程
        Match = TemplateMatch()
        Match.signal.connect(self.__log)
        Match.start()

        # 开启工作线程
        Work = WorkMain(self.account_map, self.select_card.resultMap)
        Work.signal.connect(self.__log)
        Work.signal2.connect(self.__progress)
        Work.signal3.connect(Match.state_control)
        Work.signal4.connect(Match.close_program)
        Work.browser = self.browser
        Work.start()

        # 关闭银行卡选择窗口
        self.select_card.accept()
        self.select_card = None
        self.show_log('验证完成，开始运行工作 . . .', level='warning')

    def show_log(self, content, level='info'):
        set_style = {
            'warning': 'style=\'color:#ffff00\'',
            'error': 'style=\'color:#FF0000\'',
            'info': ''}
        self.console.append('Hss@root：<span ' + set_style[level] + '>' + content + '</span>')
        QtWidgets.QApplication.processEvents()  # 刷新进程

    def __log(self, msg, status):
        if status in [0, 1]:
            self.__btn_enable()
        if status in [0, 3]:
            level = 'error'
        elif status in [1, 2]:
            level = 'warning'
        else:
            level = 'info'
        self.show_log(msg, level=level)

    def __progress(self, value):
        # 进度条更新
        self.progress.setValue(value)

    def __btn_enable(self):
        # 使控件可操作
        self.runState = False
        self.btn_start.setEnabled(True)

    def __btn_disable(self):
        # 使控件不可操作
        self.runState = True
        self.btn_start.setEnabled(False)


# 模板匹配线程
class TemplateMatch(QtCore.QThread):
    """
    1、该线程和工作线程同时开启
    2、可通过工作线程向该线程发送信号触发图像识别
    """
    # 控制台信号
    signal = QtCore.pyqtSignal(str, int)
    # 银行标识
    bank_code = None
    # U盾密码
    udpass = None
    # 多模型尺寸
    modsize = None
    # 坐标位置(比例换算)
    position = None
    # 图像识别开关
    __open_state = False

    def __init__(self):
        super(TemplateMatch, self).__init__()
        pyautogui.FAILSAFE = False

    # 接收关闭程序信号
    def close_program(self, option):
        if option == 'close':
            self.__open_state = -1

    # 匹配状态控制
    def state_control(self, bank_code, udpass):
        self.bank_code = bank_code
        self.udpass = udpass
        if bank_code == 'ccb':
            self.modsize = [(374, 163), (374, 480)]
            self.position = [(0.53, 0.49, 0.78), (0.5, 0.5, 0.5)]
        elif bank_code == 'icbc':
            self.modsize = [(379, 285), (585, 590)]
            self.position = [(0.53, 0.57, 0.89), (0.5, 0.5, 0.5)]
        else:
            self.signal.emit('错误：银行代码不在可执行列表中，无法进行图像识别！', 3)
            return
        # 打开匹配开关
        self.__open_state = True

    def run(self):
        # 循环监控
        while True:
            if self.__open_state == -1:
                break
            elif self.__open_state != True:
                self.msleep(1000)
            else:
                # 开始截图并进行识别，完成后重置状态
                self.__UShield_password(self.bank_code, self.udpass, self.modsize[0], self.position[0])
                self.__UShield_confirm(self.bank_code, self.modsize[1], self.position[1])
                self.__open_state = False

    # U盾确密码输入
    def __UShield_password(self, bank_code, udpass, modsize, position):
        """
        :param bank_code: 银行代码(ccb/icbc/...)
        :param udpass: 当前操作银行卡的U盾密码(str类型)
        :param modsize: 当前使用模板图片的宽高(width, height)
        :param position: 需要依次点击的位置相对于模板的比例(left, top1, top2)
        注意：模板名称基于银行代码查找，请务必填写正确。
        """
        self.msleep(500)
        # 模板位置(密码输入模板)
        model_path = 'source/model/%s_01.png' % bank_code
        # 获取需要依次点击的坐标系(基于显示屏)
        match_result = self.__get_coordinate(model_path, modsize, position)
        if match_result == False:
            # ## 无匹配结果则继续匹配
            self.__UShield_password(bank_code, udpass, modsize, position)
        else:
            left, top1, top2 = match_result
            # 窗口获取焦点并输入密码
            pyautogui.click(x=left, y=top1, button='left')
            self.msleep(300)
            pyautogui.press([k for k in udpass])
            self.msleep(300)
            pyautogui.click(x=left, y=top2, button='left')
            return True

    # U盾按钮确认
    def __UShield_confirm(self, bank_code, modsize, position):
        self.msleep(500)
        model_path = 'source/model/%s_02.png' % bank_code
        # 获取需要依次点击的坐标系(基于显示屏)
        match_result = self.__get_coordinate(model_path, modsize, position)
        if match_result == False:
            self.__UShield_confirm(bank_code, modsize, position)
        else:
            print('请按U盾确认，当前银行代码为：%s' % bank_code)
            return True

    # 获取要点击的坐标系
    def __get_coordinate(self, model_path, modsize, position):
        """
        :param model_path: 当前选择模型存放位置
        :param modsize: 当前选择模型的宽高(width, height)
        :param position: 需要依次点击的位置相对于模板的比例(left, top1, top2)
        :return:
        """
        # 屏幕全屏截图
        screenshot = ImageGrab.grab()
        # openCV 加载截图并转换为灰度图
        img_gray = cv2.cvtColor(np.asarray(screenshot), cv2.COLOR_RGB2GRAY)
        # 加载要匹配的模板
        Template = cv2.imread(model_path, 0)
        MW, MH = Template.shape[::-1]

        # 将灰度图全部转换为二值图
        # gray_ret, gray_binary = cv2.threshold(img_gray, 120, 255, cv2.THRESH_BINARY)
        # tpl_ret, tpl_binary = cv2.threshold(Template, 120, 255, cv2.THRESH_BINARY)

        # ## 对原始灰度图像和图像模板进行匹配
        res = cv2.matchTemplate(img_gray, Template, cv2.TM_CCOEFF_NORMED)
        # 找到最大值和最小值
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if max_val < 0.90:  # 匹配度小于90%时不接受
            return False

        print('匹配准确度：' + str(max_val))
        # 定位需要点击的各个位置(基于显示屏)
        left = int(max_loc[0] + (MW * position[0]))
        top1 = int(max_loc[1] + (MH * position[1]))
        top2 = int(max_loc[1] + (MH * position[2]))
        return left, top1, top2


# 主工作线程
class WorkMain(QtCore.QThread):
    # 控制台信号
    signal = QtCore.pyqtSignal(str, int)
    # 进度条信号
    signal2 = QtCore.pyqtSignal(float)
    # 模板匹配线程状态控制信号
    signal3 = QtCore.pyqtSignal(str, str)
    # 模板匹配线程关闭信号
    signal4 = QtCore.pyqtSignal(str)

    # 汇商所服务器域名
    hss_host = 'https://www.huishangsuo.com'
    # 宜宾确认密码页面
    yb_pass = 'https://icdsp.ibank.ybccb.com/p2ph5/pc/checkPassword.html'
    # 宜宾选择银行页面
    yb_bank = 'https://tppsgw.ibank.ybccb.com:5188/devportal/pages/userCenter/YiBinIndex.jsp'

    # 窗口操作句柄
    browser = None
    # 银行卡集合
    __cards = {}
    # 充值账户集合
    __act_map = {}

    def __init__(self, act_map, cards, parent=None):
        super(WorkMain, self).__init__(parent)
        self.__act_map = act_map
        self.__cards = cards

    def run(self):
        self.msleep(500)
        try:
            self.__run_main()
        except Exception as e:
            self.signal.emit('错误(001)：%s' % e, 0)
        finally:
            self.signal4.emit('close')

    def __run_main(self):
        # 开始发送任务
        acct_keys = sorted(self.__act_map.keys())
        card_keys = sorted(self.__cards.keys())
        acct_num = len(acct_keys)
        card_num = len(card_keys)
        # 发送提示信号到主程序界面
        self.signal.emit('程序开始运行，本次任务共 %s 条，使用银行卡 %s 张。'
                         % (acct_num, card_num), 2)

        """ 计算每张卡的充值额度 """
        card_index = 0
        for i in range(acct_num):
            capital = self.__act_map[acct_keys[i]]['capital']
            interest = self.__act_map[acct_keys[i]]['interest']
            act_money = self.__act_map[acct_keys[i]]['act_money']
            benxi = round(capital + interest, 2)
            money = round(benxi - act_money, 2)
            if money <= 0:
                money = 0
            if 'amount' not in self.__cards[card_keys[card_index]]:
                self.__cards[card_keys[card_index]]['amount'] = money
            else:
                self.__cards[card_keys[card_index]]['amount'] += money
            card_index += 1
            if card_index == card_num:
                card_index = 0

        for card in self.__cards:
            self.signal.emit('%s[%s] 本次分配金额为(%s)元' % (
                self.__cards[card]['name'], self.__cards[card]['number'],
                self.__cards[card]['amount']), 2)
        """ 计算每张卡的充值额度 """

        card_index = 0
        Progress = 0
        for k in acct_keys:
            # 发送进度条到主程序
            self.signal2.emit(round(Progress / acct_num * 100, 2))
            Progress += 1
            """ ---------- 充值卡选择 ----------- """
            card_info = self.__cards[card_keys[card_index]]
            card_index += 1
            if card_index == card_num:
                card_index = 0
            """ ---------- 充值卡选择 ----------- """
            borrow_id = self.__act_map[k]['borrow_id']
            borrow_uid = self.__act_map[k]['borrow_uid']
            capital = self.__act_map[k]['capital']
            interest = self.__act_map[k]['interest']
            sort_order = self.__act_map[k]['sort_order']
            total = self.__act_map[k]['total']
            user_name = self.__act_map[k]['user_name']
            act_money = self.__act_map[k]['act_money']
            idcard = str(self.__act_map[k]['idcard']).strip()
            if len(idcard) != 18:
                self.signal.emit('第 %s 号标, 账户[%s]身份证号码[%s]格式错误！'
                                 % (borrow_id, user_name, idcard), 3)
                continue
            # 获取用户支付密码
            if idcard[17:18].upper() == 'X':
                my_pwd = idcard[11:17]
            else:
                my_pwd = idcard[12:18]
            # 账户余额检查
            benxi = round(capital + interest, 2)
            money = round(benxi - act_money, 2)
            if money <= 0:
                self.signal.emit('第 %s 号标第 %s/%s 期需还本息共 %s, 账户[%s]余额 %s, 跳过 . . .'
                                 % (borrow_id, sort_order, total, benxi, user_name, act_money), 2)
                continue

            """ ---------------------------------------------------------------------- """
            """ ---------------------- 发送充值指令到浏览器 -------------------------- """
            """ ---------------------------------------------------------------------- """
            self.signal.emit('第 %s 号标第 %s/%s 期需还本息共 %s, 账户[%s]余额 %s, 开始充值 . . .'
                             % (borrow_id, sort_order, total, benxi, user_name, act_money), 9)
            # 切换句柄到主窗口
            self.browser.get(self.hss_host + '/Admin/CapitalRepay/admin_charge?uid=%s&money=%s'
                             % (borrow_uid, money))
            # 确认密码页面监控
            while self.yb_pass not in str(self.browser.current_url):
                self.msleep(300)
            # 获取密码框
            inputPwd = None
            while not inputPwd:
                inputPwd = self.browser.find_element_by_id('inputPwd')
                self.msleep(200)
            # 弹出软键盘并获取值
            if inputPwd.click() != 0:
                self.msleep(300)
                pwd_list = self.browser.find_elements_by_class_name('keys')
                pwd_map = {
                    # 密码按键集合，以密码值为键
                }
                for pwd_btn in pwd_list:
                    val = pwd_btn.get_attribute('value')
                    pwd_map['num_%s' % val] = pwd_btn
                # 点击输入密码
                for i in range(6):
                    self.browser.execute_script("arguments[0].click();", pwd_map['num_%s' % my_pwd[i]])

                # 点击确认按钮 'btn-success'
                while True:
                    if len(inputPwd.get_attribute('value')) == 6:
                        pwd_queren = self.browser.find_element_by_class_name('btn-success')
                        self.browser.execute_script("arguments[0].click();", pwd_queren)
                        break
                    else:
                        self.msleep(200)

                # 密码错误状态监控
                pwd_status = None
                state_step = 1
                while self.yb_pass in str(self.browser.current_url):
                    try:
                        if state_step == 1:
                            adopt = self.browser.find_element_by_class_name('btn-primary')
                            if adopt.text == '确定':
                                self.browser.execute_script("arguments[0].click();", adopt)
                                break
                        else:
                            pwd_err = self.browser.find_element_by_class_name('k-field-display')
                            if pwd_err.text in [
                                '密码不正确',
                                '密码校验未通过',
                                '请求超时，验签失败！',
                                '密码已锁定，今日24:00解锁'
                            ]:
                                pwd_status = 'error_pass'
                                break
                    except:
                        self.msleep(100)
                    finally:
                        # 检测步骤循环流转
                        state_step = 2 if state_step == 1 else 1

                # 密码错误则直接报错并跳过
                if pwd_status == 'error_pass':
                    self.signal.emit('错误：支付密码校验未通过！', 3)
                    continue
                # 选择银行页面跳转监控
                while self.yb_bank not in str(self.browser.current_url):
                    self.msleep(100)

                # 点击选择银行
                select_bank = None
                while not select_bank:
                    try:
                        select_bank = self.browser.find_element_by_xpath("//div[text()='%s']" % card_info['name'])
                        break
                    except:
                        self.msleep(100)
                self.browser.execute_script("arguments[0].click();", select_bank)

                """ ---------------------------------------------------------------------- """
                """ --------------------- 下方根据不同的银行单独处理 --------------------- """
                if card_info['code'] == 'CCB':  # 建设银行
                    (res, state) = self.__ccb_process(card_info)
                elif card_info['code'] == 'ICBC':  # 工商银行
                    (res, state) = self.__icbc_process(card_info)
                else:
                    self.signal.emit('银行选择失败：card_info_len(%s), card_info["code"](%s), code_type(%s)'
                                     % (len(card_info), card_info['code'], type(card_info['code'])), 3)
                    continue
                # 单个任务处理完成
                self.signal.emit('处理完成，返回信息：%s' % str(res), state)

        # 全部任务处理完成
        self.signal2.emit(100.00)
        self.signal.emit('任务完成！', 1)

    # 工商银行操作过程
    def __icbc_process(self, card):
        page_one = 'https://b2c.icbc.com.cn/servlet/ICBCEPCCEBizServlet'
        page_two = 'https://b2c.icbc.com.cn/servlet/ICBCINBSReqServlet'
        while page_one not in str(self.browser.current_url):
            self.msleep(200)
        try:
            self.sleep(1)
            # 选择U盾支付
            self.browser.find_element_by_id('paytype3').click()
            self.sleep(1)
            # 自动输入账号
            self.browser.find_element_by_id('paycard_h').send_keys(card['number'])
            # 点击下一步
            self.browser.find_element_by_id('acPayNext').click()
            # # # - - - 支付页面跳转监控 - - - # # #
            while page_two not in str(self.browser.current_url):
                self.msleep(200)
            # 点击支付按钮事件/提交表单
            self.sleep(1)
            self.browser.execute_script('javascript:mysubmit();')
            # 发送信号开启模板匹配
            self.signal3.emit('icbc', card['udpass'])
            self.sleep(1)
            self.browser.execute_script('javascript:formcheck();')
            # 循环监控防报错
            self.__monitoring_page()
            resp_context = '充值成功！'
            # 此处先假设为充值成功，后期完善
            resp_msg = (resp_context or '充值未提交！', 2)
        except Exception as e:
            resp_msg = ('err: %s' % e, 3)
            print('err（101）：', e)
        finally:
            return resp_msg

    # 页面URL检测(防止alert报错)
    def __monitoring_page(self):
        self.sleep(1)
        try:
            # 循环监控支付页面是否被跳转
            # 倒计时结束跳转页面URL: 'https://gw.baofoo.com/merchant_page'
            page_current = 'https://b2c.icbc.com.cn/servlet/ICBCINBSReqServlet'
            while page_current in str(self.browser.current_url):
                self.msleep(100)
            return True
        except:
            self.__monitoring_page()

    # ## 建设银行操作过程
    def __ccb_process(self, card):
        page_one = 'https://ibsbjstar.ccb.com.cn/CCBIS/CCBWLReqServlet'
        resp_msg = ('出错啦，跳过！', 3)
        try:
            while page_one not in str(self.browser.current_url):
                self.msleep(200)
            # 切换句柄到 iframe
            self.sleep(1)
            self.browser.switch_to_frame('mainframe')
            self.browser.execute_script('javascript:type_onclick(0);')
            # 登录网银
            select_input_step = 1
            while True:
                try:
                    self.browser.find_element_by_name('USERID').send_keys(card['number'])
                    self.browser.find_element_by_name('LOGPASS').send_keys(card['password'])
                    break
                except:
                    if select_input_step % 3 == 0:
                        resp_msg = ('自动填写账号密码失败，跳过！', 3)
                        return resp_msg
                    select_input_step += 1
                finally:
                    self.msleep(500)

            # 下一步
            try:
                self.msleep(500)
                self.browser.find_element_by_name('Submit').click()
            except Exception as e:
                print('请手动点击下一步：%s' % e)

            # 发送信号开启模板匹配
            self.signal3.emit('ccb', card['udpass'])
            self.sleep(1)
            # 支付确认
            while True:
                try:
                    btn_zhifu = self.browser.find_element_by_name('Submit')
                    btn_val = str(btn_zhifu.get_attribute('value'))
                    if btn_val == '支 付':
                        self.msleep(300)
                        btn_zhifu.click()
                        break
                except Exception as e:
                    print('错误(003)：%s' % e)
                    self.msleep(300)

            # 充值完成
            trans_success = None
            while not trans_success:
                try:
                    trans_success = self.browser.find_element_by_id('rspDesc')
                except:
                    self.msleep(1000)
            # ## 成功之后的节点元素
            resp_msg = (trans_success.text, 2)
            return resp_msg
        except Exception as e:
            resp_msg = ('err: ' % str(e), 3)
            print('错误(004)：%s' % str(e))
            return resp_msg
        finally:
            # 切回句柄到主窗口
            self.browser.switch_to_default_content()






