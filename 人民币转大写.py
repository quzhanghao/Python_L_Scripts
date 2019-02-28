#!/usr/bin/env python3
# -*- coding: utf-8 -*-

counts = ('', '', '拾', '佰', '仟')
units = ('', '元', '万', '亿', '兆')
elements = ('零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖')


class cnumber:

    def csplit(self, cdata):
        csdata = []
        g = len(cdata) % 4
        if g:
            csdata.append(cdata[:g])
        k = g
        lx = len(cdata) - 1
        while k <= lx:
            csdata.append(cdata[k:k + 4])
            k += 4
        return csdata

    def cschange(self, int_area):
        lk = lenki = len(int_area)
        i = 0
        single = ''
        for i in range(lenki):
            if int(int_area[i]) == 0:
                if i != lenki - 1:
                    if int(int_area[i + 1]) != 0:
                        single += elements[0]
            else:
                single += elements[int(int_area[i])] + counts[lk]
            lk -= 1
        return single

    def toupper(self, data):
        data = round(float(data) + 0.00000002, 2)
        cdata = str(data).split('.')

        int_area = cdata[0]
        dec_area = cdata[1]
        result = ''

        # 处理整数部分
        int_list = self.csplit(int_area)
        len_int_list = len(int_list)
        for i in range(len_int_list):
            single = self.cschange(int_list[i])
            if single != '':
                result += single + units[len_int_list - i]

        # 处理小数部分
        len_dec_area = len(dec_area)
        if len_dec_area == 1:
            if int(dec_area[0]) == 0:
                result += '整'
            else:
                result += elements[int(dec_area[0])] + '角整'
        else:
            if int(dec_area[0]) == 0 and int(dec_area[1]) != 0:
                result += '零' + elements[int(dec_area[1])] + '分'
            elif int(dec_area[0]) == 0 and int(dec_area[1]) == 0:
                result += '整'
            elif int(dec_area[0]) != 0 and int(dec_area[1]) != 0:
                result += elements[int(dec_area[0])] + '角' + elements[int(dec_area[1])] + '分'
            else:
                result += elements[int(dec_area[0])] + '角整'

        return result


if __name__ == '__main__':
    pt = cnumber()
    print(pt.toupper(3.1))
