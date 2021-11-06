import sys
sys.path.append('../Independent/')
from pycoingecko import CoinGeckoAPI
import time

cg = CoinGeckoAPI()

coin_detail = cg.get_coins_markets(vs_currency='usd',order='market_cap_desc',per_page=200,page=2)

def get_id_by_mc():
    global id_lst
    id_lst = []
    for coin in coin_detail:
        id_lst.append(coin['id'])
    return id_lst

def gen_twitter_dict():
    tw_dict = {}
    for id in id_lst:
        item = cg.get_coin_by_id(id)
        if 'community_data' in item:
            if 'twitter_followers' in item['community_data'].keys():
                tw_count = item['community_data']['twitter_followers']
                tw_dict[id] = tw_count
                print(tw_dict)
                time.sleep(1)
    return tw_dict

id_lst = ['oxygen', 'superfarm', 'tokemak', 'starlink', 'ampleforth', 'ergo', 'pundi-x-2', 'mask-network', 'energy-web-token', 'ocean-protocol', 'bakerytoken', 'medibloc', 'trust-wallet-token', 'feg-token', 'band-protocol', 'alchemix', 'seth', 'asd', 'keep-network', 'zenon', 'dodo', 'conflux-token', 'mango-markets', 'verge', 'cartesi', 'status', 'chia', 'bitcoin-diamond', 'playdapp', 'origin-protocol', 'pirate-chain', 'orbs', 'iexec-rlc', 'ardor', 'vulcan-forged', 'sapphire', 'tokamak-network', 'alien-worlds', 'vectorspace', 'joe', 'civic', 'mobox', 'pax-gold', 'ark', 'dvision-network', 'star-atlas', 'plex', 'akash-network', 'unibright', 'nkn', 'storm', 'dopex', 'prometeus', 'electroneum', 'pundi-x', 'badger-dao', 'venus', 'mirror-protocol', 'orchid-protocol', 'hive', 'sbtc', 'proton', 'casper-network', 'singularitynet', 'oasis-network', 'beta-finance', 'wilder-world', 'stratis', 'balancer', 'taboo-token', 'allianceblock', 'alchemy-pay', 'ultra', 'mars-ecosystem-token', 'eden', 'merit-circle', 'ton-crystal', 'auction', 'ellipsis', 'numeraire', 'aelf', 'bitkub-coin', 'husd', 'btc-standard-hashrate-token', 'clover-finance', 'marketpeak', 'lido-staked-sol', 'orion-protocol', 'my-neighbor-alice', 'syscoin', 'alchemix-usd', 'dawn-protocol', 'truefi', 'superrare', 'bifrost', 'gmx', 'kardiachain', 'e-radix', 'telos', 'steem', 'maidsafecoin', 'wrapped-centrifuge', 'polkastarter', 'storj', 'somnium-space-cubes', 'klever', 'tomochain', 'radicle', 'thorchain-erc20', 'noia-network', 'eth-2x-flexible-leverage-index', 'metal', 'catecoin', 'dero', 'render-token', 'ankreth', 'adventure-gold', 'lido-dao', 'lcx', 'escoin-token', 'funfair', 'rif-token', 'hoge-finance', 'anyswap', 'defipulse-index', 'defi-kingdoms', 'metadium', 'compound-uniswap', 'richquack', 'axia-coin', 'quark-chain', 'flex-coin', 'smooth-love-potion', 'uquid-coin', 'thorstarter', 'handshake', 'automata', 'melon', 'everipedia', 'polkaswap', 'kyber-network-crystal', 'beldex', 'utrust', 'seedify-fund', 'aragon', 'arpa-chain', 'crypto20', 'star-atlas-dao', 'sun-token', 'shiden', 'wanchain', 'gods-unchained', 'sentinel', 'api3', 'safepal', 'linear', 'platon-network', 'mx-token', 'altura', 'rook', 'hathor', 'bscpad', 'kyber-network', 'request-network', 'power-ledger', 'stp-network', 'orca', 'compound-0x', 'kin', 'ethlend', 'augur', 'zelcash', 'decentral-games', 'propy', 'redfox-labs-2', 'strike', 'shabu-shabu', 'liquity', 'spookyswap', 'tether-gold', 'concierge-io', 'hxro', 'aurory', 'boson-protocol', 'yfii-finance', 'lgcy-network', 'ethernity-chain', 'math', 'tokocrypto', 'divi', 'derivadao', 'quick', 'aavegotchi', 'gemini-dollar', 'wrapped-nxm', 'morpheus-network', 'usdx', 'unizen', 'cratos', 'covalent']
rst = gen_twitter_dict()
print(rst)
