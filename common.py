#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from configparser import ConfigParser
from random import choice as r_choice
from random import randint


class MyConfigParser(ConfigParser):
    """
    重写该类，区分大小写
    """
    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr


class Helper(object):

    def __init__(self):
        pass

    @staticmethod
    def readQss(style):
        with open(style, 'r') as f:
            return f.read()

    @staticmethod
    def createPhone():
        phone_fix = [
            130, 131, 132, 133, 134, 135, 136, 137, 138, 139,
            144, 147, 148, 146,
            150, 151, 152, 153, 155, 156, 157, 158, 159,
            166,
            176, 177, 178,
            180, 181, 182, 183, 184, 185, 186, 187, 188, 189,
            199, 198
        ]
        return str(r_choice(phone_fix)) + str(randint(1000, 9999)) + str(randint(1000, 9999))

