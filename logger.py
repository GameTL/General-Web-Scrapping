
#* Logger Library v1.1

import time
from datetime import datetime
import platform
import win10toast

# there will be more project that needs logging and don't want to write the same code again and again

def get_time():
    return time.time()

def get_human_date_time(seconds):
    return datetime.fromtimestamp(seconds).strftime("%A, %B %d, %Y %I:%M:%S")

def error_notification(name_csv, message, icon_path):
    if platform.system() == 'Windows':
        from win10toast import ToastNotifier
        # create an object to ToastNotifier class
        n = ToastNotifier()
        
        n.show_toast(name_csv, message, duration = 15, icon_path = "dependances\python logo.png")

def log2csv(csv_path, enitites, icon_path=''): # string, list
    try:
        name_csv = csv_path.split("/")[-1]
        time_s = get_time()
        enitites = [time_s, get_human_date_time(time_s)] + enitites
        date_time = get_human_date_time(time_s)
        
        with open(csv_path, "a+") as file:
            for enity in enitites:
                file.write('"' + str(enity) + '",')
            file.write("\n")
        print(f"""{name_csv}: {enitites}

DONE
DONE""")
        time.sleep(3) 
    except PermissionError:
        error_notification(name_csv, "PermissionError: CSV is being opened by another program", icon_path)
    except Exception as e:
        error_notification(name_csv, "Error: {}".format(e), icon_path)



if __name__ == '__main__':
    print('''
This library is used to log data to a csv file.
log2csv is a function that takes a csv path and a list of enitites.
csv path: string consist of the relative path to the csv file.
enitites: list of enities to be logged.

##########################################
if log fails a windows notification will be shown.''')