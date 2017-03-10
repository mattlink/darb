import requests
import pprint
pp = pprint.PrettyPrinter(indent=4)

import lib

cur_pair = "BTC-USD"

class GDAX:

	def __init__(self):
		self.api_url = "http://api.gdax.com"
		self.name = "GDAX"

	def ticker(self):
		url = self.api_url + "/products/BTC-USD/ticker"
		r = requests.get(url)
		data = r.json()
		
		price = data['price']	
		time = data['time']
	
		lib.pticker(self.name, price, cur_pair, time)
		
		return data

class KRAKEN:

	def __init__(self):
		self.api_url = "http://api.kraken.com"
		self.name = "Kraken"

	def get_time(self):
		url = self.api_url + "/0/public/Time"		
		r = requests.get(url)		
		data = r.json()
		
		#return data['result']['unixtime']		
		return data['result']['rfc1123']
 
	def ticker(self):
		url = self.api_url + "/0/public/Ticker?pair=XBTUSD"
		r = requests.get(url)
		data = r.json()['result']['XXBTZUSD']
		
		price = data['c'][0]	
		time = self.get_time()
	
		lib.pticker(self.name, price, cur_pair, time)
		
		return data

	def assets(self):
		url = self.api_url + "/0/public/AssetPairs"
		r = requests.get(url)
		data = r.json()
		
		pp.pprint(data['result'])

class POLONIEX: 
	
	def __init__(self):
		self.api_url = "http://poloniex.com/public?command="
		self.name = "Poloniex"

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
