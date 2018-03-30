#/usr/bin/env python
#coding=utf8
 
import httplib
import md5
import urllib
import random
import json
import requests #使用 requests 代替alfred里的web
from workflow import Workflow, ICON_WEB, web

appKey = '343297326eeabbd8'
secretKey = 'wGL3AcgX2mx4v9us3226z3aWWtG8grVM'

def get_web_data(query):
    print 'querystr为：'+str(query)
    query = urllib.quote(str(query))
    salt = random.randint(1, 65536)
    sign = appKey+query+str(salt)+secretKey
    m1 = md5.new()
    m1.update(sign)
    sign = m1.hexdigest()
    url = 'https://openapi.youdao.com/api?q=' + query + \
        '&from=EN&to=zh_CHS&appKey='+appKey+'&salt='+str(salt)+'&sign='+sign
    print 'url地址为：'+url
    # resp = requests.get(url)
    # print '请求内容为：'+web.get(url).content
    # print(resp.text.encode(resp.encoding).decode('utf-8'))

    # resp = web.get(url)
    s = web.get(url).json()
    print s
    print json.dumps(s, ensure_ascii=False)

    
    return s

def get_phonetic_args(s):
    result = {}
    if u'basic' in s.keys():
        if s["basic"].get("us-phonetic"):
            result["us"] = "[" + s["basic"]["us-phonetic"] + "]"
        if s["basic"].get("uk-phonetic"):
            result["uk"] = "[" + s["basic"]["uk-phonetic"] + "]"
    return result

try:
    s = get_web_data('add')
    extra_args = {}
    extra_args.update(get_phonetic_args(s))

    if s.get("errorCode") == '0':
        print '正确'
    else:
        title = '有道也翻译不出来了'
        subtitle = '尝试一下去网站搜索'
        print title+subtitle

    print s.get("errorCode")

except Exception, e:
    print e