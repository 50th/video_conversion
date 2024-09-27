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
    print('err:', video_info_str)
    res = re.match(r'.+Duration: ([\d:\.]+), start.+bitrate: (\d+) kb/s.+Video: (.+?) .+, (\d+?)x(\d+?) .+', video_info_str, flags=re.DOTALL)
    if res:
        print(res.groups())
        return res.groups()
    return None


if __name__ == '__main__':
    get_video_info('/mnt/c/Users/sjdd/Downloads/Crab_Rave.mp4')
