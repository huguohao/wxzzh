#-*-coding:utf-8-*-
#filename:handle.py
import hashlib
import web
import reply
import receive
import config
class Handle(object):
    def POST(self):
        try:
            webData = web.data()
            print "Handle Post webdata is "
            print webData   #后台打日志
            recMsg = receive.parse_xml(webData)
            toUser = recMsg.FromUserName
            fromUser = recMsg.ToUserName
            if recMsg.MsgType == 'text':
                content = recMsg.Content
                if content == u"天气":
                    replyMsg = "多云"
                else:
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            if recMsg.MsgType == 'image':
                mediaId = recMsg.MediaId
                replyMsg = reply.ImageMsg(toUser,fromUser,mediaId)
                return replyMsg.send()
            else:
                return reply.Msg.send()
        except Exception, Argment:
            return Argment

    def Meun(self):
        return config.CreateMeun()

