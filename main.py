import exchanges
import trader as t

gdax = exchanges.GDAX()
kraken = exchanges.KRAKEN()
poloniex = exchanges.POLONIEX()

exchanges = [gdax.info, kraken.info, poloniex.info]
trader = t.Trader(exchanges)

## ~~ ## ~~ ##

# gdax.verbose()
# kraken.verbose()
# poloniex.verbose()

print "\n"
trader.verbose()
print "\n"
