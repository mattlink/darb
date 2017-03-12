import requests
import pprint
pp = pprint.PrettyPrinter(indent=4)

##
# Various Useful Functions
##

def http_get(url):
	r = requests.get(url)
	data = r.json()
	return data

def verbose(info):
	print "\n"
	print "exchange: " + info['name']
	print "price: " + info['price']
	print "currency: " + info['currency']
	print "time: " + info['time']

def verbose_comparison(pairs):
	low = pairs[0]
	high = pairs[len(pairs) - 1]

	low_price = low[1]
	high_price = high[1]
	diff = float(high_price) - float(low_price)

	print "  Total Exchanges Compared: " + str(len(pairs)) + "\n\n"
	print "--~~ Lowest Price\n "# ~~--\n"
	print "------~~ Exchange: " + low[0] + "\n"
	print "------~~ Price: " + low[1] + "\n"
	print "\n"
	print "--~~ Highest Price\n "# ~~--\n"
	print "------~~ Exchange: " + high[0] + "\n"
	print "------~~ Price: " + high[1] + "\n"
	print "\n"
	print "  Total Price Margin: $" +  str(diff)
