# -*- coding: utf-8 -*-
import asyncio
import os
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog

# 导入designer工具生成的login模块
from VideoConversion_ui import Ui_VideoConversionWindow
from utils.ffmpeg_handler import convert_video, get_video_info, run_ffmpeg_command

VIDEO_FORMATS = ['avi', 'flv', 'mp4', 'mkv']
VIDEO_ENCODINGS = ['h264', 'h265']


class MainForm(QMainWindow, Ui_VideoConversionWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.select_video_btn.clicked.connect(self.select_source_video_dialog)
        self.encode_comb_box.addItems(VIDEO_ENCODINGS)
        self.format_comb_box.addItems(VIDEO_FORMATS)
        self.out_video_btn.clicked.connect(self.select_out_video_dir_dialog)
        self.conversion_video_btn.clicked.connect(self.conversion_video)

        self.source_video_path = None
        self.out_video_dir = None
        self.out_video_path = None

    def select_source_video_dialog(self):
        """选择原视频"""
        video_formats = f'视频类型 ({" ".join("*." + _ for _ in VIDEO_FORMATS)})'
        video_path, _ = QFileDialog.getOpenFileName(
            self, '选择视频', filter=video_formats)
        if video_path:
            print(video_path)
            video_info = get_video_info(video_path)
            if video_info:
                self.source_video_path = video_path
                self.video_info_label.setText(str(video_info))
                # self.format_comb_box.setCurrentText(video_info[0])

    def select_out_video_dir_dialog(self):
        """选择输出目录"""
        dir_path = QFileDialog.getExistingDirectory(
            self, '选择输出目录', './out_videos')
        if dir_path:
            self.out_video_dir = dir_path

    def conversion_video(self):
        """转换视频"""
        print(self.source_video_path)
        print(self.out_video_dir)
        if not self.out_video_dir:
            self.out_video_dir = './out_videos'
        if self.source_video_path and self.out_video_dir:
            self.out_video_path = os.path.join(
                self.out_video_dir,
                f'{os.path.splitext(os.path.basename(self.source_video_path))[0]}.{self.format_comb_box.currentText()}'
            )
            print(self.out_video_path)
            # if os.path.exists(self.out_video_path):
            #     return
            # res = convert_video(self.source_video_path, self.out_video_path,
            #                     source_video_encode='h264_qsv',
            #                     out_video_encode=self.encode_comb_box.currentText(),
            #                     out_video_format=self.format_comb_box.currentText())
            # for out, err in res:
            #     print('out:', out)
            #     print('err:', err)
            asyncio.run(run_ffmpeg_command(self.source_video_path, self.out_video_path,
                                           source_video_encode='h264_qsv',
                                           out_video_encode=self.encode_comb_box.currentText(),
                                           out_video_format=self.format_comb_box.currentText()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 初始化
    myWin = MainForm()
    # 将窗口控件显示在屏幕上
    myWin.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
