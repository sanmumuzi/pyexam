# -*- coding: utf-8 -*-
import sys


def ptail(parone=None, partwo=None, parthree=None):
    if partwo == '-N' or '-n' or None:
        with open(parone, 'rt') as f:
            data = f.readlines()
            if parthree:
                for x in data[0 - parthree:]:
                    print(x, end='')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('illegal!')
    elif len(sys.argv) == 2:
        ptail(parone=sys.argv[1], parthree=10)
    elif len(sys.argv) == 3:
        ptail(parone=sys.argv[1], partwo=sys.argv[2])
    elif len(sys.argv) == 4:
        if sys.argv[2] == '-N' or '-n':
            ptail(parone=sys.argv[1], parthree=int(sys.argv[3]))