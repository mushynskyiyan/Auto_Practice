from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import auth

url = "https://app.ecto.com"
driver = webdriver.Chrome(executable_path="/Users/jan/PycharmProjects/Cource/AutoPractice/chromedriver/chromedriver")

try:
    driver.get(url=url)
    time.sleep(2)
    login_input = driver.find_element(By.NAME, 'email')
    login_input.send_keys(auth.login)
    time.sleep(2)
    password_input = driver.find_element(By.NAME, 'password')
    password_input.send_keys(auth.password)
    time.sleep(2)
    login_input.send_keys(Keys.ENTER)
    time.sleep(2)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
