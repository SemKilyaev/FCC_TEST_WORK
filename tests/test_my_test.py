import pytest
import pickle
from selenium import webdriver
import time
from locators import MainPageLocators
# driver = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')
# driver.get('https://www.freeconferencecall.com/ru/ru/login')
#
# driver.find_element(*MainPageLocators.EMAIL_LINK).send_keys('darkvanted@gmail.com')
# driver.find_element(*MainPageLocators.PASSWORD_LINK).send_keys('cehr032197')
# driver.find_element(*MainPageLocators.LOGIN_BUTTON_LINK).click()
# pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
#
# driver.quit()
#
# cookies = pickle.load(open("cookies.pkl", "rb"))
# print(cookies)
# driver = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')
# driver.get('https://www.freeconferencecall.com/ru/ru/login')
# for cookie in cookies:
#     driver.add_cookie(cookie)
# time.sleep(5)
# driver.refresh()

import getpass

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir=C:\\Users\\"+getpass.getuser()+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default")  # this is the directory for the cookies

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://www.freeconferencecall.com/ru/ru/login')
