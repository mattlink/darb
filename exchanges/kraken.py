import configparser
config = configparser.ConfigParser()
config.read('keys.ini')

import krakenex

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import funcs as f

class KRAKEN:

    def __init__(self):
        self.api_url = "http://api.kraken.com"
        self.name = "Kraken"
        self.verbose = False

        self.API_KEY = config['kraken-read-only']['key']
        self.API_SECRET = config['kraken-read-only']['private-key']

        self.client = krakenex.API()
        self.client.key = self.API_KEY
        self.client.secret = self.API_SECRET

    def get_time(self):
        url = self.api_url + "/0/public/Time"
        data = f.http_get(url)

        ## can return unixtime with data['result']['unixtime']
        return data['result']['rfc1123']

    def ticker(self):
        url = self.api_url + "/0/public/Ticker?pair=XBTUSD"
        data = f.http_get(url)
        data = data['result']['XXBTZUSD']

        price = data['c'][0]
        time = self.get_time()

        ticker_data = {}
        ticker_data['name'] = self.name
        ticker_data['price'] = price
        ticker_data['currency'] = "BTC-USD"
        ticker_data['time'] = time

        if self.verbose == True:
            f.verbose_ticker(ticker_data)

        return ticker_data

    def balance(self):
        data = self.client.query_private('Balance')
        balance = data['result']['XXBT']
        print('KRAKEN BTC Balance: ' + balance)
        return balance


if __name__ == "__main__":
    kraken = KRAKEN()
    kraken.verbose = True
    kraken.ticker()
