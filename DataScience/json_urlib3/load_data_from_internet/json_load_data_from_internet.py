"""
This is python3 example for json object manipulation
"""
# JSON
# import JavaScript object notation manipulation library 
import json

print('_'*80)
# URLIB3
# load json data from internet with urlib library
import urllib3
print('urlib version ',urllib3.__version__)
http = urllib3.PoolManager()


# stocks data from alphavantage
my_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=10min&apikey=demo'

response = http.request('GET', my_url)

print('response status ',response.status)
print(response.data.decode('utf-8'))
