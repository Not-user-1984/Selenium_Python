from lib2to3.pgen2 import driver
from selenium import webdriver
import time
url = 'https://www.avito.ru/'

driver = webdriver.Firefox (executable_path='/Users/diplug/Python _Projetc/Selenium_Python/firefoxdriver/geckodriver')


try:
    driver.get(url=url)
    time.sleep(5)
except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()