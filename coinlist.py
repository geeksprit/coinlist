from pycoingecko import CoinGeckoAPI
from datetime import date
import csv
import time

def date_formt(timestamp):
  temp_date = date.fromtimestamp(timestamp)
  return temp_date.isoformat()
#output: '2020-12-31'


cg = CoinGeckoAPI()
original_list = cg.get_coins_list()
print("get list!")
# original_list = [{'id': '01coin', 'symbol': 'zoc', 'name': '01coin'}, {'id': '0-5x-long-algorand-token', 'symbol': 'algohalf', 'name': '0.5X Long Algorand Token'}, {'id': '0-5x-long-altcoin-index-token', 'symbol': 'althalf', 'name': '0.5X Long Altcoin Index Token'}, {'id': '0-5x-long-balancer-token', 'symbol': 'balhalf', 'name': '0.5X Long Balancer Token'}, {'id': '0-5x-long-bilibra-token', 'symbol': 'trybhalf', 'name': '0.5X Long BiLira Token'}, {'id': '0-5x-long-bitcoin-cash-token', 'symbol': 'bchhalf', 'name': '0.5X Long Bitcoin Cash Token'}, {'id': '0-5x-long-bitcoin-sv-token', 'symbol': 'bsvhalf', 'name': '0.5X Long Bitcoin SV Token'}, {'id': '0-5x-long-bitcoin-token', 'symbol': 'half', 'name': '0.5X Long Bitcoin Token'}, {'id': '0-5x-long-bitmax-token-token', 'symbol': 'btmxhalf', 'name': '0.5X Long BitMax Token Token'}, {'id': '0-5x-long-bnb-token', 'symbol': 'bnbhalf', 'name': '0.5X Long BNB Token'}, {'id': '0-5x-long-cardano-token', 'symbol': 'adahalf', 'name': '0.5X Long Cardano Token'}, {'id': '0-5x-long-chainlink-token', 'symbol': 'linkhalf', 'name': '0.5X Long Chainlink Token'}, {'id': '0-5x-long-compound-usdt-token', 'symbol': 'cusdthalf', 'name': '0.5X Long Compound USDT Token'}, {'id': '0-5x-long-cosmos-token', 'symbol': 'atomhalf', 'name': '0.5X Long Cosmos Token'}, {'id': '0-5x-long-defi-index-token', 'symbol': 'defihalf', 'name': '0.5X Long DeFi Index Token'}, {'id': '0-5x-long-dogecoin-token', 'symbol': 'dogehalf', 'name': '0.5X Long Dogecoin Token'}, {'id': '0-5x-long-dragon-index-token', 'symbol': 'drgnhalf', 'name': '0.5X Long Dragon Index Token'}, {'id': '0-5x-long-echange-token-index-token', 'symbol': 'exchhalf', 'name': '0.5X Long Exchange Token Index Token'}]

# cg.get_coins_list obja = {'id': '0-5x-long-echange-token-index-token', 'symbol': 'exchhalf', 'name': '0.5X Long Exchange Token Index Token'}
# 'id'  'symbol'  'name'

# cg.get_price objb={'usd': 6002.72, 'usd_market_cap': 0.0, 'usd_24h_vol': 10.204623057395912, 'usd_24h_change': None, 'last_updated_at': 1604622777}
# 'usd', 'usd_market_cap', 'usd_24h_vol', 'usd_24h_change', 'last_updated_at'


temp_list = []

for i in range(len(original_list)):
  temp_id = original_list[i]['id']
  temp_get_price = cg.get_price(ids=temp_id, vs_currencies='usd', include_market_cap='true', include_24hr_vol='true', include_24hr_change='true', include_last_updated_at='true')
  temp_data = {**original_list[i], **temp_get_price[temp_id]}
  temp_list.append(temp_data)
  print(str(i) + "  is got!")
  time.sleep(1)


sorted_list = sorted(temp_list, key = lambda x: x['usd_market_cap'],reverse=True)

#add rank, 清理数据
for i in range(len(sorted_list)):
  sorted_list[i]['coinGecko_link'] = 'https://www.coingecko.com/en/coins/' + sorted_list[i]['id']
  sorted_list[i]['rank'] = i + 1
  if sorted_list[i]['usd'] != None:
    sorted_list[i]['usd'] = int(sorted_list[i]['usd'])
  if sorted_list[i]['usd_market_cap'] != None:
    sorted_list[i]['usd_market_cap'] = int(sorted_list[i]['usd_market_cap'])
  if sorted_list[i]['usd_24h_vol'] != None:
    sorted_list[i]['usd_24h_vol'] = int(sorted_list[i]['usd_24h_vol'])
  if sorted_list[i]['usd_24h_change'] != None:
    sorted_list[i]['usd_24h_change'] = int(sorted_list[i]['usd_24h_change'])
  if sorted_list[i]['last_updated_at'] != None:
    sorted_list[i]['last_updated_at'] = date_formt(sorted_list[i]['last_updated_at'])



print("Start Writer file! ")
for i in range(6):
  filename = 'part' + str(i + 1) 
  print(filename)

  csv_name = filename + '.csv'
  with open(csv_name, 'w', newline='') as filename:
      spamwriter = csv.writer(filename, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
      spamwriter.writerow(['id', 'symbol', 'name', 'usd', 'usd_market_cap', 'usd_24h_vol', 'usd_24h_change', 'last_updated_at', 'rank', 'coinGecko_link'])
      for j in range(1016):
        #1016 total
        n = i + (j * 6)
        print(i, j, n)
        spamwriter.writerow([sorted_list[n]['id'], sorted_list[n]['symbol'], sorted_list[n]['name'], sorted_list[n]['usd'], sorted_list[n]['usd_market_cap'], sorted_list[n]['usd_24h_vol'], sorted_list[n]['usd_24h_change'], sorted_list[n]['last_updated_at'], sorted_list[n]['rank'], sorted_list[n]['coinGecko_link']])
  print("end for 6!!!!!")


print("end all!!!!!")



# for i in range(6):
#   filename = 'part' + str(i + 1)  
#   print(filename)
#   for j in range(3):
#     n = i + (j * 6)
#     print(i, j, n)



# def writercsv(filename):
#   csv_name = filename + '.csv'
#   with open(csv_name, 'w', newline='') as filename:
#       spamwriter = csv.writer(filename, delimiter=',',
#                               quotechar=',', quoting=csv.QUOTE_MINIMAL)
#       spamwriter.writerow(['id', 'symbol', 'name', 'usd', 'usd_market_cap', 'usd_24h_vol', 'usd_24h_change', 'last_updated_at', 'rank'])
#       spamwriter.writerow([n1, n2, n3])













# for i in range(6):
#   temp_id = original_list[i]['id']
#   temp_data = cg.get_price(ids=temp_id, vs_currencies='usd', include_market_cap='true', include_24hr_vol='true', include_24hr_change='true', include_last_updated_at='true')
#   temp_list.append(temp_data[temp_id])

# for i in range(1016):
#   for j in range(6):
#     n = i*6 + j + 1
#     temid = olist[n]['id']
#     xx = cg.get_price(ids=temid, vs_currencies='usd', include_market_cap='true', include_24hr_vol='true', include_24hr_change='true', include_last_updated_at='true')
#     print(xx)
#     print(temid)
