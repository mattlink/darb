import funcs as f

cur_pair = "BTC-USD"

class GDAX:

    def __init__(self):
        self.api_url = "http://api.gdax.com"
        self.name = "GDAX"
        self.info = self.ticker()

    def ticker(self):
        url = self.api_url + "/products/BTC-USD/ticker"
        data = f.http_get(url)

        price = data['price']
        time = data['time']

        return_data = {}
        return_data['name'] = self.name
        return_data['price'] = price
        return_data['currency'] = cur_pair
        return_data['time'] = time

        return return_data

    def verbose(self):
        f.verbose(self.info)


class KRAKEN:

    def __init__(self):
        self.api_url = "http://api.kraken.com"
        self.name = "Kraken"
        self.info = self.ticker()

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

        return_data = {}
        return_data['name'] = self.name
        return_data['price'] = price
        return_data['currency'] = cur_pair
        return_data['time'] = time

        return return_data

    def verbose(self):
        f.verbose(self.info)

class POLONIEX:

    def __init__(self):
        self.api_url = "http://poloniex.com/public?command="
        self.name = "Poloniex"
        self.info = self.ticker()

    def ticker(self):
        url = self.api_url + "returnTicker"
        data = f.http_get(url)

        price = data['USDT_BTC']['last']
        time = "time"

        return_data = {}
        return_data['name'] = self.name
        return_data['price'] = price
        return_data['currency'] = cur_pair
        return_data['time'] = time

        return return_data

    def verbose(self):
        f.verbose(self.info)


if __name__ == "__main__":
	print "the exchanges lib"
