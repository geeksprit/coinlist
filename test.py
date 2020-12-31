



import csv

n1 = 'aaa'
n2 = 'bbb'
n3 = 'ccc'
n4 = 'ddd'

with open('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar=',', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Name', 'Lovelypam', 'Wonderful Spam'])
    spamwriter.writerow([n1, n2, n3])


xx = cg.get_price(ids='bitcoin', vs_currencies='usd', include_market_cap='true', include_24hr_vol='true', include_24hr_change='true', include_last_updated_at='true')

# for i in range(2):
#   for j in range(6):
#     n = i*6 + j + 1
#     tname = clist[n]['id']
#     xx = cg.get_price(ids=tname, vs_currencies='usd', include_market_cap='true', include_24hr_vol='true', include_24hr_change='true', include_last_updated_at='true')
#     print(xx)
#     print(tname)

from datetime import date
>>> t= date.fromtimestamp(1609406150)
>>> t
datetime.date(2020, 12, 31)
>>> t.isoformat()
'2020-12-31'