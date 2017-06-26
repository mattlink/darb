import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import funcs as f

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
        ticker_data['currency'] = "BTC-USD"
        ticker_data['time'] = time

        if self.verbose == True:
            f.verbose_ticker(ticker_data)

        return ticker_data

if __name__ == "__main__":
    poloniex = POLONIEX()
    poloniex.verbose = True
    poloniex.ticker()
