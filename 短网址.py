import requests

baseurl = 'http://api.t.sina.com.cn/short_url/shorten.json?source=3271760578&url_long='


def get_short_url(url, data=None):
    url = baseurl + url
    rep = requests.get(url, timeout=60)
    return rep.json()[0]['url_short']


if __name__ == '__main__':
    print(get_short_url('http://www.baidu.com'))
