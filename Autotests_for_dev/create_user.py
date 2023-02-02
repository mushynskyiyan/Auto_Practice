import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from Autotests_for_dev.authorization import login, pwd
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import random


def random_name():
    return f'Autoyan_{random.randint(9, 100)}'


# def login_to_dev():
#     url = "https://dev-k8s.ecto.com/auth/login"
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     driver.get(url=url)
#     time.sleep(2)
#     login_input = driver.find_element(By.NAME, 'email')
#     login_input.clear()
#     login_input.send_keys(login)
#     time.sleep(2)
#     password_input = driver.find_element(By.NAME, 'password')
#     password_input.clear()
#     password_input.send_keys(pwd)
#     time.sleep(2)
#     login_input.send_keys(Keys.ENTER)
#     time.sleep(6)
#     return driver
url = "https://dev-k8s.ecto.com/auth/login"
url2 = 'https://dev-k8s.ecto.com/app/users'
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(url=url)
time.sleep(2)
login_input = driver.find_element(By.NAME, 'email')
login_input.clear()
login_input.send_keys(login)
time.sleep(2)
password_input = driver.find_element(By.NAME, 'password')
password_input.clear()
password_input.send_keys(pwd)
time.sleep(2)
login_input.send_keys(Keys.ENTER)
time.sleep(6)

#list of optins
option_list = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="app-inner"]/div[2]/div/section[1]/div/div[2]/ul[2]/li/button'))
)
option_list.click()

#users
# user_list = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, '//*[@id="app-header-menu"]/div[3]/ul[1]/li[10]/div[2]/a'))
# )
# user_list.click()
driver.get(url='https://dev-k8s.ecto.com/app/users')
creation_window = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="page-container"]/div/div/div/div/div/div[1]/div/div/a/button'))
)
creation_window.click()
time.sleep(5)
name_field = driver.find_element(By.XPATH, '//*[@id="page-container"]/div/div/div/div/div/form/div[1]/div/div/div/input')
name_field.send_keys(random_name())
username_field = driver.find_element(By.XPATH, '//*[@id="page-container"]/div/div/div/div/div/form/div[2]/div/div/div/input')
username_field.send_keys(random_name())
site_field = driver.find_element(By.XPATH, '//*[@id="select-site"]')
site_field.click()
site = driver.find_element(By.XPATH, '//*[@id="menu-site"]/div[3]/ul/li[2]')
site.click()
roles = driver.find_element(By.XPATH, '//*[@id="select-roles"]')
roles.click()
user_pick = driver.find_element(By.XPATH, '//*[@id="menu-roles"]/div[3]/ul/li[1]')
user_pick.click()
lang_field = driver.find_element(By.XPATH, '//*[@id="select-locale"]')
lang_field.click()
lang_pick = driver.find_element(By.XPATH, '//*[@id="menu-locale"]/div[3]/ul/li[1]')
lang_pick.click()
save_user = driver.find_element(By.XPATH, '//*[@id="page-container"]/div/div/div/div/div/form/div[13]/button')
save_user.click()
time.sleep(5)
driver.close()
driver.quit()




