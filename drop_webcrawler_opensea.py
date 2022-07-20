from ssl import VerifyMode
import urllib.request
from bs4 import BeautifulSoup
import ssl
import requests
import json
import random
#from dingtalkchatbot.chatbot import DingtalkChatbot
import time
from datetime import datetime
ssl._create_default_https_context = ssl._create_unverified_context
# with urllib.request.urlopen('http://python.org/') as response:
#    html = response.read()
#    print(html)

# exit()

class DingTalkRobot():
    
    def __init__(self, webhook = 'https://oapi.dingtalk.com/robot/send?access_token='):

        #self.robot = DingtalkChatbot(webhook)
        self.exception_list = []

    def send_msg(self, msg, is_at_all=False):
        if is_at_all:
            self.robot.send_text(msg=f'{msg}', is_at_all=True)
        else:
            self.robot.send_text(msg=f'{msg}')


url = 'https://opensea.io/collection/ninja-squad-official?search[sortAscending]=true&search[sortBy]=PRICE&search[toggles][0]=BUY_NOW'
cloth_url = 'https://opensea.io/collection/ninja-squad-official?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Clothing&search[stringTraits][0][values][0]=Dragonborn&search[stringTraits][0][values][1]=Werewulf&search[stringTraits][0][values][2]=Commander&search[stringTraits][0][values][3]=Ninja-Chain%20Hoodie&search[stringTraits][0][values][4]=Admiral&search[stringTraits][0][values][5]=Blue%20Moroi&search[stringTraits][0][values][6]=Pumpkin&search[stringTraits][0][values][7]=Yakuza&search[stringTraits][0][values][8]=I%27m%20fine&search[stringTraits][0][values][9]=Ninjas%20Creed&search[stringTraits][0][values][10]=Ninja%20Squad%20Armor&search[stringTraits][0][values][11]=Mummy&search[stringTraits][0][values][12]=Tuxedo&search[stringTraits][0][values][13]=Sir&search[stringTraits][0][values][14]=Lieutenant&search[stringTraits][0][values][15]=Jack-o%27-lantern&search[stringTraits][0][values][16]=Dagger&search[stringTraits][0][values][17]=Scarfed&search[stringTraits][0][values][18]=Oni&search[stringTraits][0][values][19]=Wings&search[stringTraits][0][values][20]=Skeleton&search[stringTraits][0][values][21]=Rainbow%20Warrior&search[stringTraits][0][values][22]=Arrow%20Eater&search[toggles][0]=BUY_NOW'
face_url = 'https://opensea.io/collection/ninja-squad-official?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Face&search[stringTraits][0][values][0]=Lady%20Ninja&search[stringTraits][0][values][1]=Mummy&search[stringTraits][0][values][2]=AlienMan&search[stringTraits][0][values][3]=Vampire&search[stringTraits][0][values][4]=Scarface&search[stringTraits][0][values][5]=Punk&search[stringTraits][0][values][6]=Laser%20Eyes&search[stringTraits][0][values][7]=Ape&search[stringTraits][0][values][8]=Red%20Mask&search[stringTraits][0][values][9]=High%20Ninja&search[stringTraits][0][values][10]=Mask&search[stringTraits][0][values][11]=Beast&search[stringTraits][0][values][12]=Blue%20Mask&search[stringTraits][0][values][13]=Panda%20Ninja&search[stringTraits][0][values][14]=Fox%20Mask&search[stringTraits][0][values][15]=Robo%20Ninja&search[stringTraits][0][values][16]=Mechanical%20Mask&search[stringTraits][0][values][17]=WAGMI&search[stringTraits][0][values][18]=Tiger%20Ninja&search[stringTraits][0][values][19]=Goblin%20Ninja&search[stringTraits][0][values][20]=Fireman&search[toggles][0]=BUY_NOW'
hat_url = 'https://opensea.io/collection/ninja-squad-official?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Hat&search[stringTraits][0][values][0]=Watermelon&search[stringTraits][0][values][1]=Toadz&search[stringTraits][0][values][2]=Baby%20Kongz&search[stringTraits][0][values][3]=SucukluYumurta&search[stringTraits][0][values][4]=Ninja%20Squad%20Headband&search[stringTraits][0][values][5]=Medusa&search[stringTraits][0][values][6]=Yellow%20Hat&search[stringTraits][0][values][7]=Ninja%20Headband&search[stringTraits][0][values][8]=Dagger%20Head&search[stringTraits][0][values][9]=Beanie&search[stringTraits][0][values][10]=Magnifying%20Glasses&search[stringTraits][0][values][11]=Baby&search[stringTraits][0][values][12]=Nice%20Hat&search[stringTraits][0][values][13]=Bulky%20Head&search[stringTraits][0][values][14]=Angel%20Halo&search[stringTraits][0][values][15]=Meow&search[stringTraits][0][values][16]=Chick&search[toggles][0]=BUY_NOW'
ninja_url = 'https://opensea.io/collection/ninja-squad-official?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Ninja&search[stringTraits][0][values][0]=Eddyz&search[stringTraits][0][values][1]=BeGe&search[stringTraits][0][values][2]=CMYLMZ&search[stringTraits][0][values][3]=CryptoKemal&search[stringTraits][0][values][4]=Dundar&search[stringTraits][0][values][5]=Erhan%C3%9Cnal&search[stringTraits][0][values][6]=Kortan&search[stringTraits][0][values][7]=Myoo&search[stringTraits][0][values][8]=Paradotor&search[stringTraits][0][values][9]=Umut&search[stringTraits][0][values][10]=islor&search[toggles][0]=BUY_NOW'
honor_url = 'https://opensea.io/collection/ninja-squad-official?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Type&search[stringTraits][0][values][0]=Honorary&search[toggles][0]=BUY_NOW'
weapon_url = 'https://opensea.io/collection/ninja-squad-official?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Weapon&search[stringTraits][0][values][0]=Vitalik%27s%20Scepter&search[stringTraits][0][values][1]=KGB&search[stringTraits][0][values][2]=Wings&search[stringTraits][0][values][3]=Water%20Jetpack&search[stringTraits][0][values][4]=Jet%20Pack&search[toggles][0]=BUY_NOW'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

ddt = DingTalkRobot()

while 1:
    try:        
        req = urllib.request.Request(url=cloth_url, headers=headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode('utf-8')

        soup = BeautifulSoup(html, "html.parser")

        rst = soup.find_all('div', class_='Overflowreact__OverflowContainer-sc-10mm0lu-0 gjwKJf')
        rst_tag = rst[2]
        for px in rst_tag:
            if float(px) < 0.13:
                print('~~~~~~~~~~~~~~~~YES !!! BUY !!!~~~~~~~~~~~~~~')
                #ddt.send_msg(msg = 'monitor: Oh shit! shiboshi is here! HURRY UP!!!!!!', is_at_all = True)
                #exit()
            else:
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                #dt = datetime().now().strftime("%Y-%m-%d %H:%M")
                print(px)
                #ddt.send_msg(msg = f'{dt_string} - monitor: shiboshi is on the way......', is_at_all = False)
            time.sleep(random.randint(30,60))
    except Exception as e:
        print(e)
        #ddt.send_msg(msg=f'monitor:{e}',is_at_all=True)
        time.sleep(random.randint(120,240))
