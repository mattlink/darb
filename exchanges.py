import funcs as f

fiat_cur = "USD"
trade_cur = "BTC"

cur_pair = trade_cur + "-" + fiat_cur

class GDAX:

    def __init__(self):
        self.api_url = "http://api.gdax.com"
        self.name = "GDAX"
        self.verbose = False

    def ticker(self):
        url = self.api_url + "/products/BTC-USD/ticker"
        data = f.http_get(url)

        price = data['price']
        time = data['time']

        ticker_data = {}
        ticker_data['name'] = self.name
        ticker_data['price'] = price
        ticker_data['currency'] = cur_pair
        ticker_data['time'] = time

        if self.verbose == True:
            f.verbose_ticker(ticker_data)

        return ticker_data

class KRAKEN:

    def __init__(self):
        self.api_url = "http://api.kraken.com"
        self.name = "Kraken"
        self.verbose = False

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
        ticker_data['currency'] = cur_pair
        ticker_data['time'] = time

        if self.verbose == True:
            f.verbose_ticker(ticker_data)

        return ticker_data

class POLONIEX:

    def __init__(self):
        self.api_url = "http://poloniex.com/public?command="
        self.name = "Poloniex"
        self.verbose = False

    def ticker(self):
        url = self.api_url + "returnTicker"
        data = f.http_get(url)

        price = data['USDT_BTC']['last']
        time = "time"

        ticker_data = {}
        ticker_data['name'] = self.name
        ticker_data['price'] = price
        ticker_data['currency'] = cur_pair
        ticker_data['time'] = time

        if self.verbose == True:
            f.verbose_ticker(ticker_data)

        return ticker_data


if __name__ == "__main__":
	print "the exchanges lib"
