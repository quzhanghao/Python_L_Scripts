#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def rgb2hex(x, y, z):
    s = '#'
    s += hex(x // 16)
    s += hex(x % 16)
    s += hex(y // 16)
    s += hex(y % 16)
    s += hex(z // 16)
    s += hex(z % 16)
    print(s.replace('0x', ''))


def hex2rgb(s):
    xyz = [int(i, 16) for i in s.replace('#', '')]
    x = xyz[0] * 16 + xyz[1]
    y = xyz[2] * 16 + xyz[3]
    z = xyz[4] * 16 + xyz[5]
    print(x, y, z)


if __name__ == '__main__':
    rgb2hex(204, 0, 255)
    hex2rgb('#cc00ff')
