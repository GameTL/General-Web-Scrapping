# log BTC-USD, ETH-BTC, ETH-USD 
# https://tcoil.info/how-to-get-price-data-for-bitcoin-and-cryptocurrencies-with-python-json-restful-api/

#* Log Crypto Price v3.4

import requests
import dependances.logger as logger

####SETUP####
CSV_PATH = "Crytoprice_logger/BitCoinPriceLogging.csv"
URL = 'https://min-api.cryptocompare.com/data/price'
ICON_PATH = "dependances\python-logo.png"
#############

def get_current_data(from_sym, to_sym):
    
    parameters = {'fsym': from_sym, 'tsyms': to_sym }
    # response comes as json
    response = requests.get(URL, params=parameters)   
    #https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD Example of what the link looks like with the parameterss
    data = response.json()
    
    return data[str(list(data)[0])]

if __name__ == '__main__' :
    """ import timeit
    print('1. :\t' , timeit.timeit(get_btc,number =1), 'milliseconds')
    print('2. :\t' , timeit.timeit(get_eth,number =1), 'milliseconds') """
    btc_usd = get_current_data('BTC','USD')
    eth_usd = get_current_data('ETH','USD')
    eth_btc = get_current_data('ETH','BTC')
    btc_thb = get_current_data('BTC','THB')
    eth_thb = get_current_data('ETH','THB')

    logger.log2csv(CSV_PATH,[btc_usd, eth_usd, eth_btc, btc_thb, eth_thb], ICON_PATH)

