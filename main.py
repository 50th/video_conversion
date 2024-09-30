# -*- coding: utf-8 -*-
"""
视频转码主程序
"""
import logging
import os
import queue
import sys

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog

# 导入 designer 工具生成的模块
from VideoConversion_ui import Ui_VideoConversionWindow
from utils.video_operator import VideoOperator

VIDEO_FORMATS = ['avi', 'flv', 'mp4', 'mkv']
VIDEO_ENCODINGS = ['h264', 'h265']

logger = logging.getLogger(__name__)


class MainForm(QMainWindow, Ui_VideoConversionWindow):
    """QT 主页面"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.select_video_btn.clicked.connect(self.select_source_video_dialog)
        self.encode_comb_box.addItems(VIDEO_ENCODINGS)
        self.format_comb_box.addItems(VIDEO_FORMATS)
        self.out_video_btn.clicked.connect(self.select_out_video_dir_dialog)
        self.conversion_video_btn.clicked.connect(self.conversion_video)

        self.source_video_path = None
        self.video_operator = None
        self.out_video_dir = None
        self.out_video_path = None

        self.convert_progress_timer = None

    def select_source_video_dialog(self):
        """选择原视频"""
        video_formats = f'视频类型 ({" ".join("*." + _ for _ in VIDEO_FORMATS)})'
        video_path, _ = QFileDialog.getOpenFileName(self, '选择视频',
                                                    filter=video_formats)
        if video_path:
            print(video_path)
            self.video_operator = VideoOperator(video_path)
            if self.video_operator.video_info:
                self.source_video_path = video_path
                self.video_info_label.setText(
                    str(self.video_operator.video_info))

    def select_out_video_dir_dialog(self):
        """选择输出目录"""
        dir_path = QFileDialog.getExistingDirectory(self, '选择输出目录',
                                                    './out_videos')
        if dir_path:
            self.out_video_dir = dir_path

    def conversion_video(self):
        """转换视频"""
        print(self.source_video_path)
        print(self.out_video_dir)
        if not self.out_video_dir:
            self.out_video_dir = './out_videos'
        os.makedirs(self.out_video_dir, exist_ok=True)
        if self.source_video_path and self.out_video_dir:
            video_name = os.path.basename(self.source_video_path)
            self.out_video_path = os.path.join(
                self.out_video_dir,
                f'{os.path.splitext(video_name)[0]}.{self.format_comb_box.currentText()}'
            )
            print(self.out_video_path)
            self.video_operator.convert_video(
                self.out_video_path,
                # out_video_encode=self.encode_comb_box.currentText(),
                out_video_encode='hevc_qsv',  # 暂时固定为 hevc_qsv，intel 核显加速
                out_video_format=self.format_comb_box.currentText(),
                out_video_bitrate=self.video_operator.video_info.bitrate,
            )
            # 禁用视频选择按钮和视频转换按钮
            self.select_video_btn.setEnabled(False)
            self.conversion_video_btn.setEnabled(False)
            # 创建定时器，每 500ms 读取一次进度
            self.convert_progress_timer = QTimer()
            self.convert_progress_timer.timeout.connect(self.load_convert_progress)
            self.convert_progress_timer.start(500)

    def load_convert_progress(self):
        """读取队列中转换进度"""
        try:
            progress = self.video_operator.progress_q.get_nowait()
        except queue.Empty:
            return
        self.convert_progress_bar.setValue(progress)
        if progress >= 100:
            self.convert_progress_timer.stop()
            # 恢复视频选择按钮和视频转换按钮
            self.select_video_btn.setEnabled(True)
            self.conversion_video_btn.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 初始化
    myWin = MainForm()
    # 将窗口控件显示在屏幕上
    myWin.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
