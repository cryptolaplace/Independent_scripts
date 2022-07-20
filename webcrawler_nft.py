from operator import sub
from ssl import VerifyMode
from typing import Mapping
import urllib.request
from bs4 import BeautifulSoup
import ssl
import requests
import json
import sys
import random
import time
from datetime import datetime
ssl._create_default_https_context = ssl._create_unverified_context
#from dingtalkchatbot.chatbot import DingtalkChatbot
sys.path.append('../Independent/')
from pycoingecko import CoinGeckoAPI


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

# Visula Lands
sandbox_land_url = 'https://opensea.io/collection/sandbox?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Type&search[stringTraits][0][values][0]=Land&search[toggles][0]=BUY_NOW'
dcl_land_url = 'https://opensea.io/collection/decentraland?search[sortAscending]=true&search[sortBy]=PRICE&search[toggles][0]=BUY_NOW'
nftworld_land_url = 'https://opensea.io/collection/nft-worlds?search[sortAscending]=true&search[sortBy]=PRICE&search[toggles][0]=BUY_NOW'
webbland_url = 'https://opensea.io/collection/worldwidewebbland?search[sortAscending]=true&search[sortBy]=PRICE&search[toggles][0]=BUY_NOW'
somnium_space_url = 'https://opensea.io/collection/somnium-space?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Type&search[stringTraits][0][values][0]=Land&search[toggles][0]=BUY_NOW'
cryptovoxels_url = 'https://opensea.io/collection/cryptovoxels?search[sortAscending]=true&search[sortBy]=PRICE&search[toggles][0]=BUY_NOW'

# Games
# Wolf Game: mint 0.069420 + gas
wolfgame_alphawolf_url = 'https://opensea.io/collection/wolf-game-migrated?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Alpha%20Score&search[stringTraits][0][values][0]=8&search[toggles][0]=BUY_NOW'
wolfgame_betawolf_url = 'https://opensea.io/collection/wolf-game-migrated?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Alpha%20Score&search[stringTraits][0][values][0]=7&search[toggles][0]=BUY_NOW'
wolfgame_deltawolf_url = 'https://opensea.io/collection/wolf-game-migrated?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Alpha%20Score&search[stringTraits][0][values][0]=6&search[toggles][0]=BUY_NOW'
wolfgame_omegawolf_url = 'https://opensea.io/collection/wolf-game-migrated?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Alpha%20Score&search[stringTraits][0][values][0]=5&search[toggles][0]=BUY_NOW'
wolfgame_gen0sheep_url = 'https://opensea.io/collection/wolf-game-migrated?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Generation&search[stringTraits][0][values][0]=Gen%200&search[stringTraits][1][name]=Type&search[stringTraits][1][values][0]=Sheep&search[toggles][0]=BUY_NOW'
wolfgame_gen1sheep_url = 'https://opensea.io/collection/wolf-game-migrated?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Type&search[stringTraits][0][values][0]=Sheep&search[stringTraits][1][name]=Generation&search[stringTraits][1][values][0]=Gen%201&search[toggles][0]=BUY_NOW'
wolfgame_land_url = 'https://opensea.io/collection/wolf-game-land?search[sortAscending]=true&search[sortBy]=PRICE&search[toggles][0]=BUY_NOW'
wolfgame_farmer_url = 'https://opensea.io/collection/wolf-game-farmer?search[sortAscending]=true&search[sortBy]=PRICE&search[toggles][0]=BUY_NOW'
wolfgame_pouch_url = 'https://opensea.io/collection/wool-pouch?search[sortAscending]=true&search[sortBy]=PRICE&search[toggles][0]=BUY_NOW'
vox_base_url = 'https://opensea.io/collection/collectvox'
clonex_base_url = 'https://opensea.io/collection/clonex'
clonex_mintvial_base_url = 'https://opensea.io/collection/clonex-mintvial'

# PFP
# Doodles: mint 0.123 + gas 
doodles_base_url = 'https://opensea.io/collection/doodles-official?search[sortAscending]=true&search[sortBy]=PRICE&search[toggles][0]=BUY_NOW'
bayc_base_url = 'https://opensea.io/collection/boredapeyachtclub'

# Art
fidenza_base_url = 'https://opensea.io/collection/fidenza-by-tyler-hobbs'


class DingTalkRobot():
    
    def __init__(self, webhook = 'https://oapi.dingtalk.com/robot/send?access_token=6179b9945debb5b952569b7ebdbec9fd2dfdb5d2ab3a738b4edcfe309d6ac2ee'):

        #self.robot = DingtalkChatbot(webhook)
        self.exception_list = []

    def send_msg(self, msg, is_at_all=False):
        if is_at_all:
            self.robot.send_text(msg=f'{msg}', is_at_all=True)
        else:
            self.robot.send_text(msg=f'{msg}')

#ddt = DingTalkRobot()

def parser_site(url):
    req = urllib.request.Request(url=url, headers=headers)
    res = urllib.request.urlopen(req)
    html = res.read().decode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    return soup

def get_floor(url):
    soup = parser_site(url)
    floor_rst = soup.find_all('div', class_='Overflowreact__OverflowContainer-sc-10mm0lu-0 gjwKJf')
    floor_tag = floor_rst[2]
    for price in floor_tag:
        return float(price)

def get_min_price(url):
    soup = parser_site(url)
    minpx_rst = soup.find_all('div', class_='Overflowreact__OverflowContainer-sc-7qr9y8-0 jPSCbX Price--amount')
    if minpx_rst:
        px_tag = minpx_rst[0]
        for px in px_tag:
            px = float(px.replace(',',''))
            return float(px)
    else:
        return None

def run():

    sleep_time = random.randint(10,20)
    print('\n')
    print('----------',datetime.now().strftime("%d/%m/%Y %H:%M:%S"),'----------')
    print('\n')
    print('WolfGame sheep: ', get_min_price(wolfgame_sheep_url))
    time.sleep(sleep_time)


if __name__ == '__main__':
    
    sleep_time = 1
    cg = CoinGeckoAPI()
    # wool_eth = cg.get_coin_by_id('wolf-game-wool')['market_data']['current_price']['eth']
    # wool_usd = cg.get_coin_by_id('wolf-game-wool')['market_data']['current_price']['usd']
    eth_price = cg.get_coin_by_id('ethereum')['market_data']['current_price']['usd']
    # sand_price = cg.get_coin_by_id('the-sandbox')['market_data']['current_price']['usd']
    # gala_price = cg.get_coin_by_id('gala')['market_data']['current_price']['usd']
    # axs_price = cg.get_coin_by_id('axie-infinity')['market_data']['current_price']['usd']
    # mana_price = cg.get_coin_by_id('decentraland')['market_data']['current_price']['usd']
    # gala_node_price = 0
    # wolfgame_gen0sheep_floor = get_min_price(wolfgame_gen0sheep_url)
    # wolfgame_gen1sheep_floor = get_min_price(wolfgame_gen1sheep_url)
    # time.sleep(sleep_time)
    # wolfgame_alphawolf_floor = get_min_price(wolfgame_alphawolf_url)
    # wolfgame_betawolf_floor = get_min_price(wolfgame_betawolf_url)
    # wolfgame_deltawolf_floor = get_min_price(wolfgame_deltawolf_url)
    # wolfgame_omegawolf_floor = get_min_price(wolfgame_omegawolf_url)
    # time.sleep(sleep_time)
    # wolfgame_land_floor = get_floor(wolfgame_land_url)
    # wolfgame_farmer_floor = get_floor(wolfgame_farmer_url)
    # wolfgame_pouch_floor = get_floor(wolfgame_pouch_url)
    # time.sleep(sleep_time)



    print('\n')
    print('----------',datetime.now().strftime("%d/%m/%Y %H:%M:%S"),'----------')
    print('\n')

    sandbox_land_floor = get_min_price(sandbox_land_url)
    print(f'Sandbox land: {sandbox_land_floor} eth, {int(sandbox_land_floor*eth_price)} usd')
    time.sleep(sleep_time)
    dcl_land_floor = get_min_price(dcl_land_url)
    print(f'Decentraland land: {dcl_land_floor} eth, {int(dcl_land_floor*eth_price)} usd')
    time.sleep(sleep_time)
    somnium_space_land_floor = get_min_price(somnium_space_url)
    print(f'Somnium space land: {somnium_space_land_floor} eth, {int(somnium_space_land_floor*eth_price)} usd')
    time.sleep(sleep_time)
    cryptovoxels_land_floor = get_min_price(cryptovoxels_url)
    print(f'Cryptovoxels land: {cryptovoxels_land_floor} eth, {int(cryptovoxels_land_floor*eth_price)} usd')
    time.sleep(sleep_time)
    nftworld_land_floor = get_min_price(nftworld_land_url)
    print(f'NFT World land: {nftworld_land_floor} eth, {int(nftworld_land_floor*eth_price)} usd')
    time.sleep(sleep_time)
    worldwide_webb_land_floor = get_min_price(webbland_url)
    print(f'Worldwide Webb Land: {worldwide_webb_land_floor} eth, {int(worldwide_webb_land_floor*eth_price)} usd')    
    time.sleep(sleep_time)
    print('\n')
    # print(f'WolfGame $WOOL: {wool_eth} eth, {wool_usd} usd')
    # print(f'WolfGame alphawolf: {wolfgame_alphawolf_floor} eth, {int(wolfgame_alphawolf_floor*eth_price)} usd')
    # print(f'WolfGame betawolf: {wolfgame_betawolf_floor} eth, {int(wolfgame_betawolf_floor*eth_price)} usd')
    # print(f'WolfGame deltawolf: {wolfgame_deltawolf_floor} eth, {int(wolfgame_deltawolf_floor*eth_price)} usd')
    # print(f'WolfGame omegawolf: {wolfgame_omegawolf_floor} eth, {int(wolfgame_omegawolf_floor*eth_price)} usd')
    # print(f'WolfGame gen 0 sheep: {wolfgame_gen0sheep_floor} eth, {int(wolfgame_gen0sheep_floor*eth_price)} usd')
    # print(f'WolfGame gen 1 sheep: {wolfgame_gen1sheep_floor} eth, {int(wolfgame_gen1sheep_floor*eth_price)} usd')
    # print(f'WolfGame land: {wolfgame_land_floor} eth, {int(wolfgame_land_floor*eth_price)} usd')
    # print(f'WolfGame farmer: {wolfgame_farmer_floor} eth, {int(wolfgame_farmer_floor*eth_price)} usd')
    # print(f'WolfGame pouches: {wolfgame_pouch_floor} eth, {int(wolfgame_pouch_floor*eth_price)} usd')

    # print('\n')
    # print(f'BAYC Floor: {bayc_floor} eth, {int(bayc_floor*eth_price)} usd')
    # print(f'Fidenza Floor: {fidenza_floor} eth, {int(fidenza_floor*eth_price)} usd')
    # print(f'Doodles Floor: {doodles_floor} eth, {int(doodles_floor*eth_price)} usd')
    
    # print('\n')

    while 1:
        try:
            #run()
            break
        except Exception as e:
            print(e)
            #ddt.send_msg(msg=f'monitor:{e}',is_at_all=False)
            time.sleep(random.randint(60,120))
    