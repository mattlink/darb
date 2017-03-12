import requests
import pprint
pp = pprint.PrettyPrinter(indent=4)

##
# Various Useful Functions
##

def verbose(info):
	print "\n"
	print "exchange: " + info['name']
	print "price: " + info['price']
	print "currency: " + info['currency']
	print "time: " + info['time']

def http_get(url):
	r = requests.get(url)
	data = r.json()
	return data
