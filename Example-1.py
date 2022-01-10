"""
OBJECTIVE:
    - Extract the price and title of the ads on the OLX autos page.
    - Learn to perform extractions that require a click action to load data.
    - Introduce ourselves to the logic of Selenium
2022
"""
# Target automated https://olx.co.id

import random
from time import sleep
from selenium import webdriver # pip install selenium

# Selenium driver will control the browser
# From this object we will perform the interactions
driver = webdriver.Chrome('./chromedriver') 
# on page
driver.get('https://www.olx.co.id/mobil-bekas_c198')
sleep(3)
driver.refresh() # refresh
sleep(5) # pause

# find xpath
button = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')
for i in range(3): # Scroll page on 3 looping
    try:
        # click button
        button.click()
        # random pause so it doesnt detect the bot
        sleep(random.uniform(8.0, 10.0))
        # interaction with button
        button = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')
    except:
        # handle error
        break

autos = driver.find_elements_by_xpath('//li[@data-aut-id="itemBox"]')


# Function
for auto in autos:
    # extract text
    price = auto.find_element_by_xpath('.//span[@data-aut-id="itemPrice"]').text
    print (price)
    # print it
    description = auto.find_element_by_xpath('.//span[@data-aut-id="itemTitle"]').text
    print (description)