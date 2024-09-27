import os
import platform
import re
import subprocess
from pathlib import Path
from typing import Union

FFMPEG_DIR = os.path.join(os.path.dirname(__file__), 'ffmpeg')
if platform.system() == 'Linux':
    FFMPEG_EXE = os.path.join(FFMPEG_DIR, 'ffmpeg')
    ENCODING = 'UTF-8'
else:
    FFMPEG_EXE = os.path.join(FFMPEG_DIR, 'ffmpeg.exe')
    ENCODING = 'GBK'


def get_video_info(video_path: Union[str, Path]) -> tuple:
    """
    获取视频信息

    :params video_path: 视频路径
    """
    p = subprocess.Popen([FFMPEG_EXE, '-i', video_path, '-hide_banner'],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    video_info_str = p.stderr.read().decode(ENCODING)
    print(video_info_str)
    video_info_re = (r'.+Duration: ([\d:\.]+), start.+bitrate: (\d+) kb/s.+'
                     r'Video: (.+?) .+, (\d+?)x(\d+?) .+')
    res = re.match(video_info_re, video_info_str, flags=re.DOTALL)
    if res:
        return res.groups()
    return None


def convert_video(source_video_path: Union[str, Path], out_video_path: Union[str, Path],
                  source_video_encode: str = None, out_video_encode: str = None,
                  out_video_format: str = None, out_video_bitrate: str = None,
                  out_video_fps: str = None, out_video_res: str = None):
    """
    视频转换

    :params source_video_path: 源视频路径
    :params out_video_path: 输出视频路径
    :params source_video_encode: 源视频编码
    :params out_video_encode: 输出视频编码
    :params out_video_format: 输出视频格式
    :params out_video_bitrate: 输出视频码率
    :params out_video_fps: 输出视频帧率
    :params out_video_res: 输出视频分辨率
    """
    cmd = [FFMPEG_EXE, '-c:v', source_video_encode,
           '-i', source_video_path, '-hide_banner']
    if out_video_encode:
        cmd.append('-c:v')
        cmd.append(out_video_encode)
    if out_video_format:
        cmd.append('-f')
        cmd.append(out_video_format)
    if out_video_bitrate:
        cmd.append('-b:v')
        cmd.append(out_video_bitrate)
    if out_video_fps:
        cmd.append('-r')
        cmd.append(out_video_fps)
    if out_video_res:
        cmd.append('-s')
        cmd.append(out_video_res)
    cmd.append(out_video_path)
    print(' '.join(cmd))
    # p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


if __name__ == '__main__':
    get_video_info('/mnt/c/Users/sjdd/Downloads/Crab_Rave.mp4')
