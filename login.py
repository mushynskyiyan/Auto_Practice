from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import auth

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36")
url = "https://app.ecto.com"
driver = webdriver.Chrome(
    executable_path="/Users/jan/PycharmProjects/Cource/AutoPractice/chromedriver/chromedriver",
    options=options
)

try:
    driver.get(url=url)
    time.sleep(2)
    login_input = driver.find_element(By.NAME, 'email')
    login_input.clear()
    login_input.send_keys(auth.login)
    time.sleep(2)
    password_input = driver.find_element(By.NAME, 'password')
    password_input.clear()
    password_input.send_keys(auth.password)
    time.sleep(2)
    login_input.send_keys(Keys.ENTER)
    time.sleep(6)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
