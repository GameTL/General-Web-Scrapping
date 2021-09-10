# log BTC-USD, ETH-BTC, ETH-USD 
# USD this the master
# based on this https://www.scrapingbee.com/blog/selenium-python/
# interpreter Python 3.9.2(windows store version)
# XPATH == path for fetched html

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time, datetime

def __init__driver():
    global browser
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.set_headless()
    browser = webdriver.Firefox(options=fireFoxOptions)

def get_btc():
    global btc_price
    __init__driver()
    browser.get('https://www.google.com/search?q=btc+to+usd&rlz=1C1CHBF_enTH927TH927&oq=btc+to+usd&aqs=chrome..69i57j0l9.2440j1j7&sourceid=chrome&ie=UTF-8')
    btc_price = browser.find_element_by_xpath("//span[contains(@class,'DFlfde SwHCTb')]").text
    browser.quit()


def get_eth():
    global eth_price
    __init__driver()
    browser.get('https://finance.yahoo.com/quote/ETH-USD/')
    eth_price = browser.find_element_by_xpath("//span[contains(@class,'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)')]").text
    browser.quit()


def get_eth2btc():
    global eth_2_btc_price
    __init__driver()
    browser.get('https://finance.yahoo.com/quote/ETH-BTC/')
    eth_2_btc_price = browser.find_element_by_xpath("//span[contains(@class,'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)')]").text
    browser.quit()

def get_time():
    global date_time
    date_time = datetime.datetime.now()


def logging():
    with open("BitCoinPriceLogging.csv", "a") as file:
        enitites = [date_time, btc_price, eth_price, eth_2_btc_price]
        for enity in enitites:
            file.write('"' + str(enity) + '",')
        file.write("\n")



def main():
    get_btc()
    get_eth()
    get_eth2btc()
    get_time()
    logging()
    print("Logged")

btc_price = 0
eth_price = 0
eth_2_btc_price = 0

main()