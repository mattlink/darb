import exchanges.gdax as gdax
import exchanges.kraken as kraken
import exchanges.poloniex as poloniex

def GDAX():
    return gdax.GDAX()

def KRAKEN():
    return kraken.KRAKEN()

def POLONIEX():
    return poloniex.POLONIEX()
