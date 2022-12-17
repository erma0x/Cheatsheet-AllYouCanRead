import requests
import datetime
import time

print('Get Real Time Data from Iexapis sandbox')
while True:
	IEX_CLOUD_API_TOKEN = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaa'

	symbols =['AAPL','TSLA','MSFT']
	for symbol in symbols:
		api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token={IEX_CLOUD_API_TOKEN}'
		data = requests.get(api_url).json()
		print(symbol,' price is ',data['iexRealtimePrice'])
	
	print('-'*80)
	time.sleep(2)
