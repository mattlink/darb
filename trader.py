import funcs as f

class Trader:

    def __init__(self, exchanges):
        self.price_pairs = self.compare(exchanges)

    def compare(self, exchanges):
        price_pairs = []

        for exchange in exchanges:
            ###
            # add a tuple of ( exchange_name, current_price )
            # to the price_pairs list
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
        f.verbose_comparison(pairs)
