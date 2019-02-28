# -*- coding: utf-8 -*-

__author__ = 'vanxkr.com'

import struct


def byte2float(x):
    return struct.unpack('<f', struct.pack('4b', *x))[0]


def float2byte(f):
    return [hex(i) for i in struct.pack('f', f)]


if __name__ == '__main__':
    print(byte2float([0x00, 0x00, 0x48, 0x42]))
# 50.0

    print(float2byte(50))
# [0x00, 0x00, 0x48, 0x42]
