import sys

import interface as exchanges
import trader as t

gdax = exchanges.GDAX()
kraken = exchanges.KRAKEN()
poloniex = exchanges.POLONIEX()

#exchanges = [gdax, kraken, poloniex]
exchanges = [gdax]

try:
    if sys.argv[1] == "-v":
        # make verbose
        for exchange in exchanges:
            exchange.verbose = True
    elif sys.argv[1] == "-q":
        # make quiet
        for exchange in exchanges:
            exchange.verbose = False
except:
    pass

exchange_tickers = []
for exchange in exchanges:
    exchange_tickers.append(exchange.ticker())

trader = t.Trader()
trader.verbose = True

## ~~ ## ~~ ##

print()
trader.compare(exchange_tickers)
print()
