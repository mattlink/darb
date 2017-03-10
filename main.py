import exchanges

gdax = exchanges.GDAX()
kraken = exchanges.KRAKEN()
poloniex = exchanges.POLONIEX()

## ~~ ## ~~ ##

#kraken.assets()
kraken.ticker()

#poloniex.ticker()

gdax.ticker()
print "\n"




