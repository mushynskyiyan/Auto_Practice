import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from data import Config, Wikipedia

expected = Wikipedia(Config.url)

driver = webdriver.Chrome()
driver.get(expected.url)


search_filed = driver.find_element(By.ID, expected.search_field_id)
search_filed.send_keys(expected.info)
# search_filed.send_keys(Keys.ENTER)

driver.find_element(By.XPATH, expected.search_button_id).click()
time.sleep(10)