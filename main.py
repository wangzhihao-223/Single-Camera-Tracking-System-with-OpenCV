#!/usr/bin/python3
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)
import cv2
import platform
import time
import numpy as np
from core.ui_setup import Ui_MainWindow # 用户界面代码
from core import (camera,ui_setup)  # 开启摄像头功能
import processing.algorithm as algorithm # 加载预处理和跟踪算法
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)



if __name__ == '__main__':
    app = QApplication([])
    win = QMainWindow()
    # 声明ui对象
    ui = Ui_MainWindow() # 初始化一个window实例
    ui.setupUi(win)
    win.show()
    # 执行app应用
    app.exec()