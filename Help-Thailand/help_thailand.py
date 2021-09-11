from selenium import webdriver
import time
def __init__driver():
    global browser
    browser = webdriver.Chrome()


__init__driver()
browser.get('https://popcat.click')
time.sleep(1)
button = browser.find_element_by_xpath("//div[contains(@id,'app')]")
for i in range(10**5):
    button.click()



