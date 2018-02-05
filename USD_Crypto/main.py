import Crypto
from collections import Counter


def get_files():
    return ['usd_' + name + '_4h.csv' for name in ['eth', 'ltc','xmr', 'xrp']]


def get_data(crypto):
    for colnum, colname in enumerate(crypto.header):
        print colname
        print Counter([row[colnum] for row in crypto.data]).most_common(3)
        print ""


if __name__ == "__main__":
    for currency in get_files():
        print currency
        crypto = Crypto.Currency(currency)
        get_data(crypto)
    exit(0)
