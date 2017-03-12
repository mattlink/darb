
class Trader:

    def __init__(self, exchanges):
        self.price_pairs = self.compare(exchanges)

    def compare(self, exchanges):
        price_pairs = []

        for exchange in exchanges:
            ###
            # add a tuple of ( exchange_name, current_price )
            # to the price_pairs array
            #
            price_pairs.append( (exchange['name'], exchange['price']) )


        ###
        # sort the price_pairs array based on the price value,
        # which is converted from string to float value.
        # Sorting: lowest price first -> highest price last
        #
        price_pairs.sort( key = lambda pair: float(pair[1]) )

        return price_pairs

    def verbose(self):
        pairs = self.price_pairs

        low = pairs[0]
        high = pairs[len(pairs) - 1]

        diff = float(high[1]) - float(low[1])
        
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
