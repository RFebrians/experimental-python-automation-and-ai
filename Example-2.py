"""
OBJECTIVE:
    - Extract the price and title of the ads on the OLX page.
    - Learn to use Selenium waiting for events.
    - Learn to optimize the execution time of our selections by Selenium in an intelligent way
2022
"""
import random
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome('./chromedriver') # User Agent

driver.get('https://www.olx.co.id')


for i in range(3): # Page scrolling
    try:
        # Here are the condition
        button = WebDriverWait(driver, 10).until(
          EC.presence_of_element_located((By.XPATH, '//button[@data-aut-id="btnLoadMore"]'))
        )
        button.click()
        hitung = 20 + (( i + 1 ) * 20 ) # 20 page for initial , then 20 page again for every click 
        # Wait up to 10 seconds for all the information from the last ad to be loaded
        WebDriverWait(driver, 10).until(
          EC.presence_of_element_located((By.XPATH, '//li[@data-aut-id="itemBox"][' + str(hitung) + ']'))
        )
        # Handling Break n Error
    except Exception as e:
        print (e)
        # 
        break

# Find the object
autos = driver.find_elements_by_xpath('//li[@data-aut-id="itemBox"]')

# Function
for auto in autos:
    try:
      price = auto.find_element_by_xpath('.//span[@data-aut-id="itemPrice"]').text
    except:
      price = 'no price'
    print (price)
    description = auto.find_element_by_xpath('.//span[@data-aut-id="itemTitle"]').text
    print (description)
