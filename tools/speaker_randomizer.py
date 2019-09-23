#!/usr/bin/env python3

import random


speakers = ['程庆林', '李宇龙', '孙斌', '张凯', '张晓阳', '周奇', '周亚']

def test():
    pass


def generator():
    random.shuffle(speakers)
    random.shuffle(speakers)

    return

if __name__ == "__main__":
    generator()
    print(speakers)
