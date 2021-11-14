from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time, os
import pandas as pd
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_argument("--disable-blink-features=AutomationControlled")
bafn = r'D:\data\app\dd\biance_spread.csv'
hbfn = r'D:\data\app\dd\biance_spread.csv'

def initBa():
    b = webdriver.Chrome(chrome_options = options)
    b.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
                    Object.defineProperty(navigator, 'webdriver', {
                      get: () => undefined
                    })
                  """})
    b.maximize_window()
    b.implicitly_wait(10)
    return b

def loginBa(user = 'chenzhuhai8@gmail.com', pss = 'Czh123456'):
    loginUrl = 'https://accounts.binance.com/zh-CN/login?return_to=aHR0cHM6Ly93d3cuYmluYW5jZS5jb20vemgtQ04vY29udmVydA=='
    b.get(loginUrl)
    time.sleep(1)
    b.find_element_by_name('email').send_keys(user)
    b.find_element_by_name('password').send_keys(pss)
    b.find_element_by_id('click_login_submit').click()
    
def inputCodeBa(code):
    for i in range(5):
        try:       
            ActionChains(b).send_keys_to_element(b.find_element_by_class_name('css-rivkf9'), code).perform()
            time.sleep(1)
            b.find_element_by_class_name('css-jl5e70').send_keys(Keys.ENTER)
            time.sleep(1)
            break
        except Exception as e:
            b.find_element_by_class_name('css-ye7z7w').click()   

def getResult(dcoin, scoin):
    b.find_element_by_class_name('css-1pgyemp').click()
    time.sleep(1)
    price = b.find_element_by_class_name('css-bm3e06').text.replace('\n', ':')
    reversePrice = b.find_element_by_class_name('css-a0qjr0').text.replace('\n', ':')
    obtain = b.find_element_by_class_name('css-195wmkv').text.replace('\n', ':')
    if dcoin in price and scoin in price:
        #print(scoin, svol, price, reversePrice, obtain)
        dvol = float(obtain.split(':')[1].split(' ')[0])
        px = float(price.split(' ')[-2])
        return px
    return -1
    
def convertBa(row):
    '''卖掉 scoin, 得到 dcoin'''
    dvol = -1
    try:
        dcoin, scoin, svol = row['dcoin'], row['scoin'], row['svol']
        #b.get('https://www.binance.com/zh-CN/convert')
        inputCodeBa(dcoin)
        
        b.find_element_by_class_name('css-ew2l8i').click()
        time.sleep(1)
        inputCodeBa(scoin)
        ActionChains(b).send_keys_to_element(b.find_element_by_class_name('css-16fg16t'), svol).perform()
        time.sleep(1)        
        spx = getResult(dcoin, scoin)
        if spx != -1:
            b.find_element_by_class_name('css-ew2l8i').click()
            ActionChains(b).send_keys_to_element(b.find_element_by_class_name('css-16fg16t'), svol).perform()
            ActionChains(b).send_keys_to_element(b.find_element_by_class_name('css-1ot5fm0'), svol).perform()
            bpx = getResult(dcoin, scoin)
            if bpx != -1:
                bpx = 1 / bpx
                spread = abs(bpx - spx) * 2 / (bpx + spx)*100
                dvol = spread
                if not os.path.exists(bafn):
                    with open(bafn, 'w') as f:
                        f.write(f"dcoin,scoin,svol,dvol,spx,bpx,spread\n")
                with open(bafn, 'a') as f:
                    f.write(f"{dcoin},{scoin},{svol},{dvol},{spx},{bpx},{spread}%\n")
                return f"{round(bpx, 4)} {round(spx, 4)} {round(spread, 3)}%"
    except Exception as e:
        #print(scoin, e)
        pass
    if dvol == -1:
        print(dcoin, scoin)
    return ''

def initHb():
    b = webdriver.Chrome(chrome_options = options)
    b.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
                    Object.defineProperty(navigator, 'webdriver', {
                      get: () => undefined
                    })
                  """})
    b.maximize_window()
    b.implicitly_wait(10)
    return b

def loginHb(url):
    b.get(url)
    time.sleep(1)
    
def inputCodeHb(code, bb):
    try:   
        bb.find_element_by_class_name('trade-select-text').click()
        ActionChains(b).send_keys_to_element(bb.find_element_by_class_name('trade-select-search'), code).perform()
        time.sleep(1)
        bb.find_element_by_class_name('item-text').click()
        time.sleep(1)
        return True
    except Exception as e:
        b.find_element_by_class_name('flex-auto').click()
    return False

def coin2coin(dcoin, scoin, svol):
    '''卖掉 scoin, 得到 dcoin'''
    loginHb('https://c2c.huobi.com/zh-cn/one-trade/convert')
    dvol = ''
    try:
        if not inputCodeHb(scoin, b.find_element_by_class_name('trade-input-control.init')):
            return dvol
        bb = b.find_elements_by_xpath('//div[@class = "trade-input-control init"]')[0]
        if not inputCodeHb(dcoin, bb):
            return dvol
        ActionChains(b).send_keys_to_element(b.find_element_by_class_name('font-bold-en'), svol).perform()
        time.sleep(2)      
        spx = bb.find_element_by_class_name('font-bold-en').get_attribute('value')
        if spx != '':
            if not inputCodeHb(scoin, bb):
                return dvol
            if not inputCodeHb(dcoin, b.find_element_by_class_name('trade-input-control.init')):
                return dvol
            ip = bb.find_element_by_class_name('font-bold-en')
            ip.clear()
            ActionChains(b).send_keys_to_element(ip, svol).perform()
            time.sleep(2)      
            bpx = b.find_element_by_class_name('font-bold-en').get_attribute('value')
            if bpx != '':
                bpx, spx = float(bpx), float(spx)
                spread = abs(bpx - spx) * 2 / (bpx + spx)*100
                if spread > 10:
                    print('err:', dcoin, scoin, spread)
                    return dvol
                if not os.path.exists(hbfn):
                    with open(hbfn, 'w') as f:
                        f.write(f"dcoin,scoin,svol,spx,bpx,spread\n")
                with open(hbfn, 'a') as f:
                    f.write(f"{dcoin},{scoin},{svol},{spx},{bpx},{spread}%\n")
                return f"{round(bpx/svol, 4)} {round(spx/svol, 4)} {round(spread, 3)}%"
    except Exception as e:
        pass
    return dvol

def selectBest():
    payments = b.find_elements_by_xpath('//div[@class = "pay-method-item old"]')
    isSelect = False
    for e in payments:
        if '余额' in e.text:
            e.click()
            isSelect = True
            time.sleep(1)
            break
    if not isSelect:
        for e in payments:
            if len(e.find_elements_by_class_name('best')) != 0:
                e.click()
                time.sleep(1)
                break
            
def getSellPx(scoin, dcoin, svol):
    loginHb('https://c2c.huobi.com/zh-cn/one-trade/sell')
    if not inputCodeHb(scoin, b.find_element_by_class_name('trade-input-control')):
        return ''
    bb = b.find_elements_by_xpath('//div[@class = "trade-input-control"]')[1]
    if not inputCodeHb(dcoin, bb):
        return ''
    selectBest()
    ActionChains(b).send_keys_to_element(b.find_element_by_class_name('font-bold-en'), svol).perform()
    time.sleep(3)      
    spx = bb.find_element_by_class_name('font-bold-en').get_attribute('value')
    return spx

def getBuyPx(scoin, dcoin, svol):
    loginHb('https://c2c.huobi.com/zh-cn/one-trade/buy')
    bb = b.find_elements_by_xpath('//div[@class = "trade-input-control"]')[1]
    if not inputCodeHb(scoin, bb):
        return ''    
    if not inputCodeHb(dcoin, b.find_element_by_class_name('trade-input-control')):
        return ''
    selectBest()
    ActionChains(b).send_keys_to_element(bb.find_element_by_class_name('font-bold-en'), svol).perform()
    time.sleep(5)      
    bpx = b.find_element_by_class_name('font-bold-en').get_attribute('value')
    return bpx
    
def coin2currency(dcoin, scoin, svol):
    '''卖掉 scoin, 得到 dcoin'''
    dvol = ''
    try:
        spx = getSellPx(scoin, dcoin, svol)
        if spx != '':
            bpx = getBuyPx(scoin, dcoin, svol)
            if bpx != '':
                bpx, spx = float(bpx), float(spx)
                spread = abs(bpx - spx) * 2 / (bpx + spx)*100
                if spread > 10:
                    print('err:', dcoin, scoin, spread)
                    return dvol
                if not os.path.exists(hbfn):
                    with open(hbfn, 'w') as f:
                        f.write(f"dcoin,scoin,svol,spx,bpx,spread\n")
                with open(hbfn, 'a') as f:
                    f.write(f"{dcoin},{scoin},{svol},{spx},{bpx},{spread}%\n")
                return f"{round(bpx/svol, 4)} {round(spx/svol, 4)} {round(spread, 3)}%"
    except Exception as e:
        pass
    return dvol

def convertHb(row):
    dcoin, scoin, svol = row['dcoin'], row['scoin'], row['svol']
    curreny = ['EUR', 'GBP', 'BRL', 'UAH', 'KZT', 'RUB']
    if dcoin == 'USDT' or scoin == 'USDT':
        if scoin in curreny or dcoin in curreny:
            return coin2currency(dcoin, scoin, svol)
        return coin2coin(dcoin, scoin, svol)
    else:
        return coin2currency(dcoin, scoin, svol)

def fetchHb(df):
    for ii in range(2):
        for i, r in df.iterrows():
            if df.loc[i, 'Huobi用户端'] == '':
                print(i)
                df.loc[i, 'Huobi用户端'] = convertHb(r)
    return df

def fetchBa(df):
    for ii in range(2):
        for i, r in df.iterrows():
            if df.loc[i, 'Binance用户端'] == '':
                df.loc[i, 'Binance用户端'] = convertBa(r)
    return df

df = pd.read_csv(r'D:\data\app\dd\OTC Spread Report.csv')
df.index = df.Symbol
df = df[['svol']]
df['s'] = df.index
df['scoin'] = df.s.apply(lambda s : ('USDT' if s.startswith('USDT') else s[:3]) if 'USDT' in s else s[:3])
df['dcoin'] = df.s.apply(lambda s : (s[-3:] if s.startswith('USDT') else 'USDT') if 'USDT' in s else s[-3:])
del df['s']
df['Huobi用户端'] = ''
df['Binance用户端'] = ''

b = initBa()
loginBa()
df = fetchBa(df)
b.quit()

b = initHb()
df = fetchHb(df)
b.quit()