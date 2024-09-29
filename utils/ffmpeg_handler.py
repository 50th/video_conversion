import asyncio
import dataclasses
import os
import platform
import re
import subprocess
import threading
from pathlib import Path
from typing import Union

FFMPEG_DIR = os.path.join(os.path.dirname(__file__), 'ffmpeg')
if platform.system() == 'Linux':
    FFMPEG_EXE = os.path.join(FFMPEG_DIR, 'ffmpeg')
    ENCODING = 'UTF-8'
else:
    FFMPEG_EXE = os.path.join(FFMPEG_DIR, 'ffmpeg.exe')
    ENCODING = 'GBK'


@dataclasses.dataclass
class VideoInfo:
    """视频信息"""
    video_name: str
    duration: str
    duration_time: float
    bitrate: str
    encoding: str
    width: str
    height: str
    fps: int

    def __str__(self) -> str:
        return (f'视频名称：{self.video_name}；'
                f'视频时长：{self.duration}；'
                f'视频编码：{self.encoding}；'
                f'视频分辨率：{self.width}x{self.height}；'
                f'视频帧率：{self.fps}')


def get_video_info(video_path: Union[str, Path]) -> VideoInfo:
    """
    获取视频信息

    :params video_path: 视频路径
    """
    cmd = [FFMPEG_EXE, '-i', video_path, '-hide_banner']
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    video_info_str = p.stderr.read().decode(ENCODING)
    p.stderr.close()
    video_info_re = (r'.+Duration: (?P<duration>\d+:\d+:\d+.\d+), start.+'
                     r'bitrate: (?P<bitrate>\d+) kb/s.+'
                     r'Video: (?P<encoding>.+?) .+, (?P<width>\d+?)x(?P<height>\d+?)'
                     r' .+, (?P<fps>\d+) fps,.+')
    match_res = re.match(video_info_re, video_info_str, flags=re.DOTALL)
    if match_res:
        hours, minutes, seconds = map(
            float, match_res.groupdict()['duration'].split(':'))
        duration_time = hours * 3600 + minutes * 60 + seconds
        video_info = VideoInfo(
            video_name=os.path.basename(video_path),
            duration_time=duration_time,
            **match_res.groupdict())
        return video_info
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
    cmd.append('-y')
    print(cmd)
    print(' '.join(cmd))
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stderr_thread = threading.Thread(target=stream_reader, args=(p.stderr,))
    stderr_thread.start()
    # while p.poll() is None:
    #     out = p.stderr.readline().decode(ENCODING)
    #     err = p.stderr.readline().decode(ENCODING)
    #     yield out, err


# 预先设置视频总时长（秒），你可以用 ffprobe 动态获取
total_duration = 1200  # 假设视频总时长为 1200 秒


def parse_ffmpeg_progress(line):
    """解析 ffmpeg 输出中的进度信息，并转换为秒数"""
    match = re.search(r'time=(\d+:\d+:\d+\.\d+)', line)
    if match:
        # 将 "HH:MM:SS.ms" 格式转换为秒数
        time_str = match.group(1)
        hours, minutes, seconds = map(float, time_str.split(':'))
        return hours * 3600 + minutes * 60 + seconds
    return None


async def stream_reader(stream):
    """异步读取子进程输出并计算进度百分比"""
    while True:
        line = await stream.readline()
        if not line:
            break
        print(line)
        # 解析进度并计算百分比
        current_time = parse_ffmpeg_progress(line.decode())
        if current_time:
            percent = (current_time / total_duration) * 100
            print(f"Progress: {percent:.2f}%")


async def run_ffmpeg_command(source_video_path: Union[str, Path], out_video_path: Union[str, Path],
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
    cmd.append('-y')
    print(' '.join(cmd))
    # 启动子进程并捕获 stderr
    process = await asyncio.create_subprocess_exec(*cmd, stdout=asyncio.subprocess.PIPE,
                                                   stderr=asyncio.subprocess.PIPE)

    # 异步读取 stderr 并处理进度信息
    results = await asyncio.gather(
        stream_reader(process.stderr),
        process.wait()
    )
    print(results)

# 运行事件循环
# asyncio.run(run_ffmpeg_command())


if __name__ == '__main__':
    # get_video_info('/mnt/c/Users/sjdd/Downloads/Crab_Rave.mp4')
    res = test_popen()
    for i in res:
        if i.startswith('来自'):
            print(i)
