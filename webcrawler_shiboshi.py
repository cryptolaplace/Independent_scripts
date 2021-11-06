from ssl import VerifyMode
import urllib.request
from bs4 import BeautifulSoup
import ssl
import requests
import json
import random
from dingtalkchatbot.chatbot import DingtalkChatbot
import time
from datetime import datetime
ssl._create_default_https_context = ssl._create_unverified_context
# with urllib.request.urlopen('http://python.org/') as response:
#    html = response.read()
#    print(html)

# exit()

class DingTalkRobot():
    
    def __init__(self, webhook = 'https://oapi.dingtalk.com/robot/send?access_token='):

        self.robot = DingtalkChatbot(webhook)
        self.exception_list = []

    def send_msg(self, msg, is_at_all=False):
        if is_at_all:
            self.robot.send_text(msg=f'{msg}', is_at_all=True)
        else:
            self.robot.send_text(msg=f'{msg}')


url = 'https://shiboshis.shibaswap.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

ddt = DingTalkRobot()

while 1:
    try:        
        req = urllib.request.Request(url=url, headers=headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode('utf-8')

        soup = BeautifulSoup(html, "html.parser")

        rst = soup.body.div.image.get('src')

        if rst != 'logo.png':
            print('shit, it has come!!!!!!!!!!!!')
            ddt.send_msg(msg = 'monitor: Oh shit! shiboshi is here! HURRY UP!!!!!!', is_at_all = True)
            exit()
        else:
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            #dt = datetime().now().strftime("%Y-%m-%d %H:%M")
            print(rst)
            ddt.send_msg(msg = f'{dt_string} - monitor: shiboshi is on the way......', is_at_all = False)
        time.sleep(random.randint(60,120))
    except Exception as e:
        print(e)
        ddt.send_msg(msg=f'monitor:{e}',is_at_all=True)
        time.sleep(random.randint(120,240))
