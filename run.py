# -*- coding: UTF-8 -*-
import json
import itchat, time
from itchat.content import *



# 加载配置信息
def load_config():
    f = open("config.json", encoding='utf-8')
    return json.load(f)


class WxMessage:
    name = ''
    type = ''
    msg = ''

    def __init__(self, name, type, msg):
        self.name = name
        self.type = type
        self.msg = msg

# 获取配置信息
config = load_config()
keys = config['keys']



mg = WxMessage('', '', '')


# 注册普通消息
@itchat.msg_register(TEXT)
def friend_msg(msg):
    mg.name = msg.user.nickName
    mg.type = "朋友"
    mg.msg = msg.text
    print_msg(mg)


# 注册群聊消息
@itchat.msg_register(TEXT, isGroupChat=True)
def group_msg(msg):
    mg.name = msg.actualNickName
    mg.type = msg.user.nickName
    mg.msg = msg.text
    print_msg(mg)


# 打印到的消息
def print_msg(mg):

    message_info = "发送类型：" + mg.type + "\n" + "发送人：" + mg.name + "\n" + "内容：" + mg.msg + "\n"

    for item in keys:
        if item in mg.msg:
            itchat.send(message_info, toUserName='filehelper')
            break

# 登陆微信
itchat.auto_login(True)
# 运行
itchat.run(True)
