from dingtalkchatbot.chatbot import DingtalkChatbot

from django.conf import settings
from settings import base

def send(message,at_mobiles=[]):
    #引用settings里面配置的钉钉群消息通知的Webhook地址：
    # webhook = 'https://oapi.dingtalk.com/robot/send?access_token=47306afa3a6574c1c0d4a3a8b33b717c93290ea27d2881c7fcc019df08e681b5'
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=a557b417e2ba7eb81982451aa14010b42ad7102ef45b0ff5cf864a801d18a119'
    #初始化机器人小丁，方式一：通常初始化
    xiaoming = DingtalkChatbot(webhook)
    #text消息@所有人
    xiaoming.send_text(msg=("面试hello通知：%s"%message), at_mobiles = at_mobiles)







