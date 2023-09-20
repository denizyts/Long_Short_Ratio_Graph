
import requests
import json
from datetime import datetime as dt


base_url = 'https://fapi.binance.com'
end_point = '/futures/data/globalLongShortAccountRatio'


symbol = 'DOGEUSDT'
interval = '1h'

response = requests.get(base_url + end_point , params= {'symbol': symbol , 'period': interval , 'limit': 500} )

data = response.json()


ratio = []
timelist = []

for i in range(len(data)):
 ratio.append(float(data[i]['longShortRatio']))
 time = dt.fromtimestamp(data[i]['timestamp']/1000)
 formatted_time = time.strftime('%Y-%m-%d %H:%M:%S')
 timelist.append(formatted_time)
 


def get_ratio():
 return ratio

def get_timelist():
 return timelist