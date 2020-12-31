import csv
import json
import time
from pycoingecko import CoinGeckoAPI
from datetime import date

cg = CoinGeckoAPI()

def date_formt(timestamp):
  temp_date = date.fromtimestamp(timestamp)
  return temp_date.isoformat()
#output: '2020-12-31'

with open('coinlist.json', 'r') as jsonfile:
  original_list = json.load(jsonfile)

result = [] 
with open('error1.txt', 'r') as fa:
  for line in fa:
    t = line.strip('\n')
    result.append(int(t))

# for i in range(5000, 6096):
for i in result:
  #6096 500
  temp_id = original_list[i]['id']
  try:
    temp_get_price = cg.get_price(ids=temp_id, vs_currencies='usd', include_market_cap='true', include_24hr_vol='true', include_24hr_change='true', include_last_updated_at='true')
    print(str(i) + "  is got!")
    print(temp_get_price)

    temp_data = {**original_list[i], **temp_get_price[temp_id]}

  # 清理数据
    temp_data['coinGecko_link'] = 'https://www.coingecko.com/en/coins/' + temp_data['id']
    temp_data['rank'] = i + 1
    if temp_data['usd'] != None:
      temp_data['usd'] = int(temp_data['usd'])
    if temp_data['usd_market_cap'] != None:
      temp_data['usd_market_cap'] = int(temp_data['usd_market_cap'])
    if temp_data['usd_24h_vol'] != None:
      temp_data['usd_24h_vol'] = int(temp_data['usd_24h_vol'])
    if temp_data['usd_24h_change'] != None:
      temp_data['usd_24h_change'] = int(temp_data['usd_24h_change'])
    if temp_data['last_updated_at'] != None:
      temp_data['last_updated_at'] = date_formt(temp_data['last_updated_at'])

    with open('alllist_t.csv', 'a', newline='') as filename:
        spamwriter = csv.writer(filename, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([temp_data['id'], temp_data['symbol'], temp_data['name'], temp_data['usd'], temp_data['usd_market_cap'], temp_data['usd_24h_vol'], temp_data['usd_24h_change'], temp_data['last_updated_at'], temp_data['rank'], temp_data['coinGecko_link']])

    time.sleep(0.3)
    print(str(i) + "  is Writed!")
  except:
    with open('error3.txt', 'a', newline='') as ff:
      ff.write(str(i) +  "\n")
    print(str(i) + " has an exception occurred")


print("End!")


# with open('alllist.csv', 'a', newline='') as filename:
#     spamwriter = csv.writer(filename, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
#     spamwriter.writerow([temp_data[n]['id'], temp_data[n]['symbol'], temp_data[n]['name'], temp_data[n]['usd'], temp_data[n]['usd_market_cap'], temp_data[n]['usd_24h_vol'], temp_data[n]['usd_24h_change'], temp_data[n]['last_updated_at'], temp_data[n]['rank'], temp_data[n]['coinGecko_link']])

