from operator import contains, sub
from ssl import VerifyMode
from typing import Mapping
import urllib.request
from bs4 import BeautifulSoup
import ssl
import requests
import json
import random
import time
from datetime import datetime
import pandas as pd
ssl._create_default_https_context = ssl._create_unverified_context
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

# init class
coins = {'eth':float, 'bnb':float, 'dot':float, 
        'leash':float, 'gods':float, 'crv':float,
        'near':float, 'kar':float}
locked = {'icp':float, 'ksm':float, 'geist':float, 'sdn':float, 'kar':float}
nft = {'jf':int, 'ninja':int, 'cryptoadz':int, 'doge':int, 'lions':int, 
    'head':int, 'boonji':int, 'doodles':int, 'wolf':int, 'sheep':int}
cash = {'hkd':int, 'cny':int, 'usd':int}
liabities = {'mortgage':int}

cgid_dict = {'eth':'ethereum', 'bnb':'binancecoin', 'dot':'polkadot', 
        'leash':'leash', 'gods':'gods-unchained', 'crv':'curve-dao-token',
        'near':'near', 'kar':'karura'}
coin_price_dict = {}
nft_price_dict = {}

# ninja squad 
ninja_base_url = 'https://opensea.io/collection/ninja-squad-official?search[sortAscending]=true&search[sortBy]=PRICE&search[toggles][0]=BUY_NOW'
# Wolf Game
wolfgame_wolf_url = 'https://opensea.io/collection/wolf-game?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Type&search[stringTraits][0][values][0]=Wolf&search[toggles][0]=BUY_NOW'
wolfgame_sheep_url = 'https://opensea.io/collection/wolf-game?search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=Type&search[stringTraits][0][values][0]=Sheep&search[toggles][0]=BUY_NOW'
# Jungle Freaks
jf_base_url = 'https://opensea.io/collection/jungle-freaks-by-trosley?search[sortAscending]=true&search[sortBy]=PRICE&search[toggles][0]=BUY_NOW'
# Doodles
doodles_base_url = 'https://opensea.io/collection/doodles-official?search[sortAscending]=true&search[sortBy]=PRICE&search[toggles][0]=BUY_NOW'
# CrypToadz
cryptoadz_base_url = 'https://opensea.io/collection/cryptoadz-by-gremplin?search[sortAscending]=true&search[sortBy]=PRICE&search[toggles][0]=BUY_NOW'
# LazyLions
lazylions_base_url = 'https://opensea.io/collection/lazy-lions?search[sortAscending]=true&search[sortBy]=PRICE&search[toggles][0]=BUY_NOW'
# DogePound
dogepound_base_url = 'https://opensea.io/collection/the-doge-pound?search[sortAscending]=true&search[sortBy]=PRICE&search[toggles][0]=BUY_NOW'
# Boonji
boonji_base_url = 'https://opensea.io/collection/boonjiproject?search[sortAscending]=true&search[sortBy]=PRICE&search[toggles][0]=BUY_NOW'
# HeadDao
head_base_url = 'https://opensea.io/collection/headdao?search[sortAscending]=true&search[sortBy]=PRICE&search[toggles][0]=BUY_NOW'

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
        return price

def coin_price_dict():
    import sys
    sys.path.append('../Independent/')
    from pycoingecko import CoinGeckoAPI
    cg = CoinGeckoAPI()
    for c,d in cgid_dict.items():
        coin_price_dict[c] = cg.get_price(d,'usd')[d]['usd']
        time.sleep(1)
    return coin_price_dict

def nft_price_dict():
    ninja_floor = get_floor(ninja_base_url)
    time.sleep(3)
    wolf_floor = get_floor(wolfgame_wolf_url)
    time.sleep(3)
    sheep_floor = get_floor(wolfgame_sheep_url)
    time.sleep(3)
    jf_floor = get_floor(jf_base_url)
    time.sleep(3)
    doodles_floor = get_floor(doodles_base_url)
    time.sleep(3)
    ct_floor = get_floor(cryptoadz_base_url)
    time.sleep(3)
    lions_floor = get_floor(lazylions_base_url)
    time.sleep(3)
    doge_floor = get_floor(dogepound_base_url)
    time.sleep(3)
    boonji_floor = get_floor(boonji_base_url)
    time.sleep(3)
    head_floor = get_floor(head_base_url)

    nft_price_dict['jf'] = jf_floor
    nft_price_dict['ninja'] = ninja_floor
    nft_price_dict['cryptoadz'] = ct_floor
    nft_price_dict['doge'] = doge_floor
    nft_price_dict['lions'] = lions_floor
    nft_price_dict['head'] = head_floor
    nft_price_dict['boonji'] = boonji_floor
    nft_price_dict['doodles'] = doodles_floor
    nft_price_dict['wolf'] = wolf_floor
    nft_price_dict['sheep'] = sheep_floor
    return nft_price_dict

if __name__ == '__main__':

    # position setup
    coins['eth'] = 3.14
    coins['bnb'] = 0.2
    coins['dot'] = 652
    coins['leash'] = 12.2
    coins['gods'] = 1077
    coins['crv'] = 1030
    coins['near'] = 339
    coins['kar'] = 104

    locked['icp'] = 170
    locked['ksm'] = 30
    locked['geist'] = 4460
    locked['sdn'] = 1029

    nft['jf'] = 8
    nft['ninja'] = 45
    nft['ct'] = 1
    nft['doge'] = 1
    nft['lions'] = 1
    nft['head'] = 2
    nft['boonji'] = 1
    nft['doodles'] = 1
    nft['wolf'] = 1
    nft['sheep'] = 1
    
    coin_px = coin_price_dict()
    nft_px = nft_price_dict()

    print(coin_px)
    print(nft_px)



