
import requests
import json
from datetime import datetime as dt


base_url = 'https://fapi.binance.com'
end_point = '/futures/data/openInterestHist'


symbol = 'DOGEUSDT'
interval = '1h'

response = requests.get(base_url + end_point , params= {'symbol': symbol , 'period': interval , 'limit': 500} )

data = response.json()

open_interest = []
timelist = []

for i in range(len(data)):
 open_interest.append(float(data[i]['sumOpenInterestValue']))
 time = dt.fromtimestamp(data[i]['timestamp']/1000)
 formatted_time = time.strftime('%Y-%m-%d %H:%M:%S')
 timelist.append(formatted_time)
 
print(len(open_interest))
print(len(timelist))

def get_open_interest():
 return open_interest

def get_timelist():
 return timelist