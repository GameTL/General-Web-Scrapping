# log BTC-USD, ETH-BTC, ETH-USD 
# USD this the master
# based on this https://www.scrapingbee.com/blog/selenium-python/
# interpreter Anaconda 3.8.5 with clearterminal
# XPATH == path for fetched html

import requests
from bs4 import BeautifulSoup as bs
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import clearterminal
import time

def get_btc_usd():
    page = requests.get('https://finance.yahoo.com/quote/BTC-USD/').text
    return bs(page, "html.parser").find("span", class_ = 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)').contents[0]

def get_eth_usd():
    page = requests.get('https://finance.yahoo.com/quote/ETH-USD/').text
    return bs(page, "html.parser").find("span", class_ = 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)').contents[0]

def get_eth_btc():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://finance.yahoo.com/quote/ETH-BTC/')
    page = driver.page_source
    driver.quit()
    return bs(page, "html.parser").find("span", class_ = 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)').contents[0]

def get_time():
    return datetime.datetime.now()


if __name__ == '__main__' :
    """ import timeit
    print('1. :\t' , timeit.timeit(get_btc,number =1), 'milliseconds')
    print('2. :\t' , timeit.timeit(get_eth,number =1), 'milliseconds') """

    with open("BitCoinPriceLogging.csv", "a") as file:
        enitites = [get_time(), get_btc_usd(), get_eth_usd(), get_eth_btc()]
        for enity in enitites:
            file.write('"' + str(enity) + '",')
        file.write("\n")
    clearterminal.clear()
    print('Cryto price logged: {}'.format(enitites))
    time.sleep(5)



