# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect_me.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
# 导入程序运行必须模块
import os
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog

# 导入designer工具生成的login模块
from VideoConversion_ui import Ui_VideoConversionWindow
from utils.ffmpeg_handler import get_video_info

VIDEO_FORMATS = ['avi', 'flv', 'mp4', 'mkv']
VIDEO_ENCODINGS = ['h264', 'h265']


class MainForm(QMainWindow, Ui_VideoConversionWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.select_video_btn.clicked.connect(self.show_file_dialog)
        self.ecode_comb_box.addItems(VIDEO_ENCODINGS)
        self.format_comb_box.addItems(VIDEO_FORMATS)
        self.out_video_btn.clicked.connect(self.show_dir_dialog)
        self.conversion_video_btn.clicked.connect(self.conversion_video)

        self.source_video_path = None
        self.out_video_dir = None
        self.out_video_path = None

    def accept(self):
        print('确定')

    def reject(self):
        print('取消')

    def show_file_dialog(self):
        video_formats = f'视频类型 ({" ".join("*." + _ for _ in VIDEO_FORMATS)})'
        file_path, _ = QFileDialog.getOpenFileName(
            self, '选择视频', filter=video_formats)
        if file_path:
            print(file_path)
            video_info = get_video_info(file_path)
            if video_info:
                self.source_video_path = file_path
                video_name = os.path.basename(file_path)
                video_info_text = f'{video_name}: ' + ', '.join(video_info)
                self.video_info_label.setText(video_info_text)

    def show_dir_dialog(self):
        dir_path = QFileDialog.getExistingDirectory(
            self, '选择输出目录', './out_videos')
        if dir_path:
            self.out_video_dir = dir_path

    def conversion_video(self):
        print(self.source_video_path)
        print(self.out_video_dir)
        if self.source_video_path and self.out_video_dir:
            self.out_video_path = os.path.join(
                self.out_video_dir,
                f'{os.path.splitext(os.path.basename(self.source_video_path))[0]}.mp4'
            )
            print(self.out_video_path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 初始化
    myWin = MainForm()
    # 将窗口控件显示在屏幕上
    myWin.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
