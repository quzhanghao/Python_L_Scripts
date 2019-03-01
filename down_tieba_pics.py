#!/usr/bin/env python3
import re
import urllib.request


class DownTiebaImg:

    def __init__(self, url):
        self.url = url

    def getImgLinks(self):
        response = urllib.request.urlopen(self.url)
        pattern = re.compile(r'<img class="BDE_Image" src="(.+?)" size=', re.S)
        imgLinks = re.findall(pattern, response.read().decode('utf-8'))
        return imgLinks

    def saveImgs(self, path='./', pn=''):
        imgLinks = self.getImgLinks()
        if not path.endswith('/'):
            path += '/'
        name = 0
        for link in imgLinks:
            print(link)
            urllib.request.urlretrieve(link, path + str(pn) + '_%s.jpg' % name)
            name += 1
        print('completed')


def main(path='./'):
    url = input('输入贴子网址：')
    Img = DownTiebaImg(url)
    pn = input('输入想保存的贴子页数，留空为url所在的当前页，输入 x 为贴子前x页:\n')
    if not pn:
        Img.saveImgs(path)
    else:
        _url = url.split('?pn=')
        Img.url = _url[0]
        Img.saveImgs(path, 1)
        for i in range(2, int(pn) + 1):
            _url = url.split('=')
            Img.url = _url[0] + '=' + str(i)
            Img.saveImgs(path, i)


if __name__ == '__main__':
    main()
