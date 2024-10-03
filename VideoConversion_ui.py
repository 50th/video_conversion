# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VideoConversion.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
    QProgressBar, QPushButton, QSizePolicy, QWidget)

class Ui_VideoConversionWindow(object):
    def setupUi(self, VideoConversionWindow):
        if not VideoConversionWindow.objectName():
            VideoConversionWindow.setObjectName(u"VideoConversionWindow")
        VideoConversionWindow.resize(717, 304)
        self.select_video_btn = QPushButton(VideoConversionWindow)
        self.select_video_btn.setObjectName(u"select_video_btn")
        self.select_video_btn.setGeometry(QRect(20, 10, 91, 31))
        self.video_name_label = QLabel(VideoConversionWindow)
        self.video_name_label.setObjectName(u"video_name_label")
        self.video_name_label.setGeometry(QRect(20, 60, 671, 21))
        self.encode_comb_box = QComboBox(VideoConversionWindow)
        self.encode_comb_box.setObjectName(u"encode_comb_box")
        self.encode_comb_box.setGeometry(QRect(20, 140, 121, 31))
        self.format_comb_box = QComboBox(VideoConversionWindow)
        self.format_comb_box.setObjectName(u"format_comb_box")
        self.format_comb_box.setGeometry(QRect(160, 140, 121, 31))
        self.out_video_btn = QPushButton(VideoConversionWindow)
        self.out_video_btn.setObjectName(u"out_video_btn")
        self.out_video_btn.setGeometry(QRect(300, 140, 101, 31))
        self.conversion_video_btn = QPushButton(VideoConversionWindow)
        self.conversion_video_btn.setObjectName(u"conversion_video_btn")
        self.conversion_video_btn.setGeometry(QRect(420, 140, 101, 31))
        self.convert_progress_bar = QProgressBar(VideoConversionWindow)
        self.convert_progress_bar.setObjectName(u"convert_progress_bar")
        self.convert_progress_bar.setEnabled(True)
        self.convert_progress_bar.setGeometry(QRect(20, 180, 671, 31))
        self.convert_progress_bar.setMinimum(0)
        self.convert_progress_bar.setValue(0)
        self.convert_progress_bar.setTextVisible(True)
        self.video_info_label = QLabel(VideoConversionWindow)
        self.video_info_label.setObjectName(u"video_info_label")
        self.video_info_label.setGeometry(QRect(20, 90, 671, 21))

        self.retranslateUi(VideoConversionWindow)

        QMetaObject.connectSlotsByName(VideoConversionWindow)
    # setupUi

    def retranslateUi(self, VideoConversionWindow):
        VideoConversionWindow.setWindowTitle(QCoreApplication.translate("VideoConversionWindow", u"VideoConversion", None))
        self.select_video_btn.setText(QCoreApplication.translate("VideoConversionWindow", u"\u9009\u62e9\u89c6\u9891", None))
        self.video_name_label.setText("")
        self.out_video_btn.setText(QCoreApplication.translate("VideoConversionWindow", u"\u8f93\u51fa\u8def\u5f84", None))
        self.conversion_video_btn.setText(QCoreApplication.translate("VideoConversionWindow", u"\u8f6c\u6362", None))
        self.video_info_label.setText("")
    # retranslateUi

