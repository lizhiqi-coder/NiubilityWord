# coding:utf-8

try:
    from PySide.QtCore import *
    from PySide.QtGui import *
except ImportError:
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *

import platform
import os


def bindStyleSheet(ref, style_sheet):
    style_file = QFile(style_sheet)
    style_file.open(QFile.ReadOnly)
    static_style_sheet = str(style_file.readAll())
    ref.setStyleSheet(static_style_sheet)


PLATFROM_WINDOWS = 'Windows'
PLATFROM_LINUX = 'Linux'


def getPlatform():
    if platform.system() == PLATFROM_WINDOWS:
        return PLATFROM_WINDOWS
    else:
        return PLATFROM_LINUX


def containsChinese(str):
    for ch in str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True

    return False


ROOT_DIR_NAME = 'NiubilityWord'


def getRootDir():
    dir = os.getcwd()
    while not dir.endswith(ROOT_DIR_NAME):
        temp_dir = dir
        dir = os.path.abspath(os.path.join(dir, os.pardir))
        if dir == temp_dir:
            return None
    return dir


def parseHtml(html_path):
    html_file = open(html_path, 'r')
    result = html_file.read()
    html_file.close()
    return unicode(result, 'utf-8')


if __name__ == '__main__':
    print getPlatform()
