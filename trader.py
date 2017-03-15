import funcs as f

class Trader:

    def __init__(self):
        self.verbose = False

    def compare(self, exchange_tickers):
        price_pairs = []

        for ticker in exchange_tickers:
            ###
            # add a tuple of ( exchange_name, current_price )
            # to the price_pairs list
            #
            price_pairs.append( (ticker['name'], ticker['price']) )


        ###
        # sort the price_pairs array based on the price value,
        # which is converted from string to float value.
        # Sorting: lowest price first -> highest price last
        #
        price_pairs.sort(key = lambda pair: float(pair[1]))

        if self.verbose == True:
            f.verbose_comparison(price_pairs)

        return price_pairs
