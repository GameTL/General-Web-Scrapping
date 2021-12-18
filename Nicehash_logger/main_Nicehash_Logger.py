from nicehash import nicehash as nh
import time
import platform

#* Nicehash Balance Logging v1.2
##########Settings############

#* Set the Path for API Keys, Secret Keys & Organisation ID in this order
API_LOCATION = "C:/#Keys/NicehashAPIKeys.txt" # My personal API Keys | REMOVE
HOST = 'https://api2.nicehash.com'

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

def get_time():
    return time.time()

def error_notification(message):
    if platform.system() == 'Windows':
        from win10toast import ToastNotifier
        # create an object to ToastNotifier class
        n = ToastNotifier()
        
        n.show_toast("Nicehash Logger", message, duration = 15, icon_path = "dependances\python logo.png")



if __name__ == '__main__' :
    """ import timeit
    print('1. :\t' , timeit.timeit(get_btc,number =1), 'milliseconds')
    print('2. :\t' , timeit.timeit(get_eth,number =1), 'milliseconds') """
    try:
        key, secret, organisation_id = get_api_data()   
        private_api = nh.private_api(HOST, organisation_id, key, secret)
    except:
        error_notification("Error occured while logging into Nicehash")

    try:
        with open("Nicehash_logger/NiceHashBalance.csv", "a") as file:
            enitites = [get_time(), get_balance(private_api)]
            for enity in enitites:
                file.write('"' + str(enity) + '",')
            file.write("\n")
        print("""Nichhash Balanced Logged: {}w

DONE
DONE""".format(enitites))
        time.sleep(3) 
    except PermissionError:
        error_notification("PermissionError: CSV is being opened by another program")
    except Exception as e:
        error_notification("Error: {}".format(e))

