import argparse
import sys
import time

APP_DESC="""
命令:ptail1
"""

print(APP_DESC)
if len(sys.argv) == 1:
    sys.argv.append('--help')
parser = argparse.ArgumentParser()
parser.add_argument('-f',action="store_true",help='实时更新')
parser.add_argument('-n','-N',type=int,default=10,help='输出最后几行')
parser.add_argument('file',)
args = parser.parse_args()

# print(args.file)
# print(args.n)
# print(args.f)

def ptail():
    if not args.f:
        with open(args.file, 'r', encoding='utf-8') as f:   # 坑：不能打开txt文件，编码问题
            data = f.readlines()
            for x in data[0 - args.n:]:
                print(x, end='')
    else:
        already_output = 0
        while True:
            already_output = show_last(already_output)       # 记录输出位置
            time.sleep(1)
            # print(already_output)

def show_last(already_output):
    with open(args.file, 'r', encoding='utf-8') as f:
        data = f.readlines()
        if len(data) > 10 and already_output == 0:
            already_output = len(data) - 10
        if already_output < len(data):
            for x in data[already_output - len(data):]:      # 输出这一秒内增加的文本
                print(x, end='')
            already_output = len(data)
    return already_output                   # 返回位置


if __name__ == "__main__":
    ptail()
