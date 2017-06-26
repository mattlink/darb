import configparser
config = configparser.ConfigParser()
config.read('keys.ini')

import json, hmac, hashlib, time, requests, base64
from requests.auth import AuthBase

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import funcs as f

class CoinbaseExchangeAuth(AuthBase):
    def __init__(self, api_key, secret_key, passphrase):
        self.api_key = api_key
        self.secret_key = secret_key
        self.passphrase = passphrase

    def __call__(self, request):
        timestamp = str(time.time())
        message = timestamp + request.method + request.path_url + (request.body or '')
        hmac_key = base64.b64decode(self.secret_key)
        signature = hmac.new(hmac_key, message, hashlib.sha256)
        signature_b64 = signature.digest().encode('base64').rstrip('\n')

        request.headers.update({
            'CB-ACCESS-SIGN': signature_b64,
            'CB-ACCESS-TIMESTAMP': timestamp,
            'CB-ACCESS-KEY': self.api_key,
            'CB-ACCESS-PASSPHRASE': self.passphrase,
            'Content-Type': 'application/json'
        })

        return request

class GDAX:

    def __init__(self):
        self.api_url = "http://api.gdax.com"
        self.name = "GDAX"
        self.verbose = False

        self.API_KEY = config['gdax-full']['key']
        self.API_SECRET = config['gdax-full']['secret']
        self.API_PASS = config['gdax-full']['passphrase']

        self.auth = CoinbaseExchangeAuth(self.API_KEY, self.API_SECRET, self.API_PASS)

    def ticker(self):
        url = self.api_url + "/products/" + "BTC-USD" + "/ticker"
        data = f.http_get(url)

        price = data['price']
        time = data['time']

        ticker_data = {}
        ticker_data['name'] = self.name
        ticker_data['price'] = price
        ticker_data['currency'] = "BTC-USD"
        ticker_data['time'] = time

        if self.verbose == True:
            f.verbose_ticker(ticker_data)

        return ticker_data

    def balance(self):
        url = self.api_url + '/accounts'
        r = requests.get(url, auth=self.auth)
        data = r.json()
        balance = ''
        for wallet in data:
            if wallet['currency'] == 'BTC':
               balance = wallet['balance']

        #print json.dumps(data, indent=2, sort_keys=True)
        print 'GDAX BTC Balance: ' + balance
        return balance

    def send_all_coin_to_kraken(self):
        #will require having kraken bitcoin wallet
        kraken_wallet = '33CVPrJHG5qptKmEJwETrMfroJSrR3GMLo'

        amount = get_btc_amt()

        # POST
        url = self.api_url + 'withdrawals/crypto'
        request = {
            "amount": amount,
            "currency": "BTC",
            "crypto_address": kraken_wallet
        }
        r = requests.post(url, json=request, auth=self.auth)
        print json.dumps(r.json(), indent=2, sort_keys=True)


    def get_gdax_accounts(self):
        url = self.api_url + '/accounts'
        r = requests.get(url, auth=self.auth)
        data = r.json()

        for i in range(0, len(data)):
            print json.dumps(data[i], indent=2, sort_keys=True)

    def get_coinbase_accounts(self):
        url = self.api_url + '/coinbase-accounts'
        r = requests.get(url, auth=self.auth)
        data = r.json()

        print json.dumps(data, indent=2, sort_keys=True)



if __name__ == "__main__":
    gdax = GDAX()
    gdax.verbose = True
    gdax.ticker()
