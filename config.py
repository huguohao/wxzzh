# -*- coding: utf-8 -*-
# filename: config.py
import urllib2
import json

AppId = 'wx4bb5ae285f532455'
AppSecret = '067f37361397bb8fa10010bb2acb4196'
def get_token_access():
    url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" %(AppId,AppSecret)
    result = urllib2.urlopen(url).read()
    token = json.loads(result).get('access_token')
    #print "access_token == %s" %token
    return token



