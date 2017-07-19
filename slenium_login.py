import os
import time
from selenium import webdriver
cd = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = cd 
driver = webdriver.Chrome(cd)
driver.get("http://www.weebly.com#login")

username = driver.find_element_by_id("weebly-username")
time.sleep(1)
set_un = username.send_keys("bekimdisha@gmail.com")
time.sleep(1)
password = driver.find_element_by_id("weebly-password")
time.sleep(1)
set_pass = password.send_keys("!bekim123!")
time.sleep(1)
login_button = driver.find_element_by_class_name("login-btn")
time.sleep(1)
click_login_btn = driver.find_element_by_class_name("login-btn").click()

time.sleep(1)
assert 'Weebly - Getting Started' in str(driver.title) 
time.sleep(3)


#you get the point. 
driver.close()
