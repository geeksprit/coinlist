import json
from pycoingecko import CoinGeckoAPI


cg = CoinGeckoAPI()
original_list = cg.get_coins_list()

print("get list!")
with open('coinlist.json', 'w') as f:
  json.dump(original_list,f)
