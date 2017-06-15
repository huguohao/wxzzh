#-*-coding:utf-8-*-
#filename:handle.py
import hashlib
import web
import reply
import receive
class Handle(object):
    def POST(self):
        try:
            webData = web.data()
            print "Handle Post webdata is "
            print webData   #后台打日志
            recMsg = receive.parse_xml(webData)
            if recMsg.MsgType == 'text':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                content = recMsg.Content
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            if recMsg.MsgType == 'image':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                replyMsg = reply.ImageMsg(toUser,fromUser,mediaId)
            else:
                print "暂且不处理"
                return "success"
        except Exception, Argment:
            return Argment