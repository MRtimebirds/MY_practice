"""
通过查找，能找到js代码中的操作代码
1.这是计算salt的公式，在fanyi.min.js文件中找到的，
t = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10));
2.sign: n.md5("fanyideskweb" + e + t + "sr_3(QOHT)L2dx#uuGR@r")
md5一共需要四个参数，第一个和第四个都是固定的字符串，第三个是所谓的salt。第二个就是输入的要查找的单词
"""

import requests,re,hashlib,time,random
while True:
    e=input()

    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

    session=requests.session()
    session.get('http://fanyi.youdao.com/',headers=headers)
    cookies=session.cookies.get_dict()
    # print(cookies)
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
             'referer':'http://fanyi.youdao.com/'}
    r=str(int(time.time()*1000))
    i=r+str(random.randint(1,9))

    #下面用md5破解
    sign="fanyideskweb" + e + i + "n%A-rKaT5fb[Gy?;N5@Tj"
    # md5 = hashlib.md5()
    # # 需要一个bytes格式的参数
    # md5.update(sign.encode("utf-8"))
    # sign = md5.hexdigest()
    #上面4句可改为下面2句
    sign=sign.encode()  #encode方法返回编码后的字符串，它是一个 bytes 对象。
    sign=hashlib.md5(sign).hexdigest()


    data={'i': e,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client':'fanyideskweb',
    'salt': i,  #时间戳  ，该参数查找方法：打开f12，右上角三点位置点击，选择search，搜索salt，
    'sign': sign,
    'ts': r,
    'bv': '3a019e7d0dda4bcd253903675f2209a5',
    'doctype': 'json',
    'version': 2.1,
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME'}
    #我的URL：http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule
    # 需要修改成http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule
    # 就是把_o去掉，而且这样的请求只能是用于英文翻译汉文
    url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    res=requests.post(url,headers=headers,cookies=cookies,data=data)
    # print(res.text)

    translate=re.findall('"tgt":"(.*?)"',res.text,re.S)
    print(translate[0])

