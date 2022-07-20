from datetime import datetime
from datetime import timedelta
import time
import sys
sys.path.append('../Independent/')
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()


# your param

# sys param
wool_eth = cg.get_coin_by_id('wolf-game-wool')['market_data']['current_price']['eth']
sheep_minted = 12066
sheep_staked = 11756
wolves_minted = 1743
wolves_staked = 1662
wool_claimed = 230_110_840

wolf_alpha = 14
wolf_beta = 308
wolf_delta = 529
wolf_omega = 891

game_start_date = datetime(2021,11,19,0,0)
game_pause_date = datetime(2021,11,22,14,0)
migration_date = datetime(2021,11,28,12,23)
# constants
wool_earn_day = 10000
wool_all_earn = 2_400_000_000

# read from pouch num
risky_sheep = 7760
unrisky_sheep = sheep_minted - risky_sheep
risky_pool = 1879510788 
pouch_price = 0.097


waiting_sheep = sheep_minted - unrisky_sheep - risky_sheep

risky_sheep_pct = round(100 * risky_sheep/sheep_minted,2)
unrisky_sheep_pct = round(100 * unrisky_sheep/sheep_minted,2)
waiting_sheep_pct = round(100 * waiting_sheep/sheep_minted,2)

# risky game logic
unclaimed_all_wool = wool_all_earn - wool_claimed

# def risky_game():
#     print(f'Now, risky sheep num: {risky_sheep} ({risky_sheep_pct}), unrisky sheep num: {unrisky_sheep} ({unrisky_sheep_pct}), waiting sheep: {waiting_sheep} ({waiting_sheep_pct})')
#     unrisky_sheep_earn_total = int((unrisky_sheep * 10000 * (migration_date - game_start_date).days))
#     unrisky_sheep_net_gain = int(unrisky_sheep_earn_total * 0.8)
#     unrisky_netgain_per = int(unrisky_sheep_net_gain / unrisky_sheep)

#     risky_sheep_earn_total



def risky_game():
    print(f'Now {unrisky_sheep_pct} pct sheep chose NO RISKY, {risky_sheep_pct} pct sheep chose RISKY, {waiting_sheep_pct} pct sheep is WAITING')
    print('\n')
    unrisky_sheep_earn = (unrisky_sheep * 10000 * (migration_date - game_start_date).days)
    unrisky_wool_sheep = int((unrisky_sheep_earn / unrisky_sheep) * 0.8)
    print(f'Each NO risky sheep will get {unrisky_wool_sheep} $ WOOL, i.e. {round(unrisky_wool_sheep * wool_eth,2)} $ETH')
    risky_wool_sheep = int(risky_pool / risky_sheep)
    assuming_risky_wool_sheep = int((unclaimed_all_wool - unrisky_sheep_earn)/(sheep_minted - unrisky_sheep))
    print(f'Each risky sheep have 50 pct possibility to get {risky_wool_sheep} $WOOL, i.e. {round(risky_wool_sheep * wool_eth,2)} $ETH')
    print(f'Assuming all left sheep choose risky, each risky sheep have 50 pct possibility to get {assuming_risky_wool_sheep} $WOOL, i.e. {round(assuming_risky_wool_sheep * wool_eth,2)} $ETH')
    for alpha_score in range(5,9):
        risky_wool_wolf = int(((unrisky_sheep_earn * 0.2) + ((unclaimed_all_wool - unrisky_sheep_earn) * 0.5)) * (1/(8*wolf_alpha+7*wolf_beta+6*wolf_delta+5*wolf_omega) * alpha_score))
        print(f'Each score {alpha_score} wolf will get {risky_wool_wolf} $WOOL, i.e. {round(risky_wool_wolf * wool_eth,2)} $ETH')

    # take
    print(f'If unrisky, 6 sheep could have {round(6 * 10000 * wool_eth,4)} $ETH, and daily release of {round((6 * unrisky_wool_sheep/1460) * wool_eth,4)} $ETH')
    print(f'If risky, 6 sheep could have {round(3 * 10000 * wool_eth,4)} $ETH, and daily release of {round((3 * risky_wool_sheep/1460) * wool_eth,4)} $ETH')
    print(f'If unrisky, can use the extra {round(3 * 10000 * wool_eth,4)} $ETH to buy {int(round(3 * 10000 * wool_eth,4)/pouch_price)} pouch, then daily release will be {round(((6 * unrisky_wool_sheep/1460)+(int(round(3 * 10000 * wool_eth,4)/pouch_price) * 37700/1460)) * wool_eth,4)} $ETH')

def pouch_fair():
    pass

# if linear release
daily_release = int((unclaimed_all_wool - 10000 * (unrisky_sheep + risky_sheep/2))/4/365)
daily_burn = 0

print('\n')
print('----------',datetime.now().strftime("%d/%m/%Y %H:%M:%S"),'----------')
print('\n')
print('$WOOL price: ', wool_eth, 'ETH')
print('\n')
print('Unclaimed total $WOOL: ', '{:.4e}'.format(unclaimed_all_wool))
print('Daily release: ', '{:.4e}'.format(daily_release), 'WOOL')
print('Daily burn: 0', 'WOOL')
print('Net burn: 0')


print('\n')
risky_game()
print('\n')

