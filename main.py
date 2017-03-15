import sys

import exchanges
import trader as t

gdax = exchanges.GDAX()
kraken = exchanges.KRAKEN()
poloniex = exchanges.POLONIEX()

exchanges = [gdax, kraken, poloniex]

try:
    if sys.argv[1] == "-v":
        # make verbose
        for exchange in exchanges:
            exchange.verbose = True
except:
    pass

exchange_tickers = []
for exchange in exchanges:
    exchange_tickers.append(exchange.ticker())

trader = t.Trader()
trader.verbose = True

## ~~ ## ~~ ##

print "\n"
trader.compare(exchange_tickers)
print "\n"
