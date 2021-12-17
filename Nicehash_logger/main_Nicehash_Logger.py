from nicehash import nicehash as nh
import time

###Settings###
#* Set the Path for API Keys, Secret Keys & Organisation ID in this order
API_LOCATION = "C:/#Keys/NicehashAPIKeys.txt" # My personal API Keys | REMOVE
HOST = 'https://api2.nicehash.com'
##############

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

def get_time():
    return time.time()


key, secret, organisation_id = get_api_data()
private_api = nh.private_api(HOST, organisation_id, key, secret)

if __name__ == '__main__' :
    """ import timeit
    print('1. :\t' , timeit.timeit(get_btc,number =1), 'milliseconds')
    print('2. :\t' , timeit.timeit(get_eth,number =1), 'milliseconds') """
    
    with open("Nicehash_logger/NiceHashBalance.csv", "a") as file:
        enitites = [get_time(), get_balance(private_api)]
        for enity in enitites:
            file.write('"' + str(enity) + '",')
        file.write("\n")
    print("""Nichhash Balanced Logged: {}

DONE
DONE""".format(enitites))
    time.sleep(3) 
