import logging
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from data import Config, Wikipedia

# create logger
logger = logging.getLogger('test_logger')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.FileHandler("test.log")
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to file_handlerh
ch.setFormatter(formatter)

# add file_handler to logger
logger.addHandler(ch)

expected = Wikipedia(Config.url)

driver = webdriver.Chrome()
driver.get(expected.url)


search_filed = driver.find_element(By.ID, expected.search_field_id)
logger.debug(search_filed)
search_filed.send_keys(expected.info)
# search_filed.send_keys(Keys.ENTER)

driver.find_element(By.XPATH, expected.search_button_id).click()
#time.sleep(100)

# first_heading_id = "firstHeading"
# search_result = driver.find_element(By.ID, first_heading_id)
# logger.debug(f'Found result is {search_result.text}')
# assert search_result.text == 'Результаты поиска'
#time.sleep(10)
def test_pattern():
    first_heading_id = "firstHeading"
    search_result = driver.find_element(By.ID, first_heading_id)
    logger.debug(f'Found result is {search_result.text}')
    assert search_result.text == 'Результаты поиска'
    driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[4]/div[2]/ul/li[1]/table/tbody/tr/td[2]/div[1]/a').click()


def test_pattern0():
    first_heading_id = "firstHeading"
    search_result = driver.find_element(By.ID, first_heading_id)
    logger.debug(f'Found result is {search_result.text}')
    assert search_result.text == 'Результаты поиска'