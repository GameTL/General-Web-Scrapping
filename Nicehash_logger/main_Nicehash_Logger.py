
#* Nicehash Balance Logging v1.4

from Crytoprice_logger.main_Log_Prices import CSV_PATH, ICON_PATH
from nicehash import nicehash as nh
from datetime import datetime
import dependances.logger as logger

####SETUP####
#* Set the Path for API Keys, Secret Keys & Organisation ID in this order
API_LOCATION = "C:/#Keys/NicehashAPIKeys.txt" # My personal API Keys | REMOVE
HOST = 'https://api2.nicehash.com'
CSV_PATH = "Nicehash_logger/NiceHashBalance.csv"
ICON_PATH = "dependances\python-logo.png"
###############S##############

def get_api_data():
    #! Don't hard code your API Keys, Secret Keys & Organisation ID in the code!
    with open(API_LOCATION, "r") as file:
        key = file.readline().strip() # Use strip() to remove whitespace & /n
        secret = file.readline().strip()
        organisation_id = file.readline().strip()
    return key, secret, organisation_id

def get_balance(private_api):
    my_accounts = private_api.get_accounts()
    return my_accounts['total']["totalBalance"] # 0.00300251 BTC


if __name__ == '__main__' :
    """ import timeit
    print('1. :\t' , timeit.timeit(get_btc,number =1), 'milliseconds')
    print('2. :\t' , timeit.timeit(get_eth,number =1), 'milliseconds') """
    try:
        key, secret, organisation_id = get_api_data()   
        private_api = nh.private_api(HOST, organisation_id, key, secret)
    except:
        logger.error_notification("Error occured while logging into Nicehash")

    logger.log2csv(CSV_PATH,[get_balance(private_api)], ICON_PATH)

