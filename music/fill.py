import re
import time
import sys
import pygame
from mutagen.mp3 import MP3
import math

lists = []
with open('a.lrc', 'r') as f:
    lines = f.readlines()
    for line in lines:
        temp_line = re.split(r'[]:[]', line)
        time_sum = float(temp_line[1]) * 60 + float(temp_line[2])
        lists.append([time_sum, temp_line[3].strip('\n')])  # 必须去掉换行符，然不然就尴尬了

pygame.mixer.init()
audio = MP3('a.mp3')
pygame.mixer.music.load('a.mp3')

# for x in audio.info.length:

class ProgressBar:
    def __init__(self, count = 0, total = 0, width = 50):  # 暂留，期望能实现进度条
        self.count = count
        self.total = total
        self.width = width

    def log(self, now):
        progress = self.width * self.count / self.total
        if(abs(pygame.mixer.music.get_pos()/1000 - lists[now][0]) <= 0.05):
            sys.stdout.write(' ' * 100 + '\r')
            sys.stdout.write(lists[now][1] + '\r')
            sys.stdout.flush()
            now += 1
        # sys.stdout.write(' ' * (100-len(lists[now-1][1])) + '*' * int(progress) + '-' * (self.width - int(progress) - 1) + '\r')  # 这个-1有毒
        # 弱鸡，并没有实现歌词和进度条同时存在
        if progress == self.width:
            sys.stdout.write('\n')
        sys.stdout.flush()
        self.count += 0.1
        return now

bar = ProgressBar(total=audio.info.length)
now = 0
# print(audio.info.length)
pygame.mixer.music.play(0)              # 只播放一次
for x in range(int(10 * audio.info.length)):
    now = bar.log(now)
    time.sleep(0.1)
    # print(pygame.mixer.music.get_pos())  # 返回以毫秒为单位


# a = "03"            # 我是傻逼了吗。。。。。绝望
# print(int(a))
# print(float(a))