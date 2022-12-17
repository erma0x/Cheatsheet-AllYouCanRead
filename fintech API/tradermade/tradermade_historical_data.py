#https://tradermade.com/tutorials/python-sdk-for-forex-data/
#pip install tradermade

import tradermade as tm

# set api key
tm.set_rest_api_key("api_key")
tm.live(currency='EURUSD,GBPUSD',fields=["bid", "mid", "ask"]) # returns live data - fields is optional


tm.currency_list() 
# gets list of all currency codes available add two codes to get code for currencypair ex EUR + USD gets EURUSD

tm.historical(currency='EURUSD,GBPUSD', date="2011-01-20",interval="daily", fields=["open", "high", "low","close"]) 
# returns historical data for the currency requested interval is daily, hourly, minute - fields is optional

# get timeseries data
import pandas as pd

df = pd.DataFrame()
for i in range(2011, 2021):  
    x = tm.timeseries(currency='EURUSD', start=str(i)+"-06-17",fields=["open", "high", "low","close"], end=str(i+1)+"-06-16")
    df = df.append(x)

df = df.drop_duplicates()

# returns timeseries data for the currency requested interval is daily, hourly, minute - fields parameter is optional (you can select ["close"] if you just want close prices)
tm.timeseries(currency='EURUSD', start="2021-04-20",end="2021-04-22",interval="hourly",fields=["open", "high", "low","close"]) 
 
# tm.timeseries(currency='EURUSD,GBPUSD', start="2021-04-26",end="2021-04-27",interval="minute",fields=["close"], period=15)
# returns 15 min bar for two currencies - you may need to adjust date to two days back or function will return an error that only two days of data is allowed for minute interval.

 

