# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VideoConversion.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_VideoConversionWindow(object):
    def setupUi(self, VideoConversionWindow):
        if not VideoConversionWindow.objectName():
            VideoConversionWindow.setObjectName(u"VideoConversionWindow")
        VideoConversionWindow.resize(519, 406)
        self.select_video_btn = QPushButton(VideoConversionWindow)
        self.select_video_btn.setObjectName(u"select_video_btn")
        self.select_video_btn.setGeometry(QRect(10, 10, 91, 41))
        self.video_info_label = QLabel(VideoConversionWindow)
        self.video_info_label.setObjectName(u"video_info_label")
        self.video_info_label.setGeometry(QRect(20, 60, 351, 41))
        self.ecode_comb_box = QComboBox(VideoConversionWindow)
        self.ecode_comb_box.setObjectName(u"ecode_comb_box")
        self.ecode_comb_box.setGeometry(QRect(20, 120, 101, 22))
        self.format_comb_box = QComboBox(VideoConversionWindow)
        self.format_comb_box.setObjectName(u"format_comb_box")
        self.format_comb_box.setGeometry(QRect(150, 120, 101, 22))
        self.out_video_btn = QPushButton(VideoConversionWindow)
        self.out_video_btn.setObjectName(u"out_video_btn")
        self.out_video_btn.setGeometry(QRect(280, 120, 91, 41))
        self.conversion_video_btn = QPushButton(VideoConversionWindow)
        self.conversion_video_btn.setObjectName(u"conversion_video_btn")
        self.conversion_video_btn.setGeometry(QRect(400, 120, 91, 41))

        self.retranslateUi(VideoConversionWindow)

        QMetaObject.connectSlotsByName(VideoConversionWindow)
    # setupUi

    def retranslateUi(self, VideoConversionWindow):
        VideoConversionWindow.setWindowTitle(QCoreApplication.translate("VideoConversionWindow", u"VideoConversion", None))
        self.select_video_btn.setText(QCoreApplication.translate("VideoConversionWindow", u"\u9009\u62e9\u89c6\u9891", None))
        self.video_info_label.setText(QCoreApplication.translate("VideoConversionWindow", u"\u8bf7\u9009\u62e9\u89c6\u9891", None))
        self.out_video_btn.setText(QCoreApplication.translate("VideoConversionWindow", u"\u8f93\u51fa\u8def\u5f84", None))
        self.conversion_video_btn.setText(QCoreApplication.translate("VideoConversionWindow", u"\u8f6c\u6362", None))
    # retranslateUi

