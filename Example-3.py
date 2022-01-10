"""
OBJECTIVE:
    - Download the images of OLX ads.
    - Learn to download images from the web to our pc.
    - Learn a second way to scrolling a web page.

2022
"""
import requests
from PIL import Image # pip install Pillow
import io
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome('./chromedriver.exe')


driver.get('https://www.olx.co.id')

for i in range(1): 
    try:
        
        button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//button[@data-aut-id="btnLoadMore"]'))
        )
       
        button.click()
        
        WebDriverWait(driver, 10).until(
          EC.presence_of_all_elements_located((By.XPATH, '//li[@data-aut-id="itemBox"]//span[@data-aut-id="itemPrice"]'))
        )

    except:

        break

# Images are only loaded when they are within the user window
# Scroll it ntil the top of the page
driver.execute_script("window.scrollTo({top: 0, behavior: 'smooth'});")
sleep(5)
# Alternative way
driver.execute_script("window.scrollTo({top: 20000, behavior: 'smooth'});")
sleep(5)


announcement = driver.find_elements_by_xpath('//li[@data-aut-id="itemBox"]')

i = 0

for announce in announcement:
    print(announce.get_attribute('innerHTML'))
    
    price = announce.find_element_by_xpath('.//span[@data-aut-id="itemPrice"]').text
    print (price)
    
    description = announce.find_element_by_xpath('.//span[@data-aut-id="itemTitle"]').text
    print (description)

    try:
        url = announce.find_element_by_xpath('.//figure[@data-aut-id="itemImage"]/img')
        # get attribut URL
        url = url.get_attribute('src')
        
        # request library , will get the image content
        image_content = requests.get(url).content

        # Processing Image
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert('RGB')
        file_path = './imagenes/'+ str(i) + '.jpg'  # name to save the image
        with open(file_path, 'wb') as f:
            image.save(f, "JPEG", quality=85)
    except Exception as e:
        print(e)
        print ("Error")
    i += 1