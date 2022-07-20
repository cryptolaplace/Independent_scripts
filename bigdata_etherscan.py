import sys
sys.path.append('/Users/justinfu/github/pyetherscan')
from etherscan.contracts import Contract
from etherscan.transactions import Transactions
import json


# with open('../../api_key.json', mode='r') as key_file:
#     key = json.loads(key_file.read())['key']


key = 'N3GBM9X61Y4296BBFRC1XTIKWMHSSYGFTE'
doodles = '0x8a90cab2b38dba80c64b7734e58ee1db38b8992e'


# api = Contract(address=doodles, api_key=key)
api = Transactions(api_key=key)
hash = '0x0be436318d8a916ab8d2e067c28580e8cf0d4441a38e18d41935e72c44d28305'

receipt_status = api.get_tx_receipt_status(tx_hash=hash)
print(receipt_status)

