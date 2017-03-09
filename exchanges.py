import requests
import pprint
pp = pprint.PrettyPrinter(indent=4)

class GDAX:

    def __init__(self):
        self.api_url = "http://api.gdax.com"

    def ticker(self):
        url = self.api_url + "/products/BTC-USD/ticker"
        r = requests.get(url)
        data = r.json()
        
        print "EXCHANGE: GDAX"
        print "PRODUCT: BTC-USD"
        print "PRICE: " + data['price']
        print "TIME: " + data['time'] 
         
        return data

class KRAKEN:
    
    def __init__(self):
        self.api_url = "http://api.kraken.com"
    
    def ticker(self):
        url = self.api_url + "/0/public/Ticker?pair=XBTUSD"
        r = requests.get(url)
        data = r.json() 

        pp.pprint(data)        

    def assets(self):
        url = self.api_url + "/0/public/AssetPairs"
        r = requests.get(url)
        data = r.json()
        
        # use pretty print on raw json values 
        pp.pprint(data['result'])

class POLONIEX: 
    
    def __init__(self):
        self.api_url = "http://poloniex.com/public?command="

    def ticker(self):
        url = self.api_url + "returnTicker"
        r = requests.get(url)
        data = r.json()

        # pp.pprint(data)
        print "EXCHANGE: POLONIEX"
        print "PRODUCT: BTC-USD"
        print "DATA: " 
        pp.pprint(data['USDT_BTC'])
        print "TIME: " + "insert time"

        return data
        

if __name__ == "__main__":
    print "the exchanges lib"
