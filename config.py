# -*- coding: utf-8 -*-
# filename: config.py
import urllib2
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')
AppId = 'wx4bb5ae285f532455'
AppSecret = '067f37361397bb8fa10010bb2acb4196'
url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" %(AppId,AppSecret)
result = urllib2.urlopen(url).read()
access_token = json.loads(result).get('access_token')
def CreateMeun():
    url =" https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" %access_token
    data = '''{
        "button": [
            {
                "name": "一键查询",
                "sub_button": [
                    {
                        "type": "click",
                        "name": "我的快递",
                        "key": "meitu"
                    },
                    {
                        "type": "view",
                        "name": "今天天气",
                        "url": "http://m.guju.com.cn/photos"
                    },
                    {
                        "type": "view",
                        "name": "四六级成绩",
                        "url": "http://m.qzone.com/infocenter?g_f=#2378686916/mine"
                    }]
            },
            {
                "name": "吃喝玩乐",
                "sub_button": [
                    {
                        "type": "click",
                        "name": "吃",
                        "key": "eat"
                    },
                    {
                        "type": "click",
                        "name": "喝",
                        "key": "drink"
                    },
                    {
                        "type": "click",
                        "name": "玩",
                        "key": "play"
                    },
                    {
                        "type": "view",
                        "name": "更多案例",
                        "url": "http://m.guju.com.cn/projects"
                    }]
            },
            {
                "type": "view",
                "name": "关于我们",
                "url": "http://guju.com.cn/zhuanti/freedesign.jsp?src=3"

            }

        ]
    }'''

    request = urllib2.urlopen(url, data.encode('utf-8'))
    return request.read()

CreateMeun()