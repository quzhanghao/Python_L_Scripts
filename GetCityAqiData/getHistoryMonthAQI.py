import requests
import execjs
import json


def createParams(city, month, ctx):
    '''由城市名、年月得出经js加密后的post参数,ctx由js代码解析得到'''
    method = 'GETDAYDATA'
    js = 'getEncryptedData("{0}", "{1}", "{2}")'.format(method, city, month)
    params = ctx.eval(js)
    return {'hd': params}


def getResponseData(city, month, ctx):
    '''由城市名、年月向服务器发送post请求并解密返回数据,ctx由js代码解析得到'''
    apiUrl = 'https://www.aqistudy.cn/historydata/api/historyapi.php'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
    }

    response = requests.post(apiUrl, data=createParams(city, month, ctx), headers=headers, timeout=10)
    if response.status_code != 200:
        return None
    # 解析数据
    js = 'decodeData("{0}")'.format(response.text)
    decrypted_data = ctx.eval(js)
    data = json.loads(decrypted_data)
    return data['result']['data']['items']


if __name__ == '__main__':
    # js环境，这里用nodeJS
    node = execjs.get()
    # compile javascript
    ctx = node.compile(open('encryption.js', encoding='utf-8').read())

    city = input('请输入城市名(如: 西安)：')
    year = input('请输入年份(如: 2018)：')
    month = input('请输入月份(如: 5)：').zfill(2)
    items = getResponseData(city, year + month, ctx)

    if items is not None:
        print('\n')
        print('日期\tAQI\tPM2.5\tPM10\tSO2\tNO2\tCO\tO3\t质量等级')
        for item in items:
            print(item['time_point'], end='\t')
            print(item['aqi'], end='\t')
            print(item['pm2_5'], end='\t')
            print(item['pm10'], end='\t')
            print(item['so2'], end='\t')
            print(item['no2'], end='\t')
            print(item['co'], end='\t')
            print(item['o3'], end='\t')
            print(item['quality'])
    else:
        print('数据获取失败!')
