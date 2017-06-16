# -*- coding: utf-8 -*-
# filename: meun.py
import urllib2
import json
from config import get_token_access

def CreateMeun():
    url =" https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" %get_token_access()
    data = {
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
    }

    req = urllib2.Request(url)
    req.add_header('Content-Type','application/json')
    req.add_header('encoding','utf-8')
    response = urllib2.urlopen(req,json.jumps(data,ensure_ascii=False))
    result = response.read()
    return result
