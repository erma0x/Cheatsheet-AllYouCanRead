from coinbase.wallet.client import Client
from time import sleep
from data import api_key, api_secret

#https://developers.coinbase.com/docs/wallet/guides/buy-sell


client = Client(api_key, api_secret)

currency_code = 'USD'

start_price = client.get_spot_price(currency=currency_code)

while(True):

    buy_price = client.get_buy_price(currency=currency_code)
