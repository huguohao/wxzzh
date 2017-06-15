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
			print "Handle post webdata is",webData #后台日志
			recMsg = receive.parse_xml()
			if isinstance(recMsg,receive.Msg) and recMsg.MsgType == 'text':
				toUser = recMsg.FromUserName
				fromUser = recMsg.ToUserName
				content = "hello"
				replyMsg = reply.TextMsg(toUser,fromUser,content)
				return replyMsg.send()
			else:
				print "不处理"
				return "success"
		except Exception,Argment:
			return Argment